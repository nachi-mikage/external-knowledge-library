from flask import Flask, request, jsonify, Response
import json
import os
import re

app = Flask(__name__)

# ファイルパス（環境に応じて変更）
CONSTITUTION_PATH = "/mnt/obsidian/external_lib/legal_db/constitution.json"

# JSONロード関数
def load_constitution():
    print(f">>> 読み込み中: {CONSTITUTION_PATH}")
    if not os.path.exists(CONSTITUTION_PATH):
        print(">>> ファイルが存在しません！")
        return []
    with open(CONSTITUTION_PATH, "r", encoding="utf-8") as f:
        raw = f.read()
        cleaned = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', raw)
        return json.loads(cleaned)

# APIルート：法検索
@app.route("/api/law")
def search_law():
    keyword = request.args.get("keyword", "").strip()
    if not keyword:
        return Response(json.dumps({"error": "keyword is required"}, ensure_ascii=False), mimetype="application/json")
    data = load_constitution()
    results = [
        entry for entry in data
        if keyword in entry.get("title", "") or keyword in entry.get("text", "")
    ]
    return Response(json.dumps(results, ensure_ascii=False), mimetype="application/json")

# 実行時にサーバーを起動
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

