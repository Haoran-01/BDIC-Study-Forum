import json

from flask import Blueprint, request, render_template, jsonify
from models import QuestionType
from forms import QuestionForm
from exts import db

bp = Blueprint("forum", __name__, url_prefix="/forum")

@bp.route("/sections", methods=['GET', 'POST'])
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


