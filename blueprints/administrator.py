import datetime

from flask import Blueprint, request, jsonify
from models import Administrator, PostModel, Comment, EmailCaptchaModel
from exts import db
from sqlalchemy import extract
from flask_login import login_required, current_user

bp = Blueprint("administrator", __name__, url_prefix="/adm")

@bp.route('/types', methods=['GET'])
def get_all_types():
    # 查询2020年12月8日的数据
    lecture = db.session.query(PostModel).filter(
        PostModel.post_type == 1
    ).all()

    lost = db.session.query(PostModel).filter(
        PostModel.post_type == 2
    ).all()

    tran = db.session.query(PostModel).filter(
        PostModel.post_type == 2
    ).all()

    return jsonify(data = [{'Lecture Question':len(lecture)}, {'Lost And Found':len(lost)}, {'Transaction':len(tran)}])

@bp.route('/seven_types', methods=['GET'])
def get_seven_types():
    end = datetime.datetime.now()
    end_year = end.year
    end_month = end.month
    end_day = end.day

    start = end - datetime.timedelta(days=7)

    start_year = start.year
    start_month = start.month
    start_day = start.day
    # 查询2020年12月8日的数据
    lecture = db.session.query(PostModel).filter(
        extract('day', PostModel.create_time) <= end_day,
        extract('year', PostModel.create_time) <= end_year,
        extract('month', PostModel.create_time) <= end_month,
        extract('day', PostModel.create_time) >= start_day,
        extract('year', PostModel.create_time) >= start_year,
        extract('month', PostModel.create_time) >= start_month,
        PostModel.post_type == 1
    ).all()

    lost = db.session.query(PostModel).filter(
        extract('day', PostModel.create_time) <= end_day,
        extract('year', PostModel.create_time) <= end_year,
        extract('month', PostModel.create_time) <= end_month,
        extract('day', PostModel.create_time) >= start_day,
        extract('year', PostModel.create_time) >= start_year,
        extract('month', PostModel.create_time) >= start_month,
        PostModel.post_type == 2
    ).all()

    tran = db.session.query(PostModel).filter(
        extract('day', PostModel.create_time) <= end_day,
        extract('year', PostModel.create_time) <= end_year,
        extract('month', PostModel.create_time) <= end_month,
        extract('day', PostModel.create_time) >= start_day,
        extract('year', PostModel.create_time) >= start_year,
        extract('month', PostModel.create_time) >= start_month,
        PostModel.post_type == 2
    ).all()

    return jsonify(data = [{'Lecture Question':len(lecture)}, {'Lost And Found':len(lost)}, {'Transaction':len(tran)}])

@bp.route('/seven_comment', methods=['GET'])
def get_seven_comment():
    end = datetime.datetime.now()

    end = end - datetime.timedelta(days=7)
    start = end - datetime.timedelta(days=1)

    end_year = end.year
    end_month = end.month
    end_day = end.day

    start_year = start.year
    start_month = start.month
    start_day = start.day

    result = []

    i = 0
    while (i < 7):
        comments = db.session.query(Comment).filter(
            extract('day', Comment.create_time) <= end_day,
            extract('year', Comment.create_time) <= end_year,
            extract('month', Comment.create_time) <= end_month,
            extract('day', Comment.create_time) >= start_day,
            extract('year', Comment.create_time) >= start_year,
            extract('month', Comment.create_time) >= start_month
        ).all()
        result.append(len(comments))

        end = end + datetime.timedelta(days=1)
        start = end + datetime.timedelta(days=1)

        end_year = end.year
        end_month = end.month
        end_day = end.day

        start_year = start.year
        start_month = start.month
        start_day = start.day

        i = i + 1;




    return jsonify(data = result)

@bp.route('/seven_registration', methods=['GET'])
def get_seven_registration():
    end = datetime.datetime.now()

    end = end - datetime.timedelta(days=7)
    start = end - datetime.timedelta(days=1)

    end_year = end.year
    end_month = end.month
    end_day = end.day

    start_year = start.year
    start_month = start.month
    start_day = start.day

    result = []

    i = 0
    while (i < 7):
        registration = db.session.query(EmailCaptchaModel).filter(
            extract('day', EmailCaptchaModel.create_time) <= end_day,
            extract('year', EmailCaptchaModel.create_time) <= end_year,
            extract('month', EmailCaptchaModel.create_time) <= end_month,
            extract('day', EmailCaptchaModel.create_time) >= start_day,
            extract('year', EmailCaptchaModel.create_time) >= start_year,
            extract('month', EmailCaptchaModel.create_time) >= start_month
        ).all()
        result.append(len(registration))

        end = end + datetime.timedelta(days=1)
        start = end + datetime.timedelta(days=1)

        end_year = end.year
        end_month = end.month
        end_day = end.day

        start_year = start.year
        start_month = start.month
        start_day = start.day

        i = i + 1;

    return jsonify(data=result)

@bp.route('/seven_post', methods=['GET'])
def get_seven_post():
    end = datetime.datetime.now()

    end = end - datetime.timedelta(days=7)
    start = end - datetime.timedelta(days=1)

    end_year = end.year
    end_month = end.month
    end_day = end.day

    start_year = start.year
    start_month = start.month
    start_day = start.day

    result = []

    i = 0
    while (i < 7):
        registration = db.session.query(PostModel).filter(
            extract('day', PostModel.create_time) <= end_day,
            extract('year', PostModel.create_time) <= end_year,
            extract('month', PostModel.create_time) <= end_month,
            extract('day', PostModel.create_time) >= start_day,
            extract('year', PostModel.create_time) >= start_year,
            extract('month', PostModel.create_time) >= start_month
        ).all()
        result.append(len(registration))

        end = end + datetime.timedelta(days=1)
        start = end + datetime.timedelta(days=1)

        end_year = end.year
        end_month = end.month
        end_day = end.day

        start_year = start.year
        start_month = start.month
        start_day = start.day

        i = i + 1;

    return jsonify(data=result)