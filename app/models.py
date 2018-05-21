from app import db
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(16), index = True, unique = True)


    # def __repr__(self):
    #     return '<User %r>' % (self.nickname)
    # # 这个方法应该只返回 True，除非表示用户的对象因为某些原因不允许被认证。
    # @property
    # def is_authenticated(self):
    #     return True
    # # 除非是用户是无效的，比如因为他们的账号是被禁止。
    # @property
    # def is_active(self):
    #     return True
    # # 如果是匿名的用户不允许登录系统。
    # @property
    # def is_anonymous(self):
    #     return False
    #
    # # 以 unicode 格式。我们使用数据库生成的唯一的 id
    # def get_id(self):
    #     try:
    #         return unicode(self.id)  # python 2
    #     except NameError:
    #         return str(self.id)  # python 3