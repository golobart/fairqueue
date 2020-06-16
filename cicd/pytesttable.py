from MySQLdb import _mysql
try:
    db=_mysql.connect(host="cicd_fairq-db_1",user="root",passwd="password",db="fairq_database")
    db.query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='fairq_database' AND TABLE_NAME='adminapp_calendar'")
    r=db.use_result()
    print(r.fetch_row())
    db.close()
except:
    print('databse test table error')