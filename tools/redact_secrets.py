"""Create redacted copies of the analysis report / IOC list for publication.

Usage:  python tools/redact_secrets.py
Output: public/whoo_解析レポート.md, public/whoo_iocs.csv, public/README.md
"""

from __future__ import annotations

import os
import re

PATTERNS = [
    (re.compile(r"AIza[0-9A-Za-z_\-]{35}"), "AIza…<REDACTED>"),
    (re.compile(r"qpHg9SGpAZaZ8[A-Za-z0-9_\-]+"), "qpHg…<REDACTED>"),
    (re.compile(r"\ba6hmmqxcifb4\b"), "a6hm…<REDACTED>"),
    (re.compile(r"ca-app-pub-\d+~\d+"), "ca-app-pub-…~<REDACTED>"),
    (re.compile(r"\b35cbc4a309d163a2\b"), "35cb…<REDACTED>"),
]

FILES = [
    "whoo_解析レポート.md",
    "whoo_iocs.csv",
]

PUBLIC_README = """# whoo 0.140.0 静的解析（公開用）

このリポジトリには、whoo (app.whoo) 0.140.0 の静的解析結果のうち
**公開可能な部分のみ**を置いています。

- `whoo_解析レポート.md` — 解析レポート（API キー・SDK キーは伏字化済み）
- `whoo_iocs.csv` — 通信先・識別子の IOC 一覧（キーは伏字化済み）

以下は**含まれていません**（著作権・セキュリティ上の理由）。

- APK / XAPK 本体
- 逆コンパイルしたソースコード
- API キー・SDK キー・トークンの実値
- 非公式 API クライアントの実装

## 注意

本解析は非公式のものであり、whoo 運営とは無関係です。
内容の正確性は保証しません。引用・参照の際は自己責任でお願いします。
"""


def main() -> None:
    os.makedirs("public", exist_ok=True)
    for name in FILES:
        if not os.path.exists(name):
            continue
        text = open(name, encoding="utf-8").read()
        total = 0
        for rx, repl in PATTERNS:
            text, n = rx.subn(repl, text)
            total += n
        out = os.path.join("public", os.path.basename(name))
        open(out, "w", encoding="utf-8").write(text)
        print(f"{name} -> {out}  ({total} replacements)")
    open("public/README.md", "w", encoding="utf-8").write(PUBLIC_README)
    print("public/README.md written")


if __name__ == "__main__":
    main()
