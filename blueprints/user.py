import random
import string

from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from forms import LoginFrom, RegisterForm, EmailCaptchaModel
from models import User
from exts import db, mail
from flask_mail import Message
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("User", __name__, url_prefix="/user")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')


@bp.route("/register_form", methods=['POST'])
def register_check():
    register_form = RegisterForm(request.form)

    if register_form.validate():
        check_register = User.query.filter_by(user_email=register_form.user_email.data).first()
        if check_register:
            hash_password = generate_password_hash(register_form.user_password.data)
            user = User(user_email=register_form.user_email.data, user_name=register_form.user_name.data,
                        user_password=hash_password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('User.login')), jsonify({"message": "Sign up successfully!"})
        else:
            return jsonify({"message": "Mailbox has been registered!"})
    else:
        return redirect(url_for('User.login'))


@bp.route("/login_form", methods=['POST'])
def login_check():
    login_form = LoginFrom(request.form)
    if login_form.validate():
        user_email = login_form.user_email.data
        user_password = login_form.user_password.data
        user = User.query.filter_by(user_email=user_email).first()
        if user and check_password_hash(user.user_password, user_password):
            return redirect('/')
        else:
            flash("Incorrect email or password.")
            return redirect(url_for("User.login"))
    else:
        flash("Incorrect email or password format.")
        return redirect(url_for("User.login"))


@bp.route("/captcha", methods=['POST'])
def my_mail():
    email = request.form.get("email")
    if email:
        letters = string.ascii_letters + string.digits
        captcha = "".join(random.sample(letters, 6))
        message = Message(
            subject="Cyan Pine 验证码",
            recipients=[email],
            html=render_template("email.html", email_captcha=captcha)
        )
        mail.send(message)
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if captcha_model:
            captcha_model.captcha = captcha
            captcha_model.create_time = datetime.now
            db.session.commit()
        else:
            captcha_model = EmailCaptchaModel(email=email, captcha=captcha)
            db.session.add(captcha_model)
            db.session.commit()
        print("captcha", captcha)
        # code:200,成功的，正常的请求
        return jsonify({"code": 200})
    else:
        # code:400,客户端错误
        return jsonify({"code": 400, "message": "请先传递邮箱！"})
