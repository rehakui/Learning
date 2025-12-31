Minimal Todo App (Flask)
======

## 概要
Flask と SQLAlchemy の基礎理解を目的として作成した、
最小構成の Todo 管理アプリです。

Webアプリの基本である
「リクエスト → 処理 → レスポンス」
「DBへの保存と取得」
の流れを理解することを重視しました。


## 学習目的
- Flask によるルーティングとリクエスト処理の理解
- SQLAlchemy を使った最小限の CRUD 操作の理解
- DB / Python オブジェクトの関係の整理


## 使用技術
Python 3
Flask
Flask-SQLAlchemy
SQLite


## 機能一覧
Todo の作成（POST）
Todo の一覧取得（GET）
Todo の削除（POST）

※ あえて 更新機能や認証機能は実装していません


## API エンドポイント
| メソッド | URL | 内容 |
|--------|-----|-----|
| GET | /todos | 一覧取得 |
| POST | /todos | 作成 |
| POST | /todos/delete/<id> | 削除 |


## セットアップ方法
git clone https://github.com/rehakui/Learning.git
cd Learning

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py


## 使い方（動作確認）
ブラウザで http://127.0.0.1:5000 にアクセス
フォームから Todo を追加できます


## 工夫した点
- title が空の場合は登録できないようにバリデーションを実装
- JSON と DB の違いを理解するため、SQLAlchemy を使用
- 学習目的のため、Blueprint や factory パターンは使用せず単一ファイル構成にしました
- jinja2テンプレートのreindexを使用して、リストを表示
（直近のものを優先順位高くするために数字を降順にして目に入る数字を大きくするようにした）


## 今後の改善予定
更新（PUT / PATCH）の追加
Blueprint を使ったファイル分割
HTML + フォームによる操作画面の追加


## 学んだこと
- `.all()` はデータそのものではなく、モデルのオブジェクトのリストを返すこと
- `db.session.add()` だけでは保存されず、`commit()` で確定されること
- GET と POST を用途ごとに分けることで、処理の意味が明確になること
- リクエスト → 処理 → レスポンス の流れを、実装を通して理解できた


## 作者
Ryota