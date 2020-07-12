import sys
from MySQLdb import _mysql
try:
    db=_mysql.connect(host=sys.argv[1], user="root", passwd="password", db="fairq_database")
except:
    print('db connection error')

