from flask import Flask,Response,request,session

app = Flask(__name__)
app.config['SECRET_KEY']='dskjfwqienkehyr1'

@app.route('/set_cookie')
def set_cookie():
    response=Response ("cookie 设置")
    response.set_cookie("user_id","XXX")
    return response

@app.route('/get_cookie')
def get_cookie():
    user_id=request.cookies.get("user_id")
    print("user_id",user_id)
    return "获取cookie"

@app.route('/set_session')
def set_session():
    session['username']='CyanPine'
    return "session 设置成功"

@app.route('/get_session')
def get_session():
    username=session.get('username')
    print('username:',username)
    return "get_session"


@app.route('/')
def hello_world():
    return 'hello world!'


if __name__ == '__main__':
    app.run()