# 憲法API – 日本国憲法 構造化ライブラリ

これは日本国憲法の全文をJSONで整形し、Flask APIで検索できる自作知識ライブラリです。

## 機能
- /api/law ですべての条文取得
- /api/law?keyword=象徴 のようにキーワード検索も可能

## 構成
- app/law_api_flask.py – FlaskによるAPI実装
- data/legal/constitution.json – 憲法データ（e-Govベース）

## ライセンス
MIT License（自由に使ってOK）

## 出典
法令データ出典元：e-Gov法令データ提供システム（日本政府）


