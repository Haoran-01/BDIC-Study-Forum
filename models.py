from exts import db
from datetime import datetime
# 定义orm模型
# autoincrement = True
class User(db.Model):
    __tablename__ = 'user_TEST'
    user_email = db.Column(db.String(40), primary_key = True, nullable=False)
    user_name = db.Column(db.String(200), nullable = False)
    user_password = db.Column(db.Text, nullable = False)

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)