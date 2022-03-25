import random
import string

from flask import Blueprint,request,render_template
from forms import LoginFrom,RegistForm
from models import User
from exts import db, mail
from flask_mail import Message
from models import EmailCaptchaModel

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

@bp.route("/captcha")
def get_captcha():
    email = request.args.get("email")
    letters = string.ascii_letters + string.digits
    captcha = "".join(random.sample(letters, 6))
    if email:
        message = Message(
            subject="Cyan Pine 验证码",
            recipients=[email],
            body=f"同学您好，您正在CyanPine进行注册验证，验证码有效期1分钟，请尽快完成注册。您的验证码是：{captcha}，请勿经此验证码发送给任何人。若非本人操作请忽略此邮件。"
        )
        mail.send(message)
        return "success"
    else:
        return "no email"



