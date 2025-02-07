from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'THIS IS A SECRET KEY. DO NOT SHARE. PLEASE CHANGE.'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # LoginManager is needed for our application 
    # to be able to log in and out users
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # pass
        # # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # link db with the app
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .install import install
    from .services import services
    from .users import users
    from .appointments import appointments

# to put a prefix (in this case non prefix) to every route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(install, url_prefix='/')
    app.register_blueprint(services, url_prefix='/')
    app.register_blueprint(users, url_prefix='/')
    app.register_blueprint(appointments, url_prefix='/')




    # incluir las demas tablas ademas de Admin
    from .models import Admin, User, Appointment, Service

    create_database(app)


    return app


def create_database(app):
    # check if the db is already create.
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Entra al contexto de la aplicación
            db.create_all()
            print("Created Database!!")



