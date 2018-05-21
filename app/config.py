import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_TRACK_MODIFICATIONS = True
# 配置Sqlite数据库
basedir = os.path.abspath(os.path.dirname(__file__))
# 数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLAlchemy-migrate 数据文件存储
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')