import datetime

from flask import Blueprint, request, jsonify
from models import Administrator, PostModel, Comment, EmailCaptchaModel, QuestionType, User
from exts import db
from sqlalchemy import extract
from datetime import datetime, timedelta
from flask_login import login_required, current_user

bp = Blueprint("administrator", __name__, url_prefix="/adm")

@bp.route("/registration", methods=['GET'])
def get_registration_number():
        # 总注册人数
        registration_numbers = len(User.query.all())
        return jsonify({'registration_numbers': registration_numbers}), 200


@bp.route("/gross_post", methods=['GET'])
def get_gross_post():
        # 总发帖数
        gross_post_numbers = len(PostModel.query.filter_by().all())
        return jsonify({'gross_post_numbers': gross_post_numbers}), 200

@bp.route("/gross_comment", methods=['GET'])
def get_gross_comment():
        # 总评论数
        gross_comment_numbers = len(Comment.query.filter_by().all())
        return jsonify({'gross_post_numbers': gross_comment_numbers}), 200

@bp.route('/today_comment',methods=['GET'])
def get_today_comment():
    comment_list = Comment.query.filter_by().all()
    for i in comment_list:
        if not i.create_time.date() == datetime.now().date():
            comment_list.remove(i)
    return jsonify(today_comment_num=len(comment_list)), 200

@bp.route('/today_post', methods=['GET'])
def get_today_post():
    post_list = PostModel.query.filter_by().all()
    for i in post_list:
        if not i.create_time.date() == datetime.now().date():
            post_list.remove(i)
    return jsonify(today_post_num=len(post_list)), 200


@bp.route('/post', methods=['GET'])
def get_post_table():
    post_list = PostModel.query.filter_by().all()
    all_post_list = []
    for i in post_list:
        dict = {
            'post_id' : i.id,
            'post_title' : i.title,
            'section' : QuestionType.query.filter_by(type_number=i.post_type).first().type_name
        }
        all_post_list.append(dict)
    return jsonify(data=all_post_list), 200


@bp.route('/users', methods=['GET'])
def get_user_table():
    user_list = User.query.filter_by().all()
    all_user_list = []
    for i in user_list:
        dict = {
            'user_email' : i.user_email,
            'name' : i.user_name,
        }
        all_user_list.append(dict)
    return jsonify(data=all_user_list), 200

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

    return jsonify(data = [{'name':'Lecture Question', 'value': len(lecture)}, {'name':'Lost And Found', 'value':len(lost)}, {'name':'Transaction', 'value':len(tran)}])

@bp.route('/seven_types', methods=['GET'])
def get_seven_types():
    end = datetime.now()
    end_year = end.year
    end_month = end.month
    end_day = end.day

    start = end - timedelta(days=7)

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

    return jsonify(data = [{'name':'Lecture Question', 'value': len(lecture)}, {'name':'Lost And Found', 'value':len(lost)}, {'name':'Transaction', 'value':len(tran)}])

@bp.route('/seven_comment', methods=['GET'])
def get_seven_comment():
    end = datetime.now()

    end = end - timedelta(days=7)
    start = end - timedelta(days=1)

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

        end = end + timedelta(days=1)
        start = end + timedelta(days=1)

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
    end = datetime.now()

    end = end - timedelta(days=7)
    start = end - timedelta(days=1)

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

        end = end + timedelta(days=1)
        start = end + timedelta(days=1)

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
    end = datetime.now()

    end = end - timedelta(days=7)
    start = end - timedelta(days=1)

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

        end = end + timedelta(days=1)
        start = end + timedelta(days=1)

        end_year = end.year
        end_month = end.month
        end_day = end.day

        start_year = start.year
        start_month = start.month
        start_day = start.day

        i = i + 1;

    return jsonify(data=result)

@bp.route('type_name', methods=['GET'])
def get_all_type_name():
    result = []
    types = db.session.query(QuestionType).filter().all()
    for type in types:
        result.append(type.type_name)
    return jsonify(data = result)