from flask import Blueprint,render_template
from exts import Mail
from flask_mail import Message

bp=Blueprint("user",__name__,url_prefix="/user")

@bp.route("/login")
def login():
    return render_template("login.html")

@bp.route("/register")
def register():
    return render_template("register.html")

@bp.route("/mail")
def my_mail():
    message=Message(
        subject="邮箱测试",
        recipient=['2769059069@qq.com'],
        body="这是一篇测试邮件"
    )
    mail.send(message)
    return "success"
    