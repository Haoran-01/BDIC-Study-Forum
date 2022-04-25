import flask_login
from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from models import Course
from exts import db
import json
from flask_login import login_required,current_user

bp = Blueprint("course",__name__,url_prefix="/")

@bp.route('/course',methods=['POST','GET'])
def move_course():
    data = request.get_json()
    course_id = Course.course_id
    front_id = data["course_id"]
    x = data["x"]
    y = data["y"]
    move_course = Course(course_id, None, None, None, None, x, y, front_id)
    print(move_course)

    db.session.add(move_course)
    db.session.commit()

    return {"success":200}

@bp.login_required
def course():
    data = request.get_json()
    course_id = Course.course_id
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    classroom = data["classroom"]
    teacher = data["teacher"]
    course_name = data["course_name"]
    course_color = data["course_color"]

    course = Course(course_id,classroom,teacher,course_name,course_color)

    db.session.query(Course).filter_by(Course.front_id ==front_id and Course.user_email==current_user_email).update(course)
    db.session.commit()

    return {"success":200}


"""
    my_id=str(course_id)


    json_data = {"items":{
        "course_id": my_id,
        "classroom": data["classroom"],
        "teacher": data["teacher"],
        "course_name": data["course_name"],
        "course_color": data["course_color"]
    }}

    #print(json_data)
    course_res_json = json.dumps(json_data)
    #print(course_res_json)
    return course_res_json """