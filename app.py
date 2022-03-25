from flask import Flask,request,render_template,url_for
import config
from flask_migrate import Migrate
from exts import db
from models import User
from forms import LoginFrom,RegistForm
from blueprints import page_bp,user_bp,cs_bp
# 创建一个app对象
app = Flask(__name__)

#app.config[] 配置 配置项全部放到config里
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(page_bp)
app.register_blueprint(cs_bp)



if __name__ == '__main__':
    app.run()