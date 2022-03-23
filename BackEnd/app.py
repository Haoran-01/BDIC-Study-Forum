from flask import Flask

from flask_migrate import Migrate
from models import Article, User, UserExtension
import config
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app,db)



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
