from exts import db

# 定义orm模型
# autoincrement = True
class User(db.Model):
    __tablename__ = 'user_TEST'
    user_email = db.Column(db.String(40), primary_key = True, nullable=False)
    user_name = db.Column(db.String(200), nullable = False)
    user_password = db.Column(db.Text, nullable = False)
