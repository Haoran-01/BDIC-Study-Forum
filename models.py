from exts import db
from datetime import datetime
from flask_login import UserMixin
# 定义orm模型
# autoincrement = True

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_email = db.Column(db.CHAR(200), primary_key = True, nullable=False, unique=True)
    user_name = db.Column(db.CHAR(200), nullable = False, unique=False)
    user_password = db.Column(db.CHAR(200), nullable = False)

    def get_id(self):
        return self.user_email


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    email = db.Column(db.CHAR(100), nullable=False, unique=True)
    captcha = db.Column(db.CHAR(10), nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)

# 帖子模型


class PostModel(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.CHAR(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_email = db.Column(db.CHAR(200), db.ForeignKey("user.user_email"))
    post_type = db.Column(db.Integer, nullable=False)
    author = db.relationship("User", backref="questions")
    create_time = db.Column(db.DateTime, default=datetime.now)
    comments_number = db.Column(db.Integer, nullable=False)

# 帖子类别


class QuestionType(db.Model):
    __tablename__ = 'questiontype'
    type_name = db.Column(db.CHAR(40), primary_key=True, nullable=False)
    type_number = db.Column(db.Integer, nullable=False, unique=True, autoincrement=True)
    total_post = db.Column(db.Integer, nullable=False)
    today_post = db.Column(db.Integer, nullable=False)
    today_comment = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    sector_image_url = db.Column(db.CHAR(100), nullable=False)
    sector_detail = db.Column(db.Text, nullable=False)

#用户个人主页
class UserProfile(db.Model):
    __tablename__ = 'userprofile'
    user_name = db.Column(db.VARCHAR(200), nullable = False, unique=False)
    introduction = db.Column(db.VARCHAR(500), nullable = False, unique=False)
    user_email = db.Column(db.VARCHAR(200), primary_key = True, nullable=False, unique=True)
    grade = db.Column(db.Integer, nullable=False)
    department = db.Column(db.VARCHAR(200), nullable = False, unique=False)
    major = db.Column(db.VARCHAR(200), nullable = False, unique=False)

#评论
class Comment(db.Model):
    __tablename__ = 'comment'
    cmt_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    user_email = db.Column(db.CHAR(200), db.ForeignKey("user.user_email"))
    content = content = db.Column(db.Text, nullable=False)
    creat_time = db.Column(db.DateTime, default=datetime.now)
    author = db.relationship("User", backref="comments")
    post = db.relationship("PostModel", backref="comments")

