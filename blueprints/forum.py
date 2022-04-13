import json

from flask import Blueprint, request, render_template, jsonify
from models import QuestionType
from forms import QuestionForm
from exts import db

bp = Blueprint("forum", __name__, url_prefix="/forum")

@bp.route("/sections", methods=['GET', 'POST'])
def forum_index(data=None):
    if request.method == "POST":
        data = json.loads(request.get_data(as_text=True))
        get_type_name = data["type_name"]
        if not get_type_name:
            return jsonify(msg="Request the type name")
        type = QuestionType.query.filter_by(type_name=get_type_name).first()
        if type:
            title = type.type_name
            total_post = type.total_post
            today_post = type.today_post
            today_comment = type.today_comment
            rank = type.rank
            return jsonify(title=title, total_post=total_post, today_post=today_post, today_comment=today_comment,
                       rank=rank)
        else:
            return jsonify(msg="This type is not available")


