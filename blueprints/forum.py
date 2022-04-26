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
    return jsonify(data =result), 200

@bp.route("/section_detail",methods=['GET'])
def section_detail():
    post_type_name = request.args.get('type_name')
    type = QuestionType.query.filter_by(type_name=post_type_name).all()
    result = []
    for i in type:
        dic = {
            "type_name": i.type_name,
            "total_post": i.total_post,
            "today_post": i.today_post,
            "today_comment": i.today_comment,
            "rank": i.rank,
            "sector_image_url": i.sector_image_url,
            "sector_detail": i.sector_detail
        }
        result.append(dic)

    return jsonify(data=result), 200


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
    return jsonify(data=[{'post_type_name':type_name, 'content': content, 'picture_url':user_image, 'title':title, 'comments_number':comment_number, 'time':time, 'user_email':user_email, "user_name":user_name}]),200

@bp.route("/post/comments", methods=['GET'])
def comments():
    post_id = request.args.get('post_id')
    comments = Comment.query.filter_by(post_id=post_id).all()
    result = []
    for i in comments:
        user = UserProfile.query.filter_by(user_email=i.user_email).first()
        dic = {
            "comment_id": i.cmt_id,
            "user_name" : user.user_name,
            "user_email": i.user_email,
            "content": i.content,
            "time": i.create_time,
            "user_image": user.profile,
            "like":i.like
        }
        result.append(dic)

    return jsonify(comments=result), 200

@bp.route("/publish/post", methods=['GET', 'POST'])
@login_required
def publish_post():
    data = request.get_json(silent=True)
    print(data)
    title = data['title']
    content = data['content']
    type_name = data['section']
    post_type = QuestionType.query.filter_by(type_name=type_name).first().type_number
    user_email = current_user.user_email
    post = PostModel(post_type=post_type, title=title, content=content, author_email=user_email,comments_number=0)
    db.session.add(post)
    db.session.commit()
    return jsonify(), 200

@bp.route("/publish/comment", methods=['GET', 'POST'])
@login_required
def publish_comment():
    data = request.get_json(silent=True)
    print(data)
    post_id = data['post_id']
    content = data['content']['ops'][0]['insert']
    PostModel.query.filter_by(id=post_id).first().comments_number += 1
    user_email = current_user.user_email
    post = Comment(post_id=post_id, content=content, user_email=user_email)
    db.session.add(post)
    db.session.commit()
    return jsonify(), 200

@bp.route('/like/comment', methods=['GET', 'POST'])
def like():
    data = request.get_json(silent=True)
    print(data)
    comment_id = data['comment_id']
    comment = Comment.query.filter_by(cmt_id=comment_id).first()
    comment.like = comment.like + 1
    db.session.commit()
    return jsonify(), 200

@bp.route("/section/get_new_posts", methods=['GET','POST'])
def get_new_posts():
    post_type = QuestionType.query.filter_by(type_name=request.args.get("type_name")).first().type_number
    posts = db.session.query(PostModel).filter_by(post_type=post_type).order_by(PostModel.id.desc()).all()
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
    if len(data) == 0:
        return jsonify(message="该板块还没有帖子"), 201
    return jsonify({"data": data}), 200


@bp.route("/section/get_hot_posts", methods=['GET'])
def get_hot_posts():
    post_type = QuestionType.query.filter_by(type_name=request.args.get("type_name")).first().type_number
    posts = db.session.query(PostModel).filter_by(post_type=post_type).order_by(PostModel.comments_number.desc()).all()
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
    if len(data) == 0:
        return jsonify(message="该板块还没有帖子"), 201
    return jsonify({"data": data}), 200








