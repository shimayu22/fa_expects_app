# これは何？
Djangoアドベントカレンダー2019で書いた記事用のリポジトリ。
ご自由にお試しください。


# お試し用

- part1：https://github.com/shimayu22/fa_expects_app/releases/tag/part1
  - 外部キー絞り込み無し
- part2：https://github.com/shimayu22/fa_expects_app/releases/tag/part2
  - 外部キー絞り込み有り（べた書き）
- part3：https://github.com/shimayu22/fa_expects_app/releases/tag/part3
  - 外部キー絞り込み有り（関数で作成）


# 環境
- Python 3.7.1
- Django 2.2.6


# 初期設定

### Win版
    python -m venv env
    env\Sctipts\activate
    pip install django==2.2.6
    manage.py migrate
    manage.py createsuperuser
    manage.py loaddata db.json
    manage.py runserver

### Mac版
    python3 -m venv env
    source env\bin\activate
    pip install django==2.2.6
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py loaddata db.json
    python manage.py runserver
  
# 使い方
- runserver後に、ブラウザで http://127.0.0.1/admin を開く
- createsuperuserで登録したID/PWでログインする
- [選手情報]にデータがロードされていることを確認する


## part2の場合
- [FA予想] - [FA予想を追加]をクリックし、「選手」がlimit_choices_toで指定した通り表示されるか確認する
- Models.pyのFaExpectsのplayer_idのlimit_choices_toを変更して、指定した通り表示されるか確認する


## part3の場合
- [要望] - [要望の追加]をクリックし、条件を色々変更してみる
- [FA予想] - [FA予想を追加]をクリックし、「選手」が[要望]通りに表示されているか確認する
