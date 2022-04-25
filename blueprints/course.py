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

@bp.route('/course/insert2',methods=['POST','GET'])
@login_required
def insert_course():
    data = request.get_json()
    course_id = Course.course_id
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    classroom = data["classroom"]
    teacher = data["teacher"]
    course_name = data["course_name"]
    course_color = data["course_color"]

    course = Course(course_id,classroom,teacher,course_name,course_color)
    sql = Course.front_id ==front_id and Course.user_email==current_user_email
    db.session.query(Course).filter_by(sql).update(course)
    db.session.commit()

    return {"success":200}

@bp.route('/course/delete',methods=['POST','GET'])
def delete_course():
    data = request.get_json()
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    sql = Course.front_id ==front_id and Course.user_email==current_user_email
    res = db.session.query(Course).filter(sql).delete()
    db.session.commit()
    db.session.close()

    return {"success":200}

@bp.route('/course/query_single_course',methods=['POST','GET'])
def query_single_course():
    data = request.get_json()
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    sql = Course.front_id == front_id and Course.user_email == current_user_email
    single_course = db.session.query(Course).filter(sql)
    return jsonify({'classroom':single_course.classroom, 'teacher': single_course.teacher, 'course_name':single_course.course_name, 'course_color':single_course.course_color})

@bp.route('/course/user_all_course',methods=['POST','GET'])
def user_all_course():
    user_all_course = db.session.query(Course).filter(Course.user_email == current_user.user_email).all()
    result = []
    for i in user_all_course:
        dic = {
            "course_id": i.front_id,
            "x": i.x,
            "y": i.y
        }
        result.append(dic)
    return jsonify(comments=result)


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
    return course_res_json 
    """