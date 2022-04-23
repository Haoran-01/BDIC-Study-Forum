import json

from flask import Blueprint, request, render_template, jsonify
from flask_login import login_required, current_user

from models import QuestionType, PostModel, User, Comment, UserProfile
from exts import db

bp = Blueprint("forum", __name__, url_prefix="/forum")

@bp.route("/sections", methods=['GET'])
def forum_index():
    type = QuestionType.query.filter_by().all()
    result = []
    for i in type:
        dic = {
        "type_name" : i.type_name,
        "total_post" : i.total_post,
        "today_post" : i.today_post,
        "today_comment" : i.today_comment,
        "rank" : i.rank,
        "sector_image_url" : i.sector_image_url,
        "sector_detail" : i.sector_detail
        }
        result.append(dic)

    return jsonify(data =result)

@bp.route("/post", methods=['GET'])
def forum():
    post_id = request.args.get('post_id')
    post = PostModel.query.filter_by(id=post_id).first()
    typenumber = post.post_type
    post_type = QuestionType.query.filter_by(type_number=typenumber).first()
    type_name = post_type.type_name
    title = post.title
    comment_number = post.comments_number
    time = post.create_time
    content = post.content
    user_email = post.author_email
    user = User.query.filter_by(user_email=user_email).first()
    user_image = user.profile
    return jsonify(type_name=type_name, content= content, user_image=user_image, title=title, comment_number=comment_number, time=time, user_email=user_email)

@bp.route("/post/comments", methods=['GET'])
def comments():
    post_id = request.args.get('post_id')
    comments = Comment.query.filter_by(post_id=post_id).all()
    result = []
    for i in comments:
        user = UserProfile.query.filter_by(user_email=i.user_email).first()
        dic = {
            "user_email": i.user_email,
            "content": i.content,
            "time": i.create_time,
            "user_image": user.profile,
        }
        result.append(dic)

    return jsonify(comments=result)

@bp.route("/publish/post", methods=['GET', 'POST'])
@login_required
def publish_post():
    data = request.get_json(silent=True)
    title = data['title']
    content = data['content']
    user_email = current_user.user_email










