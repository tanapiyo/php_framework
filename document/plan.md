## 機能
### 必須 / やりたい
- webサーバー（WSGIとか）
- ルーティング(URL分析して関数を呼び出し）
- HTML Template
- DB接続（ORMはSQLAlchemyとか）
- 起動コマンド・デーモン管理

### できれば
- クッキー・セッション
    - クッキーはリクエストオブジェクトやレスポンスオブジェクトから取得・操作
- ログイン認証まわり
- HTTPのメタデータ周りのお世話
- pipのインストール、環境設定（ymlとかini）

## やらない（けどMVCの機能として選択肢にある）
- ローカルデータ
- 非同期処理


## 参考資料
- Python Webフレームワーク比較
https://speakerdeck.com/terapyon/python-webhuremuwakubi-jiao
- Flask
https://a2c.bitbucket.io/flask/
- Bottle
https://bottlepy.org/docs/0.12/
- Bottleのコード
https://github.com/bottlepy/bottle
    - `bottle.py`に全ての実装がある
    - 使い方は`test`を読めばわかる