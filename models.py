from db import db

# 定义orm模型
class User(db.Model):
    __tablename__ = 'user_TEST'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(200), nullable = False)
    user_password = db.Column(db.Text, nullable = False)

