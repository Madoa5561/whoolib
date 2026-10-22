# whoo (app.whoo) v0.140.0 静的リバースエンジニアリング解析レポート

- 解析日: 2026-10-22（初回 DEX 解析 → jadx 1.5.6 導入後にソースレベルで再検証）
- 対象: `whoo+-+your+world_0.140.0_APKPure.xapk`（APKPure 配布 XAPK / base APK + 19 split）
- 手法: XAPK 展開 → **jadx 1.5.6 でデコンパイルした Java ソース 37,423 ファイル**を主軸に、`AndroidManifest.xml`・`resources.arsc`・native lib を自作パーサで補完（オフライン環境のため apktool 等は未使用）
- 本レポートは**静的解析のみ**。実機での通信キャプチャ（mitmproxy 等）は行っていない。

---

## 0. エグゼクティブ・サマリ

**「whoo がユーザー情報を同意なく外部送信している」という主張は、技術的には"概ね裏付けられる"。**

確認できた事実:

1. **アプリ起動直後（そもそも同意 UI が存在しない）に、広告・アトリビューション SDK が自動初期化される。**
   - `app.whoo.App.onCreate()` 内で **AppLovin MAX 13.5.0**（SDK キー `qpHg9SGpAZaZ8...`）と **Adjust**（アプリトークン `a6hm…<REDACTED>`）を無条件に初期化（復元ソース `App.java:205-219`）。
   - さらに `AndroidManifest.xml` の ContentProvider により、**Firebase Analytics / AppLovin の初期化が `Application.onCreate()` より前に走る**（`FirebaseInitProvider` → `FirebaseApp` 初期化で Analytics 有効化、`AppLovinInitProvider` → SDK 内部初期化）。Vungle / Bigo / Mintegral / Adjust / AdMob も同様に provider を持つ。
2. **同意管理（Consent Management）も同意ダイアログも実装されていない。**
   - Google UMP の同意フォーム呼び出し 0 件、AppLovin MAX の同意フロー有効化 0 件、`setHasUserConsent` / `setDoNotSell` のアプリ側呼び出し 0 件。
   - ログイン画面 `fragment_top.xml` に "By using whoo, you agree to the Terms of Use and Privacy Policy." という**静的テキスト**があるだけで、チェックボックスも同意ボタンもない（`R.string.top_warning`）。
3. **端末識別子が第三者 SDK に渡る。**
   - `AD_ID` 権限を宣言し、**`AdvertisingIdClient.getAdvertisingIdInfo()` の呼び出しが 13 箇所（10 SDK 以上）**ある（AppLovin / Pangle / Mintegral / Bigo / Fyber / Vungle / InMobi / Moloco / PubMatic / Five / Google Ads / Google Analytics）。
   - Adjust は `android_id` / `gps_adid` / `oaid` / `imei`(レガシー) を送信パラメータに含む（`PackageBuilder.java`）。
4. **画面遷移・タップ・権限許諾・購入などの行動ログが Firebase Analytics に送信される。**
   - `defpackage.al3`（`firebaseEventLogger`）が `screen_open` / `screen_close` / `tap_action` / `fgs_*` / `location_push` / `succeed_purchase` などを送信。
   - `MainActivity` は通知タップ時に `notification_uuid`・`variant`・経過時間まで付けて送信する。
5. **交通モード推定結果のテレメトリを外部アップロードする機構が存在する（座標は含まない）。**
   - 端末内に `raw_locations`（緯度経度・精度・速度・充電状態・前面/背面）を保存し、交通モード推定を実行。
   - アップロードされるのは `transportation_mode_results` の **14 列 CSV**（予測ラベル・確率・速度統計・鉄道距離など）。**緯度経度そのものは送信しない**。
   - 送信条件は **Firebase Remote Config `uploadable_user_ids`（許可ユーザー ID リスト）に含まれること**が実質的なゲート（AB テスト `location_model_variant` も参照されるが、後述の通り実質デッドコード）。ユーザー向けのオン/オフ設定は存在しない。
6. **一部の広告 SDK（PubMatic / InMobi）は、アプリから渡されなくても位置権限を利用して緯度経度を自動取得し、自社サーバーへ送信する。**（§5.5）

一方で、確認できなかったこと（＝過剰な主張は避けるべき点）:

- アプリコードが広告 SDK に位置を渡している形跡はない（`setLocation` 等 0 件）。ただし **PubMatic / InMobi の SDK は自ら位置を取得して送信する**（§5.5）。
- **GPS 軌跡の一括アップロード**は行っていない（送信されるのは推定結果の統計値 CSV。座標は端末内に留まる）。
- チャット内容・写真・連絡先が第三者に送られる形跡はない。
- 本レポートは「端末識別子・行動ログが同意ゲートなしに第三者 SDK へ送信される」ことと、「一部の広告 SDK が位置情報を自動取得して送信する」ことを示す。会話内容の流出を示すものではない。

---

## 1. 解析対象とファイル

| 項目 | 値 |
|---|---|
| XAPK SHA-256 | `F98D3E196ACBF8A341ED6214ABB273BEB7EC6573C2705FDF204399F248935DA7` |
| XAPK サイズ | 88,771,239 bytes |
| base APK (`app.whoo.apk`) SHA-256 | `864E34DBF8CB45523324D256FCF46E394E9104852E5D2A71C10BCB0E1A211F77` |
| base APK サイズ | 57,900,890 bytes |
| native split (`config.arm64_v8a.apk`) SHA-256 | `934C897AF2D0AF5854A24F429A72E6CA79F107D4D2895AF90438EDA209D789BF` |
| dex 数 | 6（合計 49,183 クラス） |
| 難読化 | **なし**（クラス名・パッケージ名は原形を保持。R8 によるクラス統合のみ） |

DEX 内訳:

| file | classes | strings |
|---|---|---|
| classes.dex | 10,220 | 45,810 |
| classes2.dex | 8,738 | 44,444 |
| classes3.dex | 11,518 | 41,511 |
| classes4.dex | 8,471 | 38,036 |
| classes5.dex | 10,012 | 55,191 |
| classes6.dex | 224 | 1,665 |

解析用ツール:

- **jadx 1.5.6**（`work/jadx`）— デコンパイル済みソース `work/src/sources`（37,423 ファイル）
- `work/tools/axml.py` — Android バイナリ XML パーサ
- `work/tools/dex.py` — DEX パーサ + 簡易ディスアセンブラ（文字列/メソッド/フィールド解決）
- `work/tools/xref.py` — 全 DEX のクロスリファレンス構築（呼び出し 178,385 件 / 文字列参照 75,433 件）
- `work/tools/arsc.py` / `arsc_ids.py` — `resources.arsc` の文字列プール抽出とリソース ID 逆引き

---

## 2. アプリの基本情報

| 項目 | 値 |
|---|---|
| package | `app.whoo` |
| versionName / versionCode | `0.140.0` / `466` |
| minSdk / targetSdk / compileSdk | 29 / 36 / 36 |
| アプリ名 | whoo（位置情報共有型ソーシャル。Zenly からの移行機能 `ZenlyMigrationRoute` を持つ） |
| Application クラス | `app.whoo.App` |
| 配布元の痕跡 | `com.android.stamp.source=https://play.google.com/store`、`stamp-cert-sha256` 同梱（Google Play 配布ビルドを APKPure が再配布） |

主要パーミッション（`AndroidManifest.xml` より）:

- 位置情報: `ACCESS_FINE_LOCATION` / `ACCESS_COARSE_LOCATION` / **`ACCESS_BACKGROUND_LOCATION`**
- 常駐: `FOREGROUND_SERVICE` / `FOREGROUND_SERVICE_LOCATION` / `RECEIVE_BOOT_COMPLETED` / `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` / `WAKE_LOCK`
- 広告 ID: **`com.google.android.gms.permission.AD_ID`** / `ACCESS_ADSERVICES_AD_ID` / `ACCESS_ADSERVICES_ATTRIBUTION` / `ACCESS_ADSERVICES_TOPICS`
- 端末: `CAMERA` / `RECORD_AUDIO` / `POST_NOTIFICATIONS` / `DETECT_SCREEN_RECORDING` / `DETECT_SCREEN_CAPTURE`
- 課金: `com.android.vending.BILLING`

主要コンポーネント:

| 種別 | 名前 | 備考 |
|---|---|---|
| Activity | `app.whoo.ui.MainActivity` | exported=true（+ アイコン切替用 alias 6 種） |
| Service | `app.whoo.service.location.LocationService` | `foregroundServiceType=0x8`（location） |
| Receiver | `app.whoo.service.location.DeviceBootReceiver` | 起動時に位置情報サービスを再開 |
| Receiver | `app.whoo.service.location.TransitionsReceiver` | Activity Recognition |
| Service | `app.whoo.service.MessagingService` | FCM |

→ **バックグラウンドで常時位置情報を取得し続ける設計**（アプリの主旨上は妥当だが、後述のテレメトリと組み合わさると影響が大きい）。

---

## 3. 起動シーケンス — 同意取得より先に SDK が動く

### 3.1 タイムライン

| # | 実行タイミング | 実行内容 | 根拠 |
|---|---|---|---|
| 1 | プロセス起動時（`Application.onCreate` より前） | ContentProvider による初期化フック: `FirebaseInitProvider`（FirebaseApp 初期化 → Analytics 有効化）、`AppLovinInitProvider`（SDK 内部初期化）、`MobileAdsInitProvider`、`Adjust SystemLifecycleContentProvider`、`VungleProvider`、`BigoAdsProvider`、`MBComponentLifecycleProvider` | `AndroidManifest.xml` の `<provider>` と各 provider の `onCreate()` |
| 2 | `App.onCreate()` 0x00b6–0x00bb | **AppLovin MAX 初期化**（`AppLovinSdk.initialize`） | 下記バイトコード |
| 3 | `App.onCreate()` 0x00c2–0x00db | **Adjust 初期化**（`Adjust.initSdk`） | 下記バイトコード |
| 4 | `App.onCreate()` 0x00fc–0x0118 | 登録ファネル行動ログの同期ワーカー `SyncActivityLogWorker` を `AppStartLogSync` として enqueue | 同上 |
| 5 | 以降（ログイン画面） | "By using whoo, you agree to the Terms of Use and Privacy Policy." を `fragment_top.xml` に**静的表示**（同意操作なし） | `res/layout/fragment_top.xml` / `R.string.top_warning` |

**重要**: 2〜3 は分岐なしの直線コードで、同意状態・年齢・地域による条件分岐が存在しない。そもそも同意を取得する画面・API 呼び出しが存在しないため、SDK 初期化は常に「同意より前」になる。

### 3.2 証拠（jadx 復元ソース）

`app.whoo.App.onCreate()`（`App.java:205-219`）:

```java
// 別処理（接続サービス移行）
ve4.h0(we4.b(bh2Var), null, null, new p5(this, w02Var, 7), 3);

// AppLovin MAX 初期化コルーチン起動（元 bytecode: 0x00b6-0x00bb）
ve4.h0(we4.b(bh2Var), null, null, new ht(this, null), 3);

id idVar = this.e;                       // adjustService（null なら throw するだけ）
if (idVar == null) { ff5.N("adjustService"); throw null; }

AdjustConfig adjustConfig =
    new AdjustConfig(idVar.a, "a6hm…<REDACTED>", AdjustConfig.ENVIRONMENT_PRODUCTION);
adjustConfig.setLogLevel(LogLevel.INFO);
adjustConfig.setOnDeferredDeeplinkResponseListener(new s12(idVar, 6));
Adjust.initSdk(adjustConfig);            // 元 bytecode: 0x00db
```

`ht.invokeSuspend()`（MAX 初期化本体）:

```java
App app2 = this.a;
AppLovinSdk.getInstance(app2).initialize(
    AppLovinSdkInitializationConfiguration
        .builder("qpHg9SGpAZaZ8...ISp99INX_d", app2)
        .setMediationProvider("max")
        .build(),
    new s12(app2, 8));
```

→ SDK キー、メディエーションプロバイダ `"max"`。**`setConsentFlowEnabled(true)` は呼ばれていない**。`if (idVar == null) throw` は DI の null チェックであり、同意判定ではない。

### 3.3 同意管理の不在（ネガティブ・エビデンス）

全 49,183 クラスの呼び出し箇所を走査した結果:

| API | 呼び出し元 | 意味 |
|---|---|---|
| `ConsentInformation.requestConsentInfoUpdate` | `com.applovin.impl.privacy.cmp.a` **のみ** | Google UMP は AppLovin の CMP 実装内からのみ。アプリ側からは呼ばない |
| `AppLovinSdkInitializationConfiguration$Builder.setConsentFlowEnabled` | **0 件** | MAX の同意フローは無効 |
| `AppLovinPrivacySettings.setHasUserConsent` | 自分自身のオーバーロードのみ | アプリは同意状態を設定しない |
| `AppLovinPrivacySettings.setDoNotSell` | 同上 | 同上 |
| `Adjust.setEnabled` / `Adjust.gdprForgetMe` | **0 件** | Adjust を停止/忘却させる処理なし |
| `MobileAds.setRequestConfiguration` | **0 件** | 広告の個人化状態を設定しない |
| `FirebaseAnalytics.setAnalyticsCollectionEnabled` | **0 件** | 解析は既定で有効 |

初回起動時の「同意」に相当するもの（`resources.arsc` と layout 参照から確認）:

- `R.string.top_warning` = `"By using whoo, you agree to the Terms of Use and\nPrivacy Policy."`
- 参照箇所は `res/layout/fragment_top.xml` の **1 箇所のみ**（TextView として表示）
- `R.string.privacy_policy` = "Privacy Policy"、`R.string.terms` = "Terms of Service"（設定画面からのリンク）
- チェックボックス／同意ボタンに相当する文字列は存在しない（"I Agree" は Bigo 広告の入力フォーム用 `bigo_ad_form_agree` のみ）

アプリ内「privacy settings」（`tr8.java` / `fragment_privacy_setting.xml`）のトグルは次の 2 つだけ:

| トグル | 実文字列 | 意味 |
|---|---|---|
| `recommendation_switch` | "Display to recommended users" | 「知り合いかも」リストへの表示可否 |
| `private_mode_switch` | "private mode" | ID 検索への表示可否 |

→ **"利用することで同意したものとみなす" 注意書きのみ**で、同意の取得行為が存在しない。広告・解析・テレメトリを制御する設定はアプリ内に存在しない。GDPR 等が要求する「オプトイン → SDK 初期化」の順序になっていない。

---

## 4. 組み込まれている第三者 SDK

クラス数は DEX 内のパッケージ別集計。初期化は「アプリ起動時」か「広告リクエスト時（MAX アダプタ経由）」か。

| SDK | バージョン | パッケージ | クラス数 | 初期化 | 主な送信先 |
|---|---|---|---|---|---|
| **AppLovin MAX** | **13.5.0** | `com/applovin` | 1,458 | **`App.onCreate()` + InitProvider** | `ms.applovin.com`, `prod-a.applovin.com`, `rt.applovin.com/4.0/pix` |
| **Adjust**（アトリビューション） | — | `com/adjust` | 136 | **`App.onCreate()` + SystemLifecycleContentProvider** | `app.adjust.com`, `adjust.world` |
| Google AdMob | 24.7.0 | `com/google/android/gms/ads` | (Google 全体 15,630) | **MobileAdsInitProvider** | `googleads.g.doubleclick.net` |
| Firebase Analytics | 23.2.0 | `com/google/firebase` | 同上 | **FirebaseInitProvider** | `app-measurement.com/a` |
| Google UMP | 3.2.0 | `com/google/android/ump` | 同上 | 未使用 | — |
| Pangle (ByteDance) | **7.9.1.3** | `com/bytedance` | 3,363 | MAX アダプタ | `api16-access-sg.pangle.io/api/ad/union/sdk/get_ads/` |
| Mintegral | — | `com/mbridge` | 3,474 | MAX アダプタ + Provider | — |
| Bigo Ads | — | `sg/bigo` | 1,892 | **BigoAdsProvider** + アダプタ | `mraid.bigo.sg` |
| Fyber / Inneractive | — | `com/fyber` | 1,647 | MAX アダプタ | `init-mp.fyber.com/init`, `*.inner-active.mobi` |
| Moloco | — | `com/moloco` | 1,117 | MAX アダプタ | `sdkapi.dsp-api.moloco.com/v2/init` |
| InMobi | — | `com/inmobi` | 877 | MAX アダプタ | `config.inmobi.com`, `telemetry.sdk.inmobi.com` |
| Vungle | — | `com/vungle` | 682 | **VungleProvider** + アダプタ | `config.ads.vungle.com`, `adx.ads.vungle.com` |
| PubMatic | — | `com/pubmatic` | 644 | MAX アダプタ | `ow.pubmatic.com/openrtb/2.5` |
| Five (FiveAd) | — | `com/five_corp` | 375 | MAX アダプタ | `*.fivecdm.com` |
| ByteDance APM / PGL | — | `com/apm`, `com/pgl` | 209 / 84 | Pangle 同梱 | `log.byteoversea.com`, `/monitor/collect/...` |
| ML Kit / TFLite / Billing | 18.3.1 / — / 8.3.0 | — | — | — | — |

AppLovin MAX のメディエーションアダプタ（`com/applovin/mediation/adapters/*/BuildConfig`）:

`google`, `bytedance`(Pangle), `mintegral`, `bigo`, `inneractive`(Fyber), `vungle`, `inmobi`, `moloco`, `pubmatic`, `line`

→ **1 つの広告枠に対して 10 社以上のネットワークが入札**し、各社が端末情報・AD_ID を取得する構成。

広告の実装箇所（実例）:

```
Lapp/whoo/ui/landmark/player/LandmarkMediaPlayerFragment;->onCreate()
0005: new-instance v0, Lcom/applovin/mediation/ads/MaxInterstitialAd;
0007: const-string v1, "35cb…<REDACTED>"     ← MAX 広告ユニット ID
0009: invoke-direct {v0, v1}, ...MaxInterstitialAd;-><init>(Ljava/lang/String;)V
0018: invoke-virtual {v0, v1}, ...setListener(...)
001b: invoke-virtual {v0}, ...loadAd()V
```

---

## 5. 実際に外部へ出るデータ

### 5.1 端末識別子（AD_ID ほか）

`AdvertisingIdClient.getAdvertisingIdInfo()` の呼び出し元（13 箇所）:

| SDK | クラス |
|---|---|
| AppLovin | `com.applovin.impl.v` |
| Pangle | `com.bytedance.sdk.openadsdk.eum.hnj.hn.hnj$1` |
| Five | `com.five_corp.ad.internal.tracking_data.b` |
| Fyber | `com.fyber.inneractive.sdk.config.n0` |
| Google Ads | `com.google.android.gms.internal.ads.zzcba` |
| Google Analytics | `com.google.android.gms.measurement.internal.zzhh` / `zznn` |
| InMobi | `com.inmobi.media.qc` |
| Mintegral | `com.mbridge.msdk.config.component.info.provider.subprovider.a` / `foundation.tools.g$a` |
| Moloco | `com.moloco.sdk.internal.services.o` |
| PubMatic | `com.pubmatic.sdk.common.utility.POBAdvertisingIdClient$a` |

Adjust 側の送信パラメータ（`PackageBuilder.checkDeviceIds` ほか）:

- `gps_adid`（Google Advertising ID）
- `android_id`（Android ID。`AndroidIdUtil.getAndroidId`）
- `oaid`（中国向け OAID。`Reflection.getOaidParameters`）
- `imei`（レガシー。`Reflection.getImeiParameters` — targetSdk 36 では取得不可）
- `fire_adid`

→ **広告 ID と Android ID が、アトリビューション（Adjust）と 10 社超の広告網に渡る**。これは「ユーザー情報の外部送信」の技術的中核。

### 5.2 アプリ→自社 API のヘッダ（`bt.intercept()`）

jadx 復元ソース（`defpackage/bt.java`、抜粋）:

```java
// case 1: 認証ヘッダ
String strB = ((fgc) obj).b("access_token");
String ua = p51.k("app.whoo/0.140.0 Android/", Build.VERSION.RELEASE, "/", Build.MODEL);
Locale locale = Locale.getDefault();
if (ff5.g(locale.getLanguage(), "zh")) {
    language = country.length() > 0
        ? la2.h(locale.getLanguage(), "-", locale.getCountry())
        : locale.getLanguage();
} else {
    language = locale.getLanguage();
}
kg9 kg9VarB2 = l49Var2.e.b();
kg9VarB2.a(HttpHeaders.ACCEPT_LANGUAGE, language);
kg9VarB2.a("user-agent", ua);
if (strB != null && strB.length() != 0) {
    kg9VarB2.a(HttpHeaders.AUTHORIZATION, "Bearer ".concat(strB));
}

// 別 case: サポートチャット宛のみ端末トークンを付与
if (q3b.Q(strB2, "/api/support/", false)) {
    ...
    request.a("X-Whoo-Support-Device-Token", token);  // 端末ごとにランダム UUID を生成し保存
}
```

→ 全 API リクエストに **OS バージョン・端末モデル・言語・認証トークン**が付与され、サポートチャット宛のリクエストには **端末 UUID** も付く。UA による端末フィンガープリントが成立する。

### 5.3 Adjust のイベント

| トークン | 用途 | 根拠 |
|---|---|---|
| `z90k4e` | サブスクリプション収益（`setRevenue(double, currency)` 付き） | `Lk0a;->invokeSuspend` 0x0272–0x027a |
| `dhuiz0` | 登録フロー中のイベント（プロフィール画像設定時） | `sa9.emit` 0x0031, `gc9.emit` 0x004e |

→ 課金収益とコンバージョンが Adjust（第三者）に送信される。

### 5.4 Firebase Analytics（行動ログ）

- `FirebaseAnalytics.getInstance()` の呼び出し 17 箇所。収集停止 API は未使用、`firebase_analytics_collection_enabled=false` の manifest meta-data も無し → **既定で有効**。
- 自動収集: `first_open`, `session_start`, `user_engagement` 等 + 端末情報 + AD_ID。
- さらにアプリ独自の行動イベントを送信（`defpackage.al3` = `firebaseEventLogger`）:

| イベント名 | 内容 | 根拠 |
|---|---|---|
| `screen_open` / `screen_close` | 画面名（`Screen` enum: `map`, `group_chat`, `settings_page`, `three_plans_subscription` など） | `Action.java`, `GroupChatFragment.java:517,551` |
| `tap_action` / `display_action` | 画面名 + `element_id` + 任意パラメータ | `al3.a()` |
| `fgs_direct_start` / `fgs_restarted_by_system` 等 | 位置情報 Foreground Service の起動・停止・再起動、`session_id`、`app_to_receiver_ms` などの計測値 | `FgsWorkerEvent.java`, `LocationService.java:396-577` |
| `location_push` | プッシュによる位置更新の成否・理由・時刻 | `al3.d()` |
| `measure_action` | 任意の計測イベント（key-value） | `al3.e()` |
| `succeed_purchase` / `succeed_subscription_upgrade` | 購入・アップグレード | `Action.SUCCEED_PURCHASE`, `al3.f()` |
| `tap_action`（PushNotification） | 通知タップ、`notification_uuid`・`variant`・`elapsed_hours_since_post` | `MainActivity.java:631-650` |

→ 画面遷移・タップ・権限許諾・購入・通知反応といった**行動データが Google の Firebase Analytics に送信**される。`Action` enum には位置権限の許諾（`OpenRequestLocationPermission` / `CompleteLocationSetting`）やスクリーンショット（`ScreenShot`）も含まれる。

### 5.5 広告SDKによる位置情報の自動取得（PubMatic / InMobi）— 主張は一部 true

アプリ側コードは広告 SDK に位置を渡していない（`setLocation` / `allowLocationAccess` の呼び出し **0 件**、`AdRequest` の構築 **0 件**）。しかし、**SDK 自身が位置権限を利用して位置を取得し、送信する実装**が 2 社に存在する。

**PubMatic（入札シグナルに lat/lon）**

- `POBSDKConfig` の `allowLocationAccess` 既定値が **true**（`private boolean a = true;`）。アプリは `OpenWrapSDK.allowLocationAccess(false)` を呼んでいない。
- `POBLocationDetector.getLocation()` が `LocationManager.getLastKnownLocation()` と `requestLocationUpdates()` で位置を取得（`ACCESS_FINE/COARSE_LOCATION` を検査）。
- `POBBaseSignalBuilder.getDeviceInfo()` → `POBCommonOrtbJsonHelper.getDeviceObject()` → `geo { lat, lon, accuracy, lastfix }` を生成。
- MAX アダプタ `PubMaticMediationAdapter.collectSignal()` → `POBSignalGenerator.generateSignal()` 経由で**入札シグナルに含まれる**。
- 送信先: `ow.pubmatic.com`

**InMobi（リクエスト/テレメトリに lat/lon）**

- `C0521e6.b()` が `FusedLocationProviderClient.getLastLocation()` / `LocationManager.getLastKnownLocation()` で位置を取得。
- `u-latlong-accu` = `"<lat>,<lon>,<accuracy>"`、`u-ll-ts`、`loc-granularity`、`sdk-collected=1` を生成（`C0521e6.a()`）。
- 広告リクエスト／テレメトリの POST ボディに `map.putAll(C0521e6.a.b())` で合成される（`D.f()` / `C0653nc.f()`）。
- 条件は「位置権限あり」かつ「端末の位置情報が有効」（`c()` と `e()`）。
- 送信先: `ads.inmobi.com`, `telemetry.sdk.inmobi.com`

**それ以外のネットワーク**

`com.applovin` / `com.google.android.gms.ads` / `com.bytedance` / `com.mbridge` / `com.vungle` / `sg.bigo` / `com.fyber` / `com.moloco` には、**位置を自前で取得するコード（`LocationManager` / `getLastKnownLocation` / `FusedLocationProviderClient`）が存在しない**（Google の mediation API は `Location` を受け取る口を持つが、アプリは値を渡していない）。Fyber・Moloco の入札モデルには lat/lon フィールドがあるが、**値を設定する呼び出しは存在しない**ため送信されない。

→ 「広告に緯度経度を送信している」という主張は、**PubMatic と InMobi についてはコード上 true**。ただし「アプリが全広告網に位置を渡している」は false であり、送信主体はアプリではなく SDK の自動取得である。実際の送信有無は MAX の入札設定（どのネットワークが有効か）に依存するが、SDK・アダプタ・呼び出し経路はすべて同梱されている。

### 5.6 登録ファネルの行動ログ（first-party、端末 UUID 付き）

- `o8c.a(ActivityLogStep, SessionType)` が登録・ログインの各ステップを記録（`ActivityLogStep`）:
  `input_email`, `input_password`, `input_birthday`, `input_display_name`, `input_profile_image`,
  `accept_location`, `accept_background_location`, `accept_push_notification`, `created_account` など
- `POST activity_logs`（`s9.java`）で送信。リクエストは
  `ActivityLogRequest(globalUuid, sessionUuid, sessionType, step, timestamp)`
- `globalUuid` は端末に永続化された UUID（`ba` / `vdb`）で、**アカウント作成前から端末単位の識別が可能**
- 起動時に `SyncActivityLogWorker`（`AppStartLogSync`）で未送信分を同期

→ 位置情報・通知の権限許諾や生年月日入力などの**操作イベントが、端末 UUID と時刻付きでサーバーに記録**される（入力値そのものではなくステップ名のみ）。

---

## 6. 自社サーバーと交通モード・テレメトリ

### 6.1 API

- base URL: `https://www.wh00.ooo/api/`（`p82.java` の DI 定義）
- 予備ホスト: `www-a.wh00.ooo`
- 主なエンドポイント（jadx 復元ソースの Retrofit アノテーション）:

| メソッド | パス | 用途 |
|---|---|---|
| `PUT` | `user/location` | **現在位置の送信**（`UserLocationRequestDTO`） |
| `POST` | `user/location/end_stay` | 滞在終了 |
| `GET` | `/api/locations` | 友達の位置取得 |
| `GET` | `/api/location/trigger_events` | 位置トリガ |
| `POST` | `activity_logs` | 登録ファネル行動ログ |
| `POST` | `/android/raw_locations/presigned_url` | **テレメトリ CSV のアップロード先** |
| `GET` | `users/{user_id}/footprints` | 足跡画像 |

位置情報 DTO（`ggc.java` / `UserLocationRequestDTO`）の中身:

```java
UserLocationRequestDTO(
  UserLocation(latitude, longitude, speed, stayedAt, bearing,
               horizontalAccuracy, gettingLocationType),
  UserBattery(level, state),
  AppState(active),
  UserSpot(id) )
```

→ 現在位置に加えて**バッテリー残量・充電状態・アプリの前面/背面**まで送信する（友達にバッテリーを見せる機能のため）。

### 6.2 交通モード推定（端末内処理）

ローカル DB（Room）スキーマ:

```sql
CREATE TABLE `raw_locations` (
  id, latitude REAL, longitude REAL, horizontal_accuracy REAL, altitude REAL,
  velocity REAL, bearing REAL, time INTEGER,
  state INTEGER, is_foreground INTEGER, charging INTEGER, battery_level REAL,
  expired INTEGER, valid INTEGER, provider TEXT,
  is_wifi_connected INTEGER, enable_post INTEGER,
  significant_motion_triggered INTEGER, has_speed INTEGER,
  speed_accuracy_meters_per_second REAL, is_jumped INTEGER,
  location_model_variant TEXT, jump_score REAL,
  consecutive_jump_count INTEGER, jump_input_distance REAL, stayed_at INTEGER )

CREATE TABLE `wifi_infos` (
  id, network_hash, bssid TEXT, signal_strength REAL, ... )          -- ★ Wi-Fi BSSID

CREATE TABLE `cellular_infos` (
  cell_id, new_radio_cell_id, location_area_code,
  mobile_country_code, mobile_network_code, ... )                    -- ★ セル Tower ID

CREATE TABLE `transportation_mode_results` (
  predicted_label_id, predicted_probability, rail_data_available,
  window_point_count, stop_ratio, speed_median, speed_p90,
  window_total_distance_m, ... )
```

`raw_locations` は緯度経度・精度・高度・速度・方位に加え、**フォアグラウンド/バックグラウンド状態、充電状態、バッテリー残量、Wi-Fi 接続有無、歩行/移動トリガ**まで記録する。単なる座標列ではなく、**行動・生活パターンを含む高解像度の移動履歴**が端末内に蓄積される。

- 交通モード推定モデル: `assets/transportation_mode_detection_2026-06-08-001.tflite`
- 位置ジャンプ検出: `assets/location_jump_detection_2026-05-22-002.tflite`
- 東京の鉄道データ: `assets/railways_2026-06-15_tokyo.bin`

### 6.3 外部へ出るのは「推定結果の CSV」のみ（座標は含まない）

アップロード処理（`oyb.java:25-341`）:

1. `POST /android/raw_locations/presigned_url`（`Authorization: Bearer <access_token>`）→ `PresignedUrlResponse(id, url, key)` を取得
2. 対象行を CSV に変換。ヘッダは次の 14 列:

```
id, raw_location_id, window_end_time, predicted_label_id, predicted_probability,
confirmed_label_id, rail_data_available, window_point_count, stop_ratio,
speed_median, speed_p90, window_total_distance_m, rail_distance_median, rail_near_ratio
```

3. `Content-Type: text/csv` で**署名付き URL（S3 互換）へ PUT**

→ 送信されるのは `transportation_mode_results` の統計値のみ。**緯度経度・Wi-Fi BSSID・セル ID はアップロード対象外**（端末内 DB に留まる）。ただし `window_end_time` と鉄道距離・速度統計の組み合わせから、行動パターンは相当程度推測できる。

ワーカーは `app.whoo.ui.maps.UploadRawLocationsWorker`（`App;->a()` の WorkManager マップに登録、`or4.java:57`）。

### 6.4 誰がアップロードするかはサーバーが決める（ユーザー設定なし）

SharedPreferences `location_telemetry_participation` が 4 状態を持ち、`bx4.d()`（`bx4.java:232-273`）が復元する:

| 保存値 | 状態クラス | 意味 |
|---|---|---|
| `disabled`（既定） | `zgb` | 収集・送信なし |
| `record_only` | `ahb` | 端末内に記録のみ |
| `cohort_<variant>` | `ygb` | 実験コホート（記録のみ） |
| `uploader_<variant>` | `bhb` | **アップロード実施** |

参加判定（`mh0.java:132-170`、`yf6.java:300-320`）:

1. **Firebase Remote Config の `uploadable_user_ids`** を取得（`ke9.java:573`。JSON を `UploadableUserIds` にデシリアライズ。取得失敗時は空リスト）
2. **AB テスト `location_model_variant`** の値を取得（`jv7.a0()`。既定 `none`、他に `model_c` / `model_and_rule_c`）
3. 分岐:
   - ユーザー ID が許可リストに**含まれる** → **`uploader_<variant>`**。このとき variant が `TelemetryParticipation$ABVariant`（`none` / `sm_v1`）に一致しなければ `NONE` 扱いになるため、実際には **`uploader_none`** になる
   - 許可リストに**含まれない** かつ variant が `ABVariant` に一致 → `cohort_<variant>`（記録のみ）
   - 許可リストに**含まれない** かつ variant が不一致（`model_c` 等） → `record_only`
4. `uploader_*` のとき `UploadRawLocationsWorker` を enqueue（`yf6.java:303`）
5. アップロードは **24 時間に 1 回まで**に制限（`v5c.java`、`TWENTY_FOUR_HOURS_MILLIS`）

**実装上のねじれ**: AB テストの variants は `none` / `model_c` / `model_and_rule_c` なのに、テレメトリ側の enum は `none` / `sm_v1` しか解釈しない。そのため `sm_v1` は到達不能（デッドコード）で、**「許可リストに入っているか」が実質的な送信スイッチ**になっている。

→ **ユーザーがオン/オフできる UI は存在せず**（`resources.arsc` にテレメトリ設定の文字列なし）、**サーバー側の許可リスト次第で外部送信が有効化される**。同意の観点で最も注意を要する設計。

---

## 7. リスク評価

| # | 事象 | 影響 | 確度 | 根拠 |
|---|---|---|---|---|
| R1 | 起動直後に広告/アトリビューション SDK が初期化され、AD_ID・Android ID・IP・端末情報が 10 社超へ送信 | 高（同意なきトラッキング） | **確認済み** | §3, §5.1 |
| R2 | 同意管理が未実装（UMP/MAX CMP/個別オプトインなし） | 高（GDPR/改正電気通信事業法/APPI 上の瑕疵） | **確認済み** | §3.3 |
| R3 | 画面遷移・タップ・権限許諾・購入・通知反応が Firebase Analytics（Google）へ送信 | 中〜高（行動プロファイリング） | **確認済み** | §5.4 |
| R4 | 交通モード推定結果（時刻・速度・鉄道距離など）の外部アップロードが、Remote Config の許可リスト + AB で遠隔制御され、ユーザー設定がない | 中 | **確認済み**（送信コード・条件分岐） | §6.3–6.4 |
| R5 | Wi-Fi BSSID / セル ID を端末内に収集（アップロードはされない） | 中（高精度位置の代替識別子） | **確認済み**（DB スキーマ） | §6.2 |
| R6 | バックグラウンド位置情報 + 起動時自動再開 | 中（常時追跡） | **確認済み** | §2 |
| R7 | UA による端末フィンガープリント | 低〜中 | **確認済み** | §5.2 |
| R8 | 登録ファネル行動ログ（権限許諾を含む）を端末 UUID 付きで自社サーバーへ送信 | 中 | **確認済み** | §5.6 |
| R9 | **PubMatic / InMobi の SDK が位置権限を利用して緯度経度を自動取得し、自社サーバーへ送信**（アプリ側の `setLocation` は 0 件） | 中〜高 | **確認済み**（SDK コード） | §5.5 |
| R10 | 会話・写真・連絡先の第三者送信 | — | **否定**（証拠なし） | 全 DEX 走査 |

---

## 8. 主張のファクトチェック

| 主張 | 判定 | コメント |
|---|---|---|
| 「whoo はユーザー情報を同意なく外部送信している」 | **一部 true** | 起動時に Adjust / AppLovin MAX / Firebase が初期化され、端末識別子と行動ログが第三者へ送られる。同意ゲートは存在しない。 |
| 「位置情報を外部（第三者）に送信している」 | **true（一部の広告網）** | 自社サーバー（wh00.ooo）へ現在位置を送信（`PUT user/location`）。さらに **PubMatic（入札シグナルの `geo.lat/lon`）と InMobi（`u-latlong-accu`）は SDK が位置権限を利用して自動取得し送信**する。アプリコードが渡しているわけではない。他ネットワーク（AppLovin/Google/Pangle 等）は位置送信なし。 |
| 「会話や写真が漏れている」 | **false（証拠なし）** | 該当する送信コード・エンドポイントは発見できず。 |
| 「最新版でも変わっていない」 | **true（0.140.0 時点）** | versionCode 466 の最新 XAPK で上記を確認。 |

---

## 9. 解析の限界・未検証事項

1. **動的解析なし**: 実機での通信キャプチャ（mitmproxy / PCAPdroid）による送信内容の実測は未実施。SDK の送信内容はコードと既知の仕様に基づく推定を含む。
2. **プライバシーポリシー本文の確認なし**: ネットワーク遮断環境のため `https://www.wh00.ooo/privacy_policy.html` を取得できていない。「同意の有無」の法的評価には本文との突合が必要。
3. **R8 によるクラス統合**: jadx のデコンパイルは 339 件のエラーを伴い、巨大クラス（例 `mh0`）には複数クラスが統合されている。主要経路（SDK 初期化・テレメトリ・API）は復元できたが、一部の周辺処理は完全復元できていない。
4. **サーバー側フラグの実値不明**: `uploadable_user_ids` に実際に何人・どのユーザーが含まれるか、AB `location_model_variant` の配布比率はサーバー側であり静的解析では不明。
5. **split APK**: `config.*` はリソースのみ。arm64 native lib は文字列スキャンのみ（`libsigner.so`, `libapminsight*.so` は難読化/動的ロードで詳細未解明）。

---

## 10. 推奨事項

### ユーザー向け

1. **広告 ID のリセット/削除**（Android 設定 → プライバシー → 広告）。ただし Android ID はリセット不可。
2. 位置情報の権限を「アプリ使用中のみ」に変更（`ACCESS_BACKGROUND_LOCATION` を剥奪）。
3. 可能なら DNS/広告ブロッカー（AdGuard 等）で `app.adjust.com`, `ms.applovin.com`, `app-measurement.com`, `*.pangle.io` 等を遮断。
4. プライバシーポリシー本文とデータセーフティ申告の突合、および削除請求（§6 のテレメトリ含む）を検討。

### 開発者・運営向け

1. **SDK 初期化を同意後に遅延**（UMP または MAX CMP を有効化し、`setConsentFlowEnabled(true)` + `setHasUserConsent` を実装）。現状は同意 UI 自体が無い。
2. テレメトリ参加を**明示的オプトイン**に変更し、設定画面にトグルを追加。`record_only` を既定に。
3. AD_ID 以外の識別子（Android ID / OAID / IMEI 系）の送信を停止し、必要最小限に削減。
4. Wi-Fi BSSID の収集はハッシュ化・短期保持・アップロード対象外を徹底。
5. Firebase Analytics の収集を同意後に限定（`setAnalyticsCollectionEnabled`）。
6. データセーフティ申告とプライバシーポリシーに「Adjust / AppLovin MAX / 各広告網への識別子送信」および「交通モード推定結果の外部送信（許可ユーザーのみ）」を明記。

---

## 11. 付録 A: IOC（ネットワーク先）

| ドメイン | 用途 |
|---|---|
| `www.wh00.ooo`, `www-a.wh00.ooo` | whoo 自社 API |
| `app.adjust.com`, `adjust.world` | Adjust（アトリビューション） |
| `ms.applovin.com`, `prod-a.applovin.com`, `rt.applovin.com`, `rt.applvn.com` | AppLovin MAX |
| `app-measurement.com` | Firebase Analytics |
| `googleads.g.doubleclick.net`, `ad.doubleclick.net` | Google 広告 |
| `api16-access-sg.pangle.io` | Pangle (ByteDance) |
| `init-mp.fyber.com`, `*.inner-active.mobi` | Fyber / Inneractive |
| `config.ads.vungle.com`, `adx.ads.vungle.com` | Vungle |
| `config.inmobi.com`, `ads.inmobi.com`, `telemetry.sdk.inmobi.com` | InMobi |
| `sdkapi.dsp-api.moloco.com` | Moloco |
| `ow.pubmatic.com`, `ads.pubmatic.com` | PubMatic |
| `mraid.bigo.sg` | Bigo Ads |
| `*.fivecdm.com` | Five |
| `log.byteoversea.com` | ByteDance APM |

## 12. 付録 B: 識別子・キー

| 種別 | 値 |
|---|---|
| Adjust app token | `a6hm…<REDACTED>` |
| AppLovin SDK key | `qpHg…<REDACTED>` |
| AppLovin 広告ユニット | `35cb…<REDACTED>` |
| AdMob App ID | `ca-app-pub-…~<REDACTED>` |
| Google Maps API key | `AIza…<REDACTED>` |
| Adjust イベント | `z90k4e`（収益）, `dhuiz0`（登録） |

## 13. 付録 C: 主要クラス一覧（証拠）

jadx 復元ソース上の名前で記載（`defpackage` は R8 による難読化名）。

| クラス / ファイル | 役割 |
|---|---|
| `app.whoo.App` | Application。`onCreate()` で MAX / Adjust 初期化、Worker 登録 |
| `defpackage.ht` | MAX 初期化コルーチン（SDK キー・`setMediationProvider("max")`） |
| `defpackage.bt` | OkHttp Interceptor（UA / Bearer / Accept-Language / `X-Whoo-Support-Device-Token`） |
| `defpackage.bx4` | RemoteConfig（`location_telemetry_participation`）読み出し + 状態マップ |
| `defpackage.mh0` | 許可リスト + AB → テレメトリ参加状態の永続化 |
| `defpackage.yf6` | `uploader_*` のとき `UploadRawLocationsWorker` を enqueue |
| `defpackage.oyb` | presigned URL 取得 → 交通モード結果 CSV を PUT |
| `defpackage.ihb` | テレメトリ・アップローダ |
| `defpackage.v5c` | アップロード間隔の制御（24 時間） |
| `defpackage.ke9` | Firebase Remote Config `uploadable_user_ids` 取得 |
| `app.whoo.ui.maps.UploadRawLocationsWorker` | WorkManager ワーカー |
| `app.whoo.location.telemetry.db.TelemetryDatabase_Impl` | `raw_locations` / `wifi_infos` / `cellular_infos` |
| `defpackage.tr8` | プライバシー設定画面（トグル 2 個） |
| `defpackage.al3` | Firebase 行動ログ送信（screen / tap / fgs / purchase） |
| `app.whoo.Action` / `app.whoo.Screen` | 送信する行動・画面の enum |
| `defpackage.o8c` / `defpackage.s9` | 登録ファネル行動ログと `POST activity_logs` |
| `com.pubmatic.sdk.common.utility.POBLocationDetector` | 位置の自動取得（LocationManager） |
| `com.pubmatic.sdk.openwrap.core.signal.POBBaseSignalBuilder` | 入札シグナルに `geo.lat/lon` を付与 |
| `com.inmobi.media.C0521e6` | 位置の自動取得（FusedLocation / LocationManager） |
| `com.inmobi.media.D` / `C0653nc` | `u-latlong-accu` を含むリクエスト送出 |
| `app.whoo.ui.landmark.player.LandmarkMediaPlayerFragment` | MAX インタースティシャル広告 |
| `com.adjust.sdk.PackageBuilder` | 識別子パラメータ生成 |

### 修正履歴（jadx 導入後）

| 項目 | 初回解析（DEX のみ） | jadx 検証後 |
|---|---|---|
| 初回同意 UI | "I Agree" ボタンありと記載 | **誤り**。実体は `fragment_top.xml` の静的注意書き。同意ボタンは存在しない |
| テレメトリ内容 | 生 GPS 軌跡をアップロードと記載 | **誤り**。送信は交通モード推定結果の 14 列 CSV。座標は含まない |
| テレメトリ条件 | AB フラグのみ | Remote Config `uploadable_user_ids` の**許可リスト**が実質ゲート。24 時間に 1 回 |
| 広告への位置情報 | 「広告 SDK へ位置情報は渡っていない」と記載 | **誤り**。アプリは渡していないが、PubMatic / InMobi の SDK が**自ら取得して送信**する（§5.5） |

---

## 14. 付録 D: 再現手順

```powershell
# 1. XAPK 展開
python -c "import zipfile; zipfile.ZipFile('whoo+-+your+world_0.140.0_APKPure.xapk').extractall('work/xapk')"

# 2. jadx（サンドボックス対策で config/cache をワークスペース内へ）
$env:JADX_CONFIG_DIR="$PWD\work\jadxcfg"; $env:JADX_CACHE_DIR="$PWD\work\jadxcache"
.\work\jadx\bin\jadx.bat -d work\src --no-res --show-bad-code -j 8 work\xapk\app.whoo.apk

# 3. 主要な検索
rg -n "AdjustConfig|AppLovinSdkInitializationConfiguration" work/src/sources/app/whoo/App.java work/src/sources/defpackage/ht.java
rg -n "location_telemetry_participation|uploadable_user_ids" work/src/sources
rg -n "raw_locations/presigned_url|text/csv" work/src/sources
```

---

*本レポートは静的解析の結果であり、法的判断ではありません。*
