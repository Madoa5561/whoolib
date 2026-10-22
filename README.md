# whoolib

`app.whoo` v0.140.0 の APK から再構築した **非公式 Python クライアント**です。
Retrofit インターフェース **213 エンドポイント**、kotlinx.serialization の **399 モデル**を
静的に抽出し、型付きモデルと 1:1 の API メソッドとして提供します。

- エンドポイント全一覧: [`docs/ENDPOINTS.md`](docs/ENDPOINTS.md)
- モデル（JSON キー）一覧: [`docs/MODELS.md`](docs/MODELS.md)
- 生成モデル: `whoolib/models.py`（`MODEL_REGISTRY` で FQCN から引ける）

> **注意**
> 本ライブラリは whoo 運営とは無関係の非公式実装です。
> **自分自身のアカウント**でのみ使用し、whoo の利用規約・プライバシーポリシー・
> 各国の法令（特にストーキング規制法、不正アクセス禁止法、電気通信事業法）を遵守してください。
> 他者の位置情報の追跡、迷惑メッセージの一斉送信、大量アカウント作成、スクレイピングを
> 目的とした使用は禁止します。既定でレート制限（3 req/s）を有効にしています。

---

## インストール

```bash
pip install -e .          # 開発用
# または
pip install whoolib       # 配布した場合
```

依存は `httpx` のみです（Python 3.9+）。

---

## クイックスタート

```python
from whoolib import WhooClient

client = WhooClient()                 # base_url=https://www.wh00.ooo/api/
client.login("me@example.com", "password", adid=None)

me = client.me()
print(me.user["id"], me.user["display_name"])

# 現在位置を送信（アプリと同じ UserLocationRequestDTO）
client.update_location(35.681236, 139.767125, accuracy=8.0, battery_level=0.82)

# 在席状態
client.set_online()
```

### アカウント登録

```python
client.register(
    display_name="tester",
    birthday="1995-04-01",
    username="tester_01",          # whoo ID（@ なし）
    email="me@example.com",
    password="password",
    profile_image="",              # 空文字で可
    referrership_uid=None,
    adid=None,
)
```

### セッションの保存

```python
client.save_session("session.json")        # トークンを平文保存（0600）
client = WhooClient.from_session("session.json")
```

> whoo の API は **refresh token を発行しません**。401 が返ったら再ログインしてください。

---

## 全エンドポイントへのアクセス

`client.api` に 213 メソッドが生成されています。メソッド名は
`<verb>_<path>`（`/`→`_`、`{}` 除去）です。

```python
# GET /api/rooms/{id}/users?page=2&state=active
users = client.api.get_rooms_id_users(7, page=2, state="active")

# POST /api/rooms  (body: {"room": RoomRequestBodyFields})
room = client.api.post_rooms(body={"room": {"name": "tokyo", "add_user_ids": [1, 2]}})

# DELETE /api/friends/{id}
client.api.delete_friends_id(42)
```

### 主要エンドポイント

| 操作 | メソッド |
|---|---|
| ログイン / 登録 | `client.login()` / `client.register()` |
| 自分の情報 | `client.me()`（`GET my`） |
| 位置更新 | `client.update_location()`（`PATCH user/location`） |
| 在席 | `client.set_online()` / `client.set_offline()` |
| 友達一覧 | `client.api.get_friends()` |
| ルーム一覧 / 作成 | `client.api.get_rooms()` / `client.api.post_rooms(body=...)` |
| ルームのメッセージ | `client.api.get_rooms_id_messages(id)` |
| What's Up | `client.api.get_v2_whatsup_video_timeline(...)` ほか |
| チェックイン | `client.api.get_checkins(...)` |
| プレミアム | `client.api.get_whoo_premium_v2_premium_user()` |

全 213 件は [`docs/ENDPOINTS.md`](docs/ENDPOINTS.md) を参照してください。

### 低レベル呼び出し

カタログにない・上書きしたい場合は `call()` / `request()` を使います。

```python
client.call("get_my")                                  # カタログ名で呼ぶ
client.call("post_rooms", body={...}, auth=True)       # auth を明示
client.request("GET", "some/new/endpoint", params=[("page", 1)])
```

### パラメータの渡し方

| 種類 | 引数 | 例 |
|---|---|---|
| Path | 位置引数 | `client.api.get_rooms_id_users(7)` |
| Query | キーワード | `page=2, per=20`、配列は `user_ids=[1,2]` |
| JSON body | `body=` | `body={"name": "x"}` またはモデル |
| multipart | `parts=` | `{"email": "...", "photo": ("a.jpg", b"...", "image/jpeg")}` |
| form | 各フィールド | `client.api.post_validate_email(email="a@b.c")` |
| header | `headers=` | `headers={"X-Goog-Api-Key": "..."}` |

### multipart の主なフィールド（APK の構築コードから抽出）

| エンドポイント | フィールド |
|---|---|
| `POST email/login` | `email`, `password`, `adid` |
| `PATCH user` | `user[<field>]`（例: `user[display_name]`, `user[introduction]`, `user[watch_logs][][user_id]`） |
| `POST friends` | `user_id`, `is_in_japan`（または `user[friend_ids]`, `user[is_in_japan]`） |
| `POST rooms/{id}/messages` | `message[uid]`, `message[body]`, `message[media][]`, `message[stamp_id]`, `message[reply_original_message_id]`, `message[room_ids][]` |
| `POST stamp_messages` | `message[stamp_id]`, `message[stamp_count]`, `message[user_id]` |
| `PATCH user_spot` 系 | `user_spot[spot_type]` |

> multipart は `parts={...}` にそのまま渡せます（値は `str` / `bytes` / `(filename, bytes, content_type)`）。
> フィールド名はエンドポイントごとに上記の規則に従います。

### モデル

```python
from whoolib.models import MODEL_BY_NAME

UserAccount = MODEL_BY_NAME["UserAccount"]
acc = UserAccount(display_name="n", email="e", password="p")
acc.to_dict()      # {'display_name': 'n', 'email': 'e', 'password': 'p'}
```

`MODEL_REGISTRY` は FQCN（`app.whoo.data.api.request.UserAccount`）からクラスを引けます。
ネストしたオブジェクトは `dict` のまま保持されます（必要な場合は手動で変換）。

---

## エラー

```python
from whoolib import (
    AuthenticationError, ValidationError, NotFoundError,
    PermissionDeniedError, RateLimitError, ServerError, NetworkError,
)

try:
    client.api.get_rooms_id_users(1)
except AuthenticationError:
    client.login(...)
except ValidationError as e:
    print(e.code, e.errors, e.status_code)
except RateLimitError as e:
    print(e.retry_after)
```

| 例外 | HTTP | 意味 |
|---|---|---|
| `ValidationError` | 400 / 422 | 入力エラー（`error_code`, `errors`） |
| `AuthenticationError` | 401 | トークン欠落・期限切れ・認証失敗 |
| `PermissionDeniedError` | 403 | 権限なし |
| `NotFoundError` | 404 | 存在しない／非公開 |
| `RateLimitError` | 429 | レート制限（`retry_after`） |
| `ServerError` | 5xx | サーバー障害 |
| `NetworkError` | - | DNS/TLS/タイムアウト |

---

## 実装メモ（解析結果）

| 項目 | 値 |
|---|---|
| base URL | `https://www.wh00.ooo/api/` |
| 認証 | `Authorization: Bearer <access_token>` |
| User-Agent | `app.whoo/0.140.0 Android/<ver>/<model>`（既定 `.../14/generic`） |
| Accept-Language | `ja`（変更可） |
| ログイン | `POST email/login`、**multipart/form-data**（`email`, `password`, `adid`） |
| 登録 | `POST email/users`、JSON（`display_name`, `profile_image`, `birthday`, `username`, `email`, `password`, `referrership_uid`, `adid`） |
| トークン | レスポンス `UserResponse.access_token`、リフレッシュなし |
| 位置更新 | `PATCH user/location`、`UserLocationRequestDTO`（緯度経度・速度・精度・バッテリー・前面/背面・spot） |
| サポート | `support/*` のみ `X-Whoo-Support-Device-Token: <UUID>` |
| レート制限 | 既定 3 req/s（トークンバケット） |
| リトライ | GET/PUT/DELETE の 429/5xx、指数バックオフ |

### 別ホストのエンドポイント

APK 内には whoo 以外の Retrofit インスタンスも含まれます。カタログでは
エンドポイント単位で base URL を上書きしています。

| interface | base URL | 例 |
|---|---|---|
| `gqa` | `https://open.spotify.com/` | `GET api/token`（Cookie ヘッダが必要） |
| `bg4` | `https://routes.googleapis.com/` | `GET directions/v2:computeRoutes`（`X-Goog-Api-Key` / `X-Goog-FieldMask`） |

### HTTP メソッドの対応（確定）

APK 内の Retrofit アノテーションは R8 で難読化されていますが、Retrofit 本体の
アノテーション解析コード（`k35.java`）に各クラス→HTTP メソッドの分岐が残っていたため、
以下は**推定ではなく確定**です。

| 難読化名 | HTTP |
|---|---|
| `@j94` | GET |
| `@co4` | HEAD |
| `@j78` | POST |
| `@k78` | PUT |
| `@i78` | PATCH |
| `@d82` | DELETE |
| `@nz7` | OPTIONS |

> サーバー側のバージョン差異で 405 が返る場合は `client.request()` で上書きできます。
> 同じパス・動詞の重複定義には `_2` サフィックスを付けています
> （例: `patch_rooms_id`, `patch_rooms_id_2`）。

---

## 制約

- **動的検証は未実施**です。実機での通信キャプチャによる最終確認は行っていません。
- `birthday` の書式・`profile_image` の形式など、サーバー側のバリデーションは未検証です。
- レスポンスのネスト構造は `dict` のまま返ります（モデル変換はトップレベルのみ）。
- 401 時の自動再ログインは行いません（資格情報を保持しない設計）。
- whoo 側の仕様変更により予告なく動作しなくなる可能性があります。

---

## テスト

```bash
pytest -q
```

`httpx.MockTransport` によるオフラインテスト（15 件）:
ログインの multipart、登録 JSON、認証ヘッダ、パス/クエリ展開（配列含む）、
位置情報 payload、base URL 上書き、エラーマッピング、モデル変換、セッション保存。

---

## ファイル構成

```
whoolib/
  __init__.py        # 公開API
  client.py          # HTTPコア（認証・ヘッダ・リトライ・レート制限）
  api.py             # 213 メソッド（生成）
  _endpoints.py      # エンドポイントカタログ（生成）
  models.py          # 399 モデル（生成）
  exceptions.py
  py.typed
docs/
  ENDPOINTS.md       # 全エンドポイント一覧
  MODELS.md          # 全モデルと JSON キー
  REGENERATE.md      # 再生成パイプライン
tools/               # 生成スクリプト（APK 解析 → コード生成）
tests/
  test_whoolib.py
```

---

## ライセンス / 免責

MIT。本ソフトウェアは「現状のまま」提供され、利用によって生じた
アカウント停止・法的責任を含む一切の結果について作者は責任を負いません。
