import MySQLdb

class DatabaseContext:

    result = []    

    def __init__(self, host, user, password, dbname):
        db = MySQLdb.connect(host=host,user=user,passwd=password,db=dbname)        
        cur = db.cursor()

    def RunQuery(query):
        self.cur.execute(query)
        self.result = self.cur.fetchall()

    def CloseConnection():
        db.close()
