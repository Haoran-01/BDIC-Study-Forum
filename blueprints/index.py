from flask import Blueprint, request, render_template

bp = Blueprint("Index", __name__, url_prefix="/")


# 论坛主界面
@bp.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


# 论坛主界面得到10个最新的帖子
@bp.route("/index/get_post")
def get_post():
    return


# 论坛主界面得到热门板块
@bp.route("/index/get_popular_type")
def get_popular_type():
    return
