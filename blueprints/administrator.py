import flask_login
from flask import Blueprint, request, jsonify
from models import Administrator, User, Comment, PostModel
from exts import db

bp = Blueprint("administrator", __name__, url_prefix="/adm")

@bp.route("/adm/registration", methods=['GET'])
def get_registration_number():
        # 总注册人数
        registration_numbers = len(User.query.all())
        return jsonify({'registration_numbers': registration_numbers}), 200


@bp.route("/adm/gross_post", methods=['GET'])
def get_gross_post():
        # 总发帖数
        gross_post_numbers = len(PostModel.query.filter_by().all())
        return jsonify({'gross_post_numbers': gross_post_numbers}), 200

@bp.route("/adm/gross_comment", methods=['GET'])
def get_gross_post():
        # 总评论数
        gross_comment_numbers = len(Comment.query.filter_by().all())
        return jsonify({'gross_post_numbers': gross_comment_numbers}), 200
