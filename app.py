from flask import Flask,request,render_template,url_for
import config
from flask_migrate import Migrate
from db import db
# from models import User
from forms import LoginFrom
# 创建一个app对象
app = Flask(__name__)

#app.config[] 配置 配置项全部放到config里
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
@app.route('/user')
def user_add():
    # 添加数据
    user = User(user_name = '阎浩然' ,user_password = 'root')
    db.session.add(user)
    # 提交数据
    db.session.commit()

    # 查询数据
    user_1 = User.query.filter_by(user_id = 1)[0]
    print(user_1.user_password)

    # 更改数据 （先查再改）
    user_1 = User.query.filter_by(user_id=1)[0]
    user_1.user_password = "123456"
    db.session.commit()

    # 删除数据
    # user_1 = User.query.filter_by(user_id=1).delete()
    # db.session.commit()

    # 外键 db.ForeignKey()
    # orm 中用relationship
    # backref 代表反向引用，代表对方询问我的时候的字段名称
    # the_user = db.relationship('User',backref = '表名')
    # the_user = db.relationship('User',backref = （’表名‘，uselist = False)) 这样返回的是一个对象而不是一个列表

    return "sucess"

# 设置访问的url，‘/’为设置成一个根路径
@app.route('/')
def hello_world():
    return 'hello world!'


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