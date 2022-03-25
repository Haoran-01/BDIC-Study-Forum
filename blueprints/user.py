from flask import Blueprint,request,render_template
from forms import LoginFrom,RegistForm
from models import User
from exts import db

bp = Blueprint("User",__name__,url_prefix="/user")

@bp.route("/login", methods=['GET','POST'])
def login():
    form = LoginFrom(request.form)
    if request.method == 'POST' and form.validate():
        return "登录成功"
    else:
        return render_template('login.html')

@bp.route("/register", methods=['GET','POST'])
def register():
    form = RegistForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(user_email=form.user_email.data, user_name=form.user_name.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return "注册成功"
    else:
        return render_template('register.html')


