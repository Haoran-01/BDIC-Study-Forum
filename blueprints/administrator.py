from flask import Blueprint, request, jsonify
from models import Administrator, PostModel, Comment, QuestionType, User
from exts import db
from flask_login import login_required, current_user
from datetime import datetime
bp = Blueprint("administrator", __name__, url_prefix="/adm")


@bp.route('/get_all_problems', methods=['GET'])
def get_all_problems():
    return


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
