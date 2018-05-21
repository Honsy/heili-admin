from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # 使用flask_login
    login = LoginManager(app)

    # 注册蓝图
    from app.views import app as view_app
    app.register_blueprint(view_app)
    # 插件注册
    db.init_app(app)

    return app