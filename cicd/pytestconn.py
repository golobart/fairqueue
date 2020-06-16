from MySQLdb import _mysql
try:
    db=_mysql.connect(host="cicd_fairq-db_1",user="root",passwd="password",db="fairq_database")
except:
    print('db connection error')

