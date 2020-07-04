#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd fairqueue; python manage.py createsuperuser --no-input)
fi

# These env var only exists in the docker-compose and openshift, so we asume mysql db
echo "FAIRQ_COMPOSE = $FAIRQ_COMPOSE"
echo "FAIRQ_OPENSHIFT = $FAIRQ_OPENSHIFT"
if [ "$FAIRQ_COMPOSE" == "yes" ]; then
  # Wait mysql fairq_database to exists
  echo "Check if database exists"
  if [ "$FAIRQ_OPENSHIFT" == "yes" ]; then
    DB_MYSQL_CONN = "srvdbfairq" # Openshift service
  else
    DB_MYSQL_CONN = "cicd_fairq-db_1" # Docker host
  fi
  testconn=`python fairqueue/cicd/pytestconn.py $DB_MYSQL_CONN`
  while [[ ! -z "`echo $testconn`" ]]
#  while [[  -z "`mysql --defaults-extra-file=mysql_extra_config.cnf -h cicd_fairq-db_1 -qfsNBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='fairq_database'" 2>&1`" ]]
#  while [[  -z "`mysql -h cicd_fairq-db_1 -u fairq_user -pfairq_pwd -Dfairq_database -qfsNBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='fairq_database'" 2>&1`" ]]
  do
    echo "WAITING FOR DATABASE fairq_database TO EXIST...."
    sleep 3s
    testconn=`python fairqueue/cicd/pytestconn.py $DB_MYSQL_CONN`
  done

# check if tables exist or create them
  echo "Check if tables exist"
  testtable=`python fairqueue/cicd/pytesttable.py $DB_MYSQL_CONN`
  if [[ ! $testtable =~ "adminapp_calendar" ]]; then
#  if [[ ! -z  "`mysql --defaults-extra-file=mysql_extra_config.cnf -h cicd_fairq-db_1 -qfsNBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='fairq_database' AND TABLE_NAME='adminapp_calendar'" 2>&1`" ]]; then
#  if [[ ! -z  "`mysql -h cicd_fairq-db_1 -u fairq_user -pfairq_pwd -Dfairq_database -qfsNBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='fairq_database' AND TABLE_NAME='adminapp_calendar'" 2>&1`" ]]; then
    echo "adminapp_calendar table does not exist, making migrations...."
    (cd fairqueue; python manage.py makemigrations; python manage.py migrate;
    python manage.py loaddata fixtures/alldbdata.json)
  fi
  echo "Point settings.py to mysql"
  sed -i "s/DATABASES = {/XDATABASESX = {/g" fairqueue/fairqueue/settings.py
  sed -i "s/XXXDATABASESXXX = {/DATABASES = {/g" fairqueue/fairqueue/settings.py
  if [ "$FAIRQ_OPENSHIFT" == "yes" ]; then # also point to openshift service, not to docker host
    sed -i "s/cicd_fairq-db_1/srvdbfairq/g" fairqueue/fairqueue/settings.py
  fi
else
# for sqlite always create schema
  echo "sqlite3 tables never exist, making migrations...."
  (cd fairqueue; python manage.py makemigrations; python manage.py migrate;
  python manage.py loaddata fixtures/alldbdata.json)
fi
echo "Installing gettext, messages and runserver"
(cd fairqueue;
apt-get update; apt-get install -y gettext;
apt-get install -y python-dev default-libmysqlclient-dev;
apt-get install -y python3-dev;
python manage.py compilemessages;
python manage.py runserver 0.0.0.0:8000)
#(. ./django_queue_venv/bin/activate; cd fairqueue; python manage.py runserver)
