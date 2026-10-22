# GitHub 公開前チェックリスト

このワークスペースには「公開してよいもの」と「絶対に公開してはいけないもの」が
混在しています。以下は技術的・法的リスクの観点からの整理です（法的助言ではありません）。

## 判定表

| 対象 | 判定 | 理由 |
|---|---|---|
| `whoo+-+your+world_0.140.0_APKPure.xapk` | **✕ 即削除** | 著作物（APK）の再配布。Google Play 配布ビルドのコピーであり、DMCA 等の対象 |
| `work/` 全体（`apk/`, `xapk/`, `src/`, `cache/`, `res/`） | **✕ 即削除** | APK 本体、逆コンパイル成果物（派生著作物）、API キー・SDK キーを含む |
| `jadx-*.zip`（3 個） | **✕ 削除推奨** | 再配布不要。合計 240MB 超でリポジトリを肥大化させる |
| `build/`, `whoolib.egg-info/`, `.pytest_cache/`, `__pycache__/` | **✕ 削除** | 生成物。絶対パス（`C:\Users\...`）が混入する可能性 |
| `whoo_iocs.csv`（未マスク） | **✕ 公開不可** | Adjust トークン、AppLovin SDK キー、AdMob ID、広告ユニット ID を含む |
| `whoo_解析レポート.md`（未マスク） | **✕ 公開不可** | Google Maps API キー、各種 SDK キー、アプリのコード断片を含む |
| `whoolib/`（フル機能クライアント） | **△ 非公開を強く推奨** | コード自体は独自著作物だが、ToS 違反・悪用リスクが高い（下記） |
| `docs/ENDPOINTS.md` / `docs/MODELS.md` | **△ 条件付き** | 私的 API の完全マップ。事実の記述だが ToS・営業秘密の観点でリスク |
| `dist/whoolib-1.0.0-py3-none-any.whl` | **△** | 中身は `whoolib` と同じリスク |
| `README.md` / `LICENSE` / `pyproject.toml` | **○** | 独自コンテンツ。キーなし |
| `tests/` / `tools/` | **○** | 独自コード。`work/` を前提にするがパス参照のみ |
| `public/`（マスク済みレポート・IOC） | **○** | キーを伏字化したコピー |

## なぜ `whoolib` は「△」なのか

1. **ToS**: 非公式クライアントの公開は、whoo の利用規約（自動アクセス・逆コンパイル禁止）に
   違反する可能性が高いです。アカウント停止・民事請求のリスクがあります。
2. **悪用リスク**: このアプリは位置情報共有型です。`update_location()`（任意座標の送信）、
   `register()`（アカウント作成）、メッセージ・友達申請 API を備えたクライアントを公開すると、
   ストーキング・スパム・なりすましの道具になります。
3. **著作権**: Python コード自体は独自ですが、`models.py` のクラス名・`_endpoints.py` の
   パス一覧はアプリ由来の識別子です。事実の記述として保護されにくい一方、争いになる余地はあります。

**公開する場合の最低条件**

- リポジトリを **private** にする、または
- **読み取り専用**に絞る（`update_location`, `register`, メッセージ送信, 友達申請を削除）
- README に「自分のアカウントのみ」「ToS 遵守」「ストーキング禁止」を明記
- レート制限を維持（既定 3 req/s）

## なぜ API キーを伏せるのか

APK に埋め込まれたキーは「秘密」ではありませんが、公開すると以下が起きます。

| キー | リスク |
|---|---|
| Google Maps API key (`AIza…`) | 第三者が quota を消費し、whoo 側の地図機能が停止。Google の利用規約違反 |
| AppLovin SDK key (`qpHg…`) | 収益・アトリビューションの不正操作 |
| Adjust token (`a6hm…`) | インストール計測の偽装（attribution fraud） |
| AdMob App ID / 広告ユニット | 広告配信のなりすまし・不正リクエスト |

GitHub の secret scanning は `AIza…` を検知して Google に通知することがあります。
**マスク済みコピーは `public/` に生成済み**です（`python tools/redact_secrets.py`）。

## すでに push してしまった場合

**公開リポジトリは、ファイルを消すコミットだけでは不十分**です。Git の履歴に残ります。

```powershell
# 1. まずリポジトリを private に戻す（GitHub Settings → Danger Zone、または gh）
gh repo edit --visibility private

# 2. 履歴から削除（git-filter-repo 推奨）
pip install git-filter-repo
git filter-repo --invert-paths `
  --path "whoo+-+your+world_0.140.0_APKPure.xapk" `
  --path work `
  --path jadx-1.5.6.zip `
  --path jadx-gui-1.5.6-win.zip `
  --path jadx-gui-1.5.6-with-jre-win.zip `
  --path build `
  --path whoolib.egg-info `
  --path .pytest_cache

# 3. 強制 push
git remote add origin https://github.com/<user>/<repo>.git
git push --force --all
git push --force --tags
```

- フォークがある場合は、フォーク先の履歴も残ります。**フォークを削除**してください。
- GitHub は SHA 指定で古いコミットを一時的に表示できることがあります。
  完全削除は GitHub Support への依頼が必要です（"remove cached views"）。
- 公開期間があった場合、コピー・Wayback・検索キャッシュは消えません。**公開されたものとして扱う**。

## キーが漏れた場合

- **自分が発行したキー**（自分の Google Cloud キー、自分のトークン）: ただちに revoke / 再発行。
- **whoo のキー**（`AIza…`, Adjust, AppLovin）: 自分では revoke できません。
  公開リポジトリから削除し、必要なら whoo のセキュリティ窓口へ連絡してください。
  キーを自分で使い続けると、Google / Adjust 側の規約違反になります。

## 公開してよい最小構成（案）

```
public/
  whoo_解析レポート.md   # キー・コード断片をマスク済み
  whoo_iocs.csv          # キーをマスク済み
README.md
LICENSE
```

`whoolib` を公開するかは別判断です。公開するなら private 化か読み取り専用化を検討してください。

## リポジトリ監査コマンド

push 済みのリポジトリで、危険なファイル・キーが残っていないか確認できます。

```powershell
# APK / 逆コンパイル / ツール / 生成物が追跡されていないか
git ls-files | Select-String -Pattern '\.(apk|xapk|dex|arsc)$|^work/|^jadx-|^build/|egg-info|pytest_cache'

# キーが履歴に含まれていないか（作業ツリー）
git grep -nE 'AIza[0-9A-Za-z_-]{35}|qpHg9SGpAZaZ8|a6hmmqxcifb4|ca-app-pub-[0-9]+'

# リポジトリサイズ（100MB 超のファイルがあると GitHub に拒否される）
git count-objects -vH

# Releases に APK を添付していないか
gh release list
```

履歴全体を調べる場合は `git log -p --all -S 'AIza' -- .` などを使います。

## 公開前のもう一つの論点：責任ある開示

- 解析結果（特に「PubMatic / InMobi が位置情報を自動取得」という指摘）は、
  公開前に whoo のセキュリティ窓口へ連絡し、修正の猶予を置くことを検討してください。
- レポートには逆コンパイルしたコード断片が含まれます。公開時は**引用の範囲（数行）に留め**、
  全文掲載は避けてください。
- 実際のユーザーデータ・アカウント情報は含めないでください（本レポートには含まれていません）。

## 参考：法的位置づけ（一般論）

- **APK / 逆コンパイル結果の再配布** → 著作権侵害（複製権・公衆送信権）のリスクが高い。
- **API 仕様の公開** → 事実の記述は著作権保護の対象外になり得るが、ToS・営業秘密は別問題。
- **非公式クライアントの公開** → 著作権よりも **契約（ToS）違反** と **悪用リスク** が中心。
- **セキュリティ研究の公表** → 表現の自由として尊重されるが、過度なコード引用・キー公開は避ける。

必要に応じて、公開前に法律の専門家へ確認してください。
