# タスク管理API（FastAPI）

---

## 1. 概要

本プロジェクトは、FastAPIを用いて作成したシンプルなタスク管理APIです。
ユーザー認証（JWT）を導入し、ログインユーザーごとにタスクを管理できるように設計しています。
バックエンド開発の基礎（CRUD・認証・DB設計）を実践的に学ぶことを目的としています。

---

## 2. 機能

* ユーザー登録
* ログイン（JWT認証）
* タスクの作成・取得・更新・削除（CRUD）
* ログインユーザーごとのタスク管理
* パスワードのハッシュ化（bcrypt）
* ページネーション機能（skip / limit）
* キーワード検索機能
* エラーハンドリング（HTTPException）
* タスクの作成日時・更新日時の管理

---

## 3. 技術スタック

* Python
* FastAPI
* SQLite
* SQLAlchemy
* JWT認証（python-jose）
* passlib（bcrypt）
* Docker / docker-compose

---

## 4. ディレクトリ構成

```
task_api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   └── routers/
│       ├── tasks.py
│       └── users.py
├── data/
│   └── task.db
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 5. API例 

### ログイン

```
POST /users/login
```

#### リクエスト（form形式）

```
POST /users/register
{
  "email": "test@example.com",
  "password": "test123"
}
```

#### レスポンス

```json
{
  "access_token": "xxxxxxxxxxxx"
}
```

---

## 6. API使用例 / メモ一覧取得

### タスク一覧取得

```
GET /tasks?skip=0&limit=10&keyword=買い物
```

#### ヘッダー

```
Authorization: Bearer <アクセストークン>
```

#### レスポンス例

```json
[
  {
    "id": 1,
    "title": "買い物に行く",
    "completed": false,
    "created_at": "2026-03-23T10:00:00",
    "updated_at": "2026-03-23T10:00:00"
  }
]
```

---

## 7. 実行方法

### 環境変数（.env）

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### Dockerで起動

```
docker-compose up --build
```

---

### APIドキュメント

```
http://localhost:8000/docs
```

---

## 8. APIドキュメント画面

FastAPI標準のSwagger UIを利用しており、ブラウザ上でAPIの確認・実行が可能です。
ログイン後、「Authorize」ボタンからJWTトークンを設定することで認証付きAPIを試すことができます。

---

## 9. 工夫した点

* JWT認証を導入し、ユーザーごとのデータ分離を実装
* パスワードをbcryptでハッシュ化し、セキュリティを向上
* CRUD処理を分離（routers / crud）し、可読性と保守性を向上
* エラーハンドリングをHTTPExceptionで統一
* ページネーションと検索機能を実装し、実用性を向上
* Docker環境を構築し、簡単に起動できるようにした

---

## 10. 今後の改善

* パスワードリセット機能の追加
* リフレッシュトークンの実装
* PostgreSQLへの移行
* テストコード（pytest）の追加
* タスクにタグ・期限・優先度の追加
* フロントエンドとの連携

---