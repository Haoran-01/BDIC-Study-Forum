from flask import Flask,Response,request,session,Blueprint

bp = Blueprint("Cookie_Session",__name__,url_prefix="/")

@bp.route('/set_cookie/<name>')
def set_cookie(name):
    response = Response ("cookie 设置")
    user_email=request.form.get();
    user_id=request.form.get();
    response.set_cookie("user_email",user_email)
    response.set_cookie("user_id",user_id)
    return response

@bp.route('/get_cookie')
def get_cookie():
    user_id = request.cookies.get("user_id")
    user_email = request.cookies.get("user_email")
    print("user_id", user_id)
    return "获取cookie"

@bp.route('/set_session')
def set_session():
    session['user_id'] = request.form.get();
    session['user_email'] = request.form.get();
    return "session 设置成功"

@bp.route('/get_session')
def get_session():
    user_name = session.get('user_id')
    user_email= session.get('user_email')

    """
    if (user_id == None | | user_email == null)
        response = Response("请先登录")
        return response
    return "get_session"
    """