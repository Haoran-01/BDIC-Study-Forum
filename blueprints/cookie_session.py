from flask import Flask,Response,request,session,Blueprint,jsonify

bp = Blueprint("Cookie_Session",__name__,url_prefix="/")

@bp.route('/set_cookie')
def set_cookie():
    response = Response ("cookie 设置")
    user_email=request.form.get();
    user_id=request.form.get();
    response.set_cookie("user_email",user_email)
    response.set_cookie("user_id",user_id)
    return response

@bp.route('/get_cookie')
def get_cookie():
    user_email = request.cookies.get("_user_id")
    return jsonify({'code':200, 'message': user_email})

@bp.route('/set_session')
def set_session():
    data = request.get_json(silent=True)
    session['_user_id'] = data['user_email']
    return jsonify({'code':200})

@bp.route('/get_session',methods=['GET'])
def get_session():
    if session.get("_user_id"):
        user_email = session.get('_user_id')
        return jsonify({"message":user_email}),200
    else:
        return jsonify(status=400), 400