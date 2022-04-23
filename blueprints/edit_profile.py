from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from sqlalchemy.sql.functions import current_user
from flask_login import login_required
from models import UserProfile
from exts import db
import json

bp = Blueprint("edit_profile",__name__,url_prefix="/")

#个人信息编辑
@bp.route('/profile',methods=['POST','GET'])
#@login_required
def edit_profile():
    print('begin edit')
    data = request.get_json()

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