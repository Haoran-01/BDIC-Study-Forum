from flask import Blueprint,request,render_template,redirect,url_for
from forms import LoginFrom,RegisterForm
from models import User
from exts import db, mail
from flask_mail import Message

bp = Blueprint("User",__name__,url_prefix="/user")


# 登录界面
@bp.route("/login", methods=['GET','POST'])
def login():
    form = LoginFrom(request.form)
    if request.method == 'POST' and form.validate():

        return "登录成功"
    else:
        return render_template('login.html')

# 注册界面
@bp.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            user = User(user_email=form.user_email.data, user_name=form.user_name.data,
                        user_password=form.user_password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("User.login"))
        else:
            return redirect(url_for("User.register"))
# 发送邮件
@bp.route("/mail")
def my_mail():
    message = Message(
        subject="Cyan Pine 验证码",
        recipients=['2334201198@qq.com'],
        body="同学您好，/n您正在CyanPine进行注册验证，验证码有效期1分钟，请尽快完成注册"

    )
    mail.send(message)
    return "success"



