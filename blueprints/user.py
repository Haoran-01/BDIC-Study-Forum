from flask import Blueprint,request,render_template
from forms import LoginFrom, RegisterForm
from models import User
from exts import db, mail
from flask_mail import Message

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
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(user_email=form.user_email.data, user_name=form.user_name.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return "注册成功"
    else:
        return render_template('register.html')

@bp.route("/mail")
def my_mail():
    message = Message(
        subject="Cyan Pine 验证码",
        recipients=['2334201198@qq.com'],
        body="同学您好，/n您正在CyanPine进行注册验证，验证码有效期1分钟，请尽快完成注册"

    )
    mail.send(message)
    return "success"



