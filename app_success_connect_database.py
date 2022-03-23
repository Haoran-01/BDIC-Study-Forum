from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zl_flask'
USERNAME = 'root'
PASSWORD = 'Sunqi750666'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

migrate = Migrate(app,db)

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


# db.drop_all()
db.create_all()

@app.route("/oto")
def one_to_one():
    user = User(username="Jerry")
    extension = UserExtension(school="Peking University")
    user.extension = extension
    db.session.add(user)
    db.session.commit()
    return "one to one successful"

@app.route("/otm")
def one_to_many():
    article1 = Article(title="111", content="Jerry is very handsome.")
    article2 = Article(title="222", content="Jerry is a man with sense of humor.")
    user = User(username="Jerry")
    article1.author = user
    article2.author = user
    db.session.add(article1,article2)
    db.session.commit()

    print(user.articles)
    return "One to many successful!"





@app.route("/delete")
def delete():
    Article.query.filter_by(id=1).delete()
    db.session.commit()
    return "delete successfully!"

@app.route("/alter")
def alter():
    article = Article.query.filter_by(id=1)[0]
    article.content = "y"
    db.session.commit()
    return "Alter successfully!"

@app.route("/find")
def find():
    article = Article.query.filter_by(id=1)[0]
    print(article.title)
    return "successful!"

@app.route("/article")
def article_view():
    article = Article(title="flower",content="XXXXXX")
    db.session.add(article)
    db.session.commit()
    return "successful!"

@app.route('/')
def hello_world():  # put application's code here
    #TEST CONNECTION

    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())

    return 'Hello World!'


if __name__ == '__main__':
    app.run()