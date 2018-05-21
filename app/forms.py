from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired,ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(FlaskForm):
    password = StringField("password" ,validators=[DataRequired()])
    username = StringField("username",validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    # 密码加密
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 相关校验
    def validate_username(self, field):
        if field.data != 'you':
            raise ValidationError('Invalid username')
    def validate_password(self, field):
        if field.data != 'flask':
            raise ValidationError('Invalid password')