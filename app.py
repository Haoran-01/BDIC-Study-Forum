from flask import Flask,request,render_template,url_for
import config
from flask_migrate import Migrate
from exts import db
# from models import User
from forms import LoginFrom
from blueprints import page_bp,user_bp
# 创建一个app对象
app = Flask(__name__)

#app.config[] 配置 配置项全部放到config里
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(page_bp)

# 设置访问的url，‘/’为设置成一个根路径

# 连接登录界面
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginFrom(request.form)
        if form.validate():
            return "登陆成功"
        else:
            return "登录失败"


if __name__ == '__main__':
    app.run()