from flask import Blueprint,request,render_template
from forms import LoginFrom

bp = Blueprint("User",__name__,url_prefix="/user")

@bp.route("/login")

def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginFrom(request.form)
        if form.validate():
            return "登陆成功"
        else:
            return "登录失败"

@bp.route("/register")
def register():
    return "注册"
