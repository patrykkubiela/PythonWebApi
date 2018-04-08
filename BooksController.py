import flask
import MySQLdb
import DatabaseContext

class BooksController:

    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    

    @app.route('/', methods=['GET'])
    def Get():
        context = DatabaseContext.DatabaseContext("192.168.1.3", "root", "!FXp@ss8", "BooksCollection")
        context.RunQuery("SELECT * FROM Books")
        result = ""

        for row in context.result:
            result += row

        return result
    
    app.run()