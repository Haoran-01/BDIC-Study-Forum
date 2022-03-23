from flask import Flask,jsonify,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
# import config


app = Flask(__name__)

#数据库的配置变量
HOSTNAME='127.0.0.1'
PORT ='3306'
DATABASE='project_group_12'
USERNAME='root'
PASSWORD='Wwj13049995918()'
DB_URI='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
app.config['SQLALCHEMY_DATABASE_URI']=DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)



@app.route('/profile')
def profile():
    user_id=request.args.get("id")
    if user_id:
        return "用户个人中心"
    else:
        return redirect(url_for("index"))

@app.route('/')
def index():  # put application's code here
    #return  "hello 知了"
    return {"username":"group12"}

if __name__ == '__main__':
    app.run()
