from exts import db
from datetime import datetime
from flask_login import UserMixin
# 定义orm模型
# autoincrement = True

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_email = db.Column(db.CHAR(200), primary_key = True, nullable=False, unique=True)
    user_name = db.Column(db.CHAR(200), nullable = False, unique=True)
    user_password = db.Column(db.CHAR(200), nullable = False)

    def get_id(self):
        return self.user_email

class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.CHAR(100), nullable=False, unique=True)
    captcha = db.Column(db.CHAR(10), nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)

class QuestionModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.CHAR(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_email = db.Column(db.CHAR(200), db.ForeignKey("user.user_email"))
    post_type = db.Column(db.Integer, nullable=False)
    author = db.relationship("User", backref="questions")

class QuestionType(db.Model):
    __tablename__ = 'questiontype'
    type_name = db.Column(db.CHAR(40), primary_key=True, nullable=False)
    type_number = db.Column(db.Integer, nullable=False, unique=True, autoincrement=True)
    total_post = db.Column(db.Integer, nullable=False)
    today_post = db.Column(db.Integer, nullable=False)
    today_comment = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)