#!flask/bin/python
from migrate.versioning import api
from app.config import SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO
from app import db
from app.run import app
import os.path

with app.app_context():  # 使用这个 db  一定要在flask 的上下文使用才可以   关键字 “flask上下文” 自己去百度 嗯嗯
    db.create_all()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))

        # 项目已经弄好了 自己折腾吧 谢谢