import random
import string

from flask import Blueprint,request,render_template,redirect,url_for,flash,jsonify
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

@bp.route("/register_form", methods=['POST'])
def register_check():
    register_form = RegisterForm(request.form)

    if register_form.validate():
        hash_password = generate_password_hash(register_form.user_password.data)
        user = User(user_email=register_form.user_email.data, user_name=register_form.user_name.data, user_password=hash_password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('User.login'))
    else:
        return redirect(url_for('User.login'))


@bp.route("/login_form",methods=['POST'])
def login_check():
    login_form = LoginFrom(request.form)
    if login_form.validate():
        user_email = login_form.user_email.data
        user_password = login_form.user_password.data
        user = User.query.filter_by(user_email=user_email).first()
        if user and check_password_hash(user.user_password, user_password):
            return redirect('/')
        else:
            flash("邮箱或密码错误")
            return redirect(url_for("User.login"))
    else:
        flash("邮箱或密码格式错误")
        return redirect(url_for("User.login"))

@bp.route("/captcha",methods=['POST'])
def my_mail():
    email = request.form.get("email")
    if email:
        letters = string.ascii_letters + string.digits
        captcha = "".join(random.sample(letters, 6))
        message = Message(
            subject="Cyan Pine 验证码",
            recipients=[email],

            body=f"同学您好，\n\n您正在CyanPine进行注册验证，\n\n验证码有效期1分钟，请尽快完成注册。\n\n您的验证码为：\n\n {captcha} \n\n请勿将此验证码转发给任何人。\n\n若非本人操作，请忽略此邮件。"
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
        print("captcha",captcha)
        #code:200,成功的，正常的请求
        return jsonify({"code":200})
    else:
        #code:400,客户端错误
        return jsonify({"code":400,"message":"请先传递邮箱！"})


