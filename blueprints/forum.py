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
    user_profile = UserProfile.query.filter_by(user_email=user_email).first()
    user = User.query.filter_by(user_email=user_email).first()
    user_name = user.user_name
    user_image = user_profile.profile
    return jsonify(data=[{'post_type_name':type_name, 'content': content, 'picture_url':user_image, 'title':title, 'comments_number':comment_number, 'time':time, 'user_email':user_email, "user_name":user_name}])

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
            "like":i.like
        }
        result.append(dic)

    return jsonify(comments=result)

@bp.route("/publish/post", methods=['GET', 'POST'])
@login_required
def publish_post():
    data = request.get_json(silent=True)
    title = data['title']
    content = data['content']
    post_type = data['post_id']
    user_email = current_user.user_email
    post = PostModel(post_type=post_type, title=title, content=content, user_email=user_email)
    db.session.add(post)
    db.session.commit()
    return jsonify(code=200)

@bp.route("/publish/comment", methods=['GET', 'POST'])
@login_required
def publish_post():
    data = request.get_json(silent=True)
    post_id = data['title']
    content = data['content']
    user_email = current_user.user_email
    post = Comment(post_id=post_id, content=content, user_email=user_email)
    db.session.add(post)
    db.session.commit()
    return jsonify(code=200)








