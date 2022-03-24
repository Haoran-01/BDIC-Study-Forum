from exts import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)

class UserExtension(db.Model):
    __tablename__ = "user_extension"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    #db.backref
    # 1. 在反向引用一对一
    user = db.relationship("User", backref=db.backref("extension", uselist=False))

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    author = db.relationship("User", backref="articles")