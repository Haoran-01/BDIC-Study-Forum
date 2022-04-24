from flask import Blueprint, request, render_template, jsonify
from models import PostModel, QuestionType, Comment
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
@bp.route("/index/get_post",methods=['GET'])
def get_post():
    posts = PostModel.query.all()
    data = []
    for i in posts:
        dict = {
            "content": i.content,
            "comments_number": i.comments_number,
            "post_type_name": QuestionType.query.filter_by(type_number=i.post_type).first().type_name,
            "post_id": i.id,
            "user_name": i.author.user_name,
            # 需要有相对应的用户照片url
            "picture_url": "http://tncm.zm/psm",
            "title": i.title,
            "user_email": i.author_email,
            "time": i.create_time
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
            "profile": "http://hzvgqyy.ni/occvggpean",
            "rank": i.rank
        }
        data.append(dict)
    return jsonify({"code":200,"data":data})

@bp.route("/index/get_information",methods=['GET'])
def get_information():
    if flask_login.current_user:
        email = flask_login.current_user.user_email
        # 个人发帖数
        post_numbers = len(PostModel.query.filter_by(author_email=email).all())
        # 个人评论数
        comment_number = len(Comment.query.filter_by(user_email=email).all())
        # 赞同回复
        # 假装有一些代码
        return jsonify({'code':200,'post_number':post_numbers,'comment_number':comment_number})
    else:
        return jsonify({'code':400})

# @bp.route('/1',methods=['GET'])
# def test():
#     numbers = len(PostModel.query.filter_by(author_email='2334201198@qq.com').all())
#     print(numbers)
#     return jsonify({'code':200,'message':1})
