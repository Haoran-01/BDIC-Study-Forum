from flask import Flask,Response,request,session,Blueprint

bp = Blueprint("Cookie_Session",__name__,url_prefix="/")

@bp.route('/set_cookie/<name>')
def set_cookie(name):
    response = Response ("cookie 设置")
    response.set_cookie("user_email","yhr1019@163.com")
    return response

@bp.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get("user_id")
    print("user_id", user_id)
    return "获取cookie"

@bp.route('/set_session')
def set_session():
    session['username'] = 'CyanPine'
    return "session 设置成功"

@bp.route('/get_session')
def get_session():
    username = session.get('username')
    print('username:',username)
    return "get_session"