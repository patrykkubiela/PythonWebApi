import flask
import MySQLdb
import DatabaseContext

class BooksController:

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    

    @app.route('/', methods=['GET'])
    def Get():
        context = DatabaseContext.DatabaseContext("192.168.1.3", "root", "", "BooksCollection")
        numrows = context.RunQuery("SELECT * FROM Books")
        result = "ss"
        
        for row in context.result:
            result += str(row[1])

        return result
    
    app.run()