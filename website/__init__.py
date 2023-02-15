from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
import mysql.connector
from flask_mail import Mail
from os import path
from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"

app = Flask(__name__)

def create_app():
    
    app.secret_key = 'ticket selling site'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'crud'

    
    mydb =mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud"
    )

    mycursor = mydb.cursor()
#email section

# def mailing():


#     app.config['DEBUG'] = True
#     app.config['TESTING'] = False
#     app.config['app_SERVER'] = 'localhost'
#     app.config['app_PORT'] = 25
#     app.config['app_USE_TLS'] = False 
#     app.config['app_USE_SSL'] = False 
#     app.config['app_DEBUG'] = True
#     app.config['app_USERNAME'] = 'ticketme'
#     app.config['app_PASSWORD'] = ''
#     app.config['app_DEFAULT_SENDER'] = None
#     app.config['app_MAX_EappS'] = 5
#     app.config['app_SUPRESS_SEND'] = False
#     app.config['app_ASCII_ATTACHMENTS'] = False


#     mail = Mail(app)




    # db.init_app(app)

    from .views import views
    from .auth import auth
    from .backend import backend

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(backend, url_prefix='/admin')

    # from .models import User, Note
    
    # with app.app_context():
    #     db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    user = mycursor.execute("SELECT * FROM accounts")
    
    @login_manager.user_loader
    def load_user(id):
        return user(int(id))

    return app


# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
