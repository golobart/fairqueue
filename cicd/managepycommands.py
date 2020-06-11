python manage.py --version
python manage.py --help

python -Wa manage.py test
python manage.py check --deploy

python manage.py runserver

python manage.py dbshell
python manage.py shell

python manage.py makemessages - l 'ca'
python manage.py makemessages - l 'en_US'
python manage.py makemessages - l 'zh_CN'
python manage.py makemessages - l 'es'
python manage.py compilemessages

python manage.py makemigrations
python manage.py showmigrations
python manage.py sqlmigrate
python manage.py sqlmigrate adminapp
python manage.py sqlmigrate adminapp 0005_auto_20200522_1526
python manage.py migrate

python manage.py dumpdata --exclude contenttypes --exclude auth.permission --indent 2 > fixtures/alldbdata.json
python manage.py loaddata alldbdata.json
