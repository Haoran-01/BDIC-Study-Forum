from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from models import Course
from exts import db
import json

bp = Blueprint("course",__name__,url_prefix="/")

@bp.route('/course',methods=['POST','GET'])
#@login_required
def course():
    print('begin edit')
    data = request.get_json()

    print(data)
    print(data["From"])

    id = Course.id
    From = data["From"]
    To = data["To"]
    Room = data["Room"]
    Lecturer = data["Lecturer"]
    course_name = data["course_name"]
    color = data["color"]

    course = Course(id,From,To,Room,Lecturer,course_name,color)

    db.session.add(course)
    db.session.commit()

    my_id=str(id)


    json_data = {"items":{
        "id": my_id,
        "From": data["From"],
        "To": data["To"],
        "Room": data["Room"],
        "Lecturer": data["Lecturer"],
        "course_name": data["course_name"],
        "color": data["color"]
    }}

    #print(json_data)
    course_res_json = json.dumps(json_data)
    #print(course_res_json)
    return course_res_json