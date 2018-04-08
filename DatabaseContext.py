import MySQLdb

class DatabaseContext:

    result = []
    
    def __init__(self, host, user, password, dbname):
        self.db = MySQLdb.connect(host,user,password,dbname)        
        self.cursor = self.db.cursor()

    def RunQuery(self, query):
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()

    def CloseConnection():
        db.close()
