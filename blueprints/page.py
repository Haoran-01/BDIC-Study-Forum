from flask import Blueprint,request,render_template,session
from flask_login import login_required

bp = Blueprint("Page",__name__,url_prefix="/")


@bp.route("/")
def login():
    return render_template("index.html")

# @bp.route("/index")
# def index():
#     return render_template("index.html")

# @bp.route("/login", methods=['GET','POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')

