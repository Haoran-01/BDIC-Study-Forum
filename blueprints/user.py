import random
import string

from flask import Blueprint,request,render_template,redirect,url_for
from forms import LoginFrom, RegisterForm, EmailCaptchaModel
from models import User
from exts import db, mail
from flask_mail import Message
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

bp = Blueprint("User",__name__,url_prefix="/user")

@bp.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginFrom(request.form)
        if form.validate():
            return "登录成功"
        else:
            return render_template("login.html")


@bp.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            hash_password = generate_password_hash(form.user_password.data)
            user = User(user_email=form.user_email.data, user_name=form.user_name.data, user_password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('User.login'))
        else:
            return redirect(url_for('User.register'))

@bp.route("/captcha")
def my_mail():
    email = request.args.get("email")
    if email:
        letters = string.ascii_letters + string.digits
        captcha = "".join(random.sample(letters, 6))
        message = Message(
            subject="Cyan Pine 验证码",
            recipients=[email],
            body=f"同学您好，您正在CyanPine进行注册验证，验证码有效期1分钟，请尽快完成注册。您的验证码为：{captcha}  请勿将此验证码转发给任何人。若非本人操作，请忽略此邮件。"
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha =captcha)
            db.session.add(captcha_model)
            db.session.commit()
        return "success"
    else:
        return "no email"



