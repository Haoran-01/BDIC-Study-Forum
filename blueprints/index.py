from flask import Blueprint, request, render_template, jsonify
from models import PostModel, QuestionType
import flask_login

bp = Blueprint("Index", __name__, url_prefix="/")

"""
#进入页面前检查是否登录
@bp.before_request
def if_sign_in():
    if request.url == "/":
        user = flask_login.current_user
        if user.is_anonymous == True:
            return jsonify({"code": 200, "message": "anonymous"})
        else:
            # # 用户应绑定用户头像
            # user_picture = user.picture
            # user_email = user.user_email
            return jsonify({"code": 200, "message": "user", "user_email": user.email})
    else:
        return None
"""


# 论坛主界面
@bp.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")


# 论坛主界面得到10个最新的帖子
@bp.route("/index/get_post")
def get_post():
    posts = PostModel.query.all()
    data = []
    for i in posts:
        dict = {
            "content": i.content,
            # 帖子模型缺少评论数
            # "comments_number": i.comments_number,
            "post_type_name": i.post_type_name,
            "author": i.author,
            # 需要有相对应的用户照片url
            # "picture_url": "http://tncm.zm/psm",
            "title": i.title
                }
        data.append(dict)
    return jsonify({"code":200,"data":data})


# 论坛主界面得到热门板块
@bp.route("/index/get_popular_type")
def get_popular_type():
    question_types = QuestionType.query.all()
    data = []
    for i in question_types:
        dict = {
            "type_name": i.type_name,
            "today_comment": i.today_comment,
            # 需要有相对应的板块图片
            # "type_picture": "http://hzvgqyy.ni/occvggpean",
            "rank": i.rank
        }
        data.append(dict)
    return jsonify({"code":200,"data":data})
