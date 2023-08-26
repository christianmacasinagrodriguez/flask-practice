from flask import Flask, render_template, request
from  flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ANY KEY YOU WANT AS LONG AS IT IS A STRING'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app) 

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    #from .store import store
    from .auth import auth
    from .application import application
    from .views import views
    
    
    #app.register_blueprint(store, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 
    app.register_blueprint(application, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
   
    
    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')