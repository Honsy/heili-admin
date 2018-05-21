
from flask import render_template,Blueprint,flash,redirect
from .forms import LoginForm

app = Blueprint('app',__name__)




# 后台管理使用
@app.route('/')
@app.route('/index') #
def index():
    user = { 'nickname': 'Honsy' } # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Username and password are correct')
        return redirect('/technology')
    return render_template('login.html',
        title = 'Sign In',
        form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('register.html',
        title = 'Sign In',
        form = form)

@app.route('/main', methods = ['GET', 'POST'])
def main():
    return render_template('Backstage/main.html')

@app.route('/technology', methods = ['GET', 'POST'])
def technology():
    return render_template('Backstage/technology.html')

# 前端展示使用
@app.route('/api/v1/index', methods = ['GET'])
def apiIndex():
    return 'ssss'