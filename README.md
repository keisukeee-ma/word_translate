# word_translate - ネーミング辞書

日本語を英語・スペイン語・ポルトガル語・ドイツ語・フランス語に一括翻訳するDjangoアプリ。

## セットアップ手順

```bash
# 1. 仮想環境を作成
python3 -m venv venv
source venv/bin/activate  # Macの場合
# venv\Scripts\activate  # Windowsの場合

# 2. パッケージをインストール
pip install django==4.2 googletrans==4.0.0rc1 django-widget-tweaks whitenoise python-decouple dj-database-url setuptools

# 3. DBを初期化
python manage.py migrate

# 4. サーバー起動
python manage.py runserver
```

## アクセス
ブラウザで http://127.0.0.1:8000/ を開く

## 注意
- `config/local_settings.py` がローカル開発用の設定ファイルです
- Django 4.2 + Python 3.10以上で動作確認済み
