# 再生成パイプライン

`whoolib` の `_endpoints.py` / `models.py` / `api.py` / `docs/*.md` は
すべて APK の静的解析結果から生成しています。whoo の新バージョンが出たら
以下の手順で再生成できます。

## 前提

1. APK/XAPK を展開し、base APK を `work/xapk/app.whoo.apk` に置く。
2. jadx でソースを `work/src/sources` に出力する。

```powershell
$env:JADX_CONFIG_DIR="$PWD\work\jadxcfg"
$env:JADX_CACHE_DIR="$PWD\work\jadxcache"
.\work\jadx\bin\jadx.bat -d work\src --no-res --show-bad-code -j 8 work\xapk\app.whoo.apk
```

## 生成

```powershell
python tools/api_inventory.py     # Retrofit インターフェース → work/cache/api_catalog.json
python tools/model_inventory.py   # kotlinx.serialization → work/cache/model_catalog.json
python tools/endpoint_build.py    # パス・verb・パラメータ → work/cache/endpoints.json
python tools/gen_lib.py           # whoolib/_endpoints.py, models.py, docs/MODELS.md
python tools/gen_api.py           # whoolib/api.py, docs/ENDPOINTS.md
```

## 仕組み

- **HTTP メソッド**: Retrofit のアノテーション解析コード（APK 内 `k35.java`）の
  `instanceof` 分岐から確定（`j94`=GET, `j78`=POST, `i78`=PATCH, `d82`=DELETE, `k78`=PUT）。
- **パラメータ**: `@Path` / `@Query` / `@Body` / `@Part` / `@Field` / `@Header` を
  アノテーションクラス（`yb8` / `uz8` / `gp0` / `ob8` / `li3` / `vo4`）から分類。
- **JSON キー**: `kotlinx.serialization` の `PluginGeneratedSerialDescriptor`
  （`al8` + `.j("key", ...)`）から抽出。定数キーは `static final String` を解決。
- **base URL**: Retrofit ビルダー（`p82.java` の `of8.w("...")`）から取得。
  別ホストは `gqa`（Spotify）と `bg4`（Google Routes）のみ。
