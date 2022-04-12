import json

from flask import Blueprint, request, render_template, jsonify
from forms import QuestionForm
from exts import db

bp = Blueprint("forum", __name__, url_prefix="/forum")

@bp.route("/sections", methods=['GET', 'POST'])
def forum_index():
    if request.method == ["POST"]:
        data = json.load(request.get_data(as_text=True))
        return {"code": 200}
    if request.method == ['GET']:
        if not get_type_name:
            return jsonify(msg="Request the type name")
        type = QuestionForm.query.filter_by(type_name=get_type_name).first()
        if type:
            title = type.type_name.data
            total_post = type.total_post.data
            today_post = type.today_post.data
            today_comment = type.today_comment.data
            rank = type.rank.data
        return jsonify(title=title, total_post=total_post, today_post=today_post, today_comment=today_comment,rank=rank)






