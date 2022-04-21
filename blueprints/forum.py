import json

from flask import Blueprint, request, render_template, jsonify
from models import QuestionType,PostModel
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
    return jsonify(type_name=type_name, content= content, title=title, comment_number=comment_number, time=time, user_email=user_email)




