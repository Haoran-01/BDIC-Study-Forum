from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from sqlalchemy.sql.functions import current_user
from flask_login import login_required
from models import UserProfile, PostModel, QuestionType
from exts import db
import json

bp = Blueprint("edit_profile",__name__,url_prefix="/")

#个人信息编辑
@bp.route('/profile',methods=['POST','GET'])
#@login_required
def edit_profile():
    print('begin edit')
    data = request.get_json(silent=True)

    user_name = data["user_name"]
    introduction = data["introduction"]
    user_email = data["user_email"]
    grade = data["grade"]
    department = data["department"]
    major = data["major"]

    userprofile = UserProfile(user_name,introduction,user_email,grade,department,major,"profile111")
    #def __init__(self, user_name, introduction, user_email, grade, department, major, profile)
    #print(data)

    db.session.add(userprofile)
    db.session.commit()

    json_data = {
        "user_name":data["user_name"],
        "introduction":data["introduction"],
        "user_email":data["user_email"],
        "grade":data["grade"],
        "department":data["department"],
        "major":data["major"]
    }

    #print(json_data)
    up_res_json = json.dumps(json_data)
    #print(up_res_json)
    return up_res_json

    #return jsonify(code= 200, message= "save successfully!", data=data)

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
            "picture_url": "http://tncm.zm/psm",
            "title": i.title,
            "user_email": i.author_email,
            "time": i.create_time
        }
        data.append(dict)
    if len(data) == 0:
        return jsonify(code=200,message="没发布过帖子")
    return jsonify(code=200,data=data)