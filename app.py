from flask import Flask
import config
from flask_migrate import Migrate
from exts import db, mail
import os
from blueprints import page_bp,user_bp,cs_bp,forum_bp

# 创建一个app对象
app = Flask(__name__)

#app.config[] 配置 配置项全部放到config里
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(page_bp)
app.register_blueprint(cs_bp)
app.register_blueprint(forum_bp)

app.secret_key = os.getenv("SECRET_KEY","dskjfwqienkehyr1")
if __name__ == '__main__':
    app.run()