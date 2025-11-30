# 憲法API – 日本国憲法 構造化ライブラリ

これは日本国憲法の全文をJSONで整形し、Flask APIで検索できる自作知識ライブラリです。

## 機能
- /api/law ですべての条文取得
- /api/law?keyword=象徴 のようにキーワード検索も可能

## 構成
- app/law_api_flask.py – FlaskによるAPI実装
- data/legal/constitution.json – 憲法データ（e-Govベース）

## 刑法　2025/11/29追加
- penal_code.json　刑法 （明治四十年法律第四十五号）

## 皇室法令データ（Imperial House Law Series）2025/11/18追加
本リポジトリには、日本の皇室関連法令を JSON 形式で構造化した
皇室法令データセット（LLM最適化版）を収録しています。

**収録法令**
- imperial_house_law_llm.json
皇室典範（昭和22年法律第3号）
- imperial_house_finance_law_llm.json
皇室経済法（昭和22年法律第4号）
- imperial_house_finance_enforcement_law_llm.json
皇室経済法施行法（昭和22年法律第113号）
- imperial_house_special_law_2017_llm.json
皇室典範特例法（平成29年法律第63号）
- imperial_house_council_election_rules_llm.json
皇室会議議員及び予備議員選挙規則（昭和22年政令第164号）
- imperial_house_abdication_enforcement_order_2018_llm.json
天皇の退位等に関する皇室典範特例法施行令（平成30年政令第44号）

**JSON 仕様**
すべての法令データは以下の形式で統一されています。
```json
{
  "meta": {
    "title": "皇室典範",
    "law_id": "昭和22年法律第3号"
  },
  "articles": [
    {
      "article": "第一条",
      "paragraphs": [
        "皇位は、皇統に属する男系の男子が、これを継承する。"
      ]
    }
  ]
}
```

**目的**
- LLM での法令推論
- 自作 API での検索・照会
- サーバー側 RAG の基礎データ
- 国法体系（六法＋関連法）の機械読解用コーパス

## ライセンス
MIT License（自由に使ってOK）

## 出典
法令データ出典元：e-Gov法令データ提供システム（日本政府）


