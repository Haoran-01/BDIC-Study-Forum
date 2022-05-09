from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from sqlalchemy.sql.functions import current_user
from flask_login import login_required
from models import UserProfile, PostModel, QuestionType
from exts import db
import json

bp = Blueprint("edit_profile",__name__,url_prefix="/")

#个人信息编辑
@bp.route('/profile',methods=['POST','GET'])
def edit_profile():
    data = request.get_json(silent=True)

    user_name = data["user_name"]
    introduction = data["introduction"]
    #user_email = current_user.user_email
    user_email = data["user_email"]
    grade = data["grade"]
    department = data["department"]
    major = data["major"]

    userprofile = UserProfile.query.filter_by(user_email=user_email).first()

    userprofile.user_name = user_name
    userprofile.introduction = introduction
    userprofile.grade = grade
    userprofile.department = department
    userprofile.major = major
    db.session.commit()

    return jsonify(code=200)

@bp.route('/get_profile', methods=['GET'])
def get_profile():
    data = request.get_json(silent=True)
    user_email = data["user_email"]
    userprofile = UserProfile.query.filter_by(user_email=user_email).first()

    user_name = userprofile.user_name
    introduction = userprofile.introduction
    grade = userprofile.grade
    department = userprofile.department
    major = userprofile.major

    return jsonify(user_name=user_name, introduction=introduction, grade=grade, department=department, major=major)

# 个人界面得到自己的所有帖子
@bp.route("/profile/my_post", methods=['GET'])

def get_my_post():
    email = request.args.get("email")
    posts = PostModel.query.filter_by(author_email=email)
    data = []
    for i in posts:
        dict = {
            "content": i.content,
            "comments_number": i.comments_number,
            "post_type_name": QuestionType.query.filter_by(type_number=i.post_type).first().type_name,
            "post_id": i.id,
            "user_name": i.author.user_name,
            "picture_url": UserProfile.query.filter_by(user_email=i.author_email).first().profile,
            "title": i.title,
            "user_email": i.author_email,
            "time": i.create_time
        }
        data.append(dict)
    if len(data) == 0:
        return jsonify(code=200,message="没发布过帖子")
    return jsonify(code=200,data=data)

@bp.route('/profile/post_photo', methods = ['GET', 'POST'])

def post_photo():
    return