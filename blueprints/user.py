import random
import string

import wtforms
from flask import Blueprint,request,render_template,redirect,url_for,flash,session
from forms import LoginFrom, RegisterForm, EmailCaptchaModel,ForgetFormEmail,ForgetFormPassword
from flask_login import login_user,logout_user,login_required
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

# 用户登出


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out successfully!"

# 注册功能


@bp.route("/register_form", methods=['POST','GET'])
def register_check():
    register_form = RegisterForm(request.form)

    if register_form.validate():
        check_register = User.query.filter_by(user_email = register_form.user_email.data).first()
    #     if check_register:
    #         hash_password = generate_password_hash(register_form.user_password.data)
    #         user = User(user_email=register_form.user_email.data, user_name=register_form.user_name.data,
    #                     user_password=hash_password)
    #         db.session.add(user)
    #         db.session.commit()
    #         # return redirect(url_for('User.login'))
    #         return {"code": 200, "message": "Sign up successfully!"}
    #     else:
    #         # return redirect(url_for('User.login'))
    #         return {"code": 400, "message": "Mailbox has been registered!"}

        hash_password = generate_password_hash(register_form.user_password.data)
        user = User()
        user.user_email = register_form.user_email.data
        user.user_name = register_form.user_name.data
        user.user_password = register_form.user_password
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('User.login'))
    else:
        return redirect(url_for('User.login'))

# 登录功能


@bp.route("/login_form", methods=['POST'])
def login_check():
    login_form = LoginFrom(request.form)
    if login_form.validate():
        user_email = login_form.user_email.data
        user_password = login_form.user_password.data
        user = User.query.filter_by(user_email=user_email).first()
        if user and check_password_hash(user.user_password, user_password):
            # response = redirect("/")
            # response.set_cookie("user_email",user_email)
            # session["user_email"] = user_email
            # session['logged_in'] = True

            # 通过flask-login登录
            login_user(user)
            return redirect('/')
        else:
            flash("Incorrect email or password.")
            return redirect(url_for("User.login"))
    else:
        flash("Incorrect email or password format.")
        return redirect(url_for("User.login"))


@bp.route("/captcha",methods=['POST','GET'])
def my_mail():
    data = request.get_json(silent=True)
    email = data["email"]
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
        return {'code':200}
    else:
        # code:400,客户端错误
        return {"code": 400, "message": "请先传递邮箱！"}


@bp.route("/forget_form_email", methods=['POST','GET'])
def email_check():
    data = request.get_json(silent=True)
    email = data["email"]
    captcha = data["captcha"]
    email_model = EmailCaptchaModel.query.filter_by(email = email).first()
    captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
    if email_model:
        if captcha_model.captcha == captcha:
            global the_email
            the_email = email_model.email
            return {"code":200}
        else:
            return {"code": 400, "message": "captcha"}
    else:
        return {"code":400,"message":"email"}


@bp.route("/forget_form_password",methods=['POST','GET'])
def password_check():
    global the_email
    email = the_email
    password_form = ForgetFormPassword(request.form)
    if password_form.validate():
        new_password = password_form.user_password.data
        user_model = User.query.filter_by(user_email=email).first()
        user_model.user_password = generate_password_hash(new_password)
        db.session.commit()
        print("success")
        return redirect(url_for("User.login"))
    else:
        return redirect(url_for("User.login"))




