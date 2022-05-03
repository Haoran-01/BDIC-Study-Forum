import flask_login, openpyxl, xlrd
from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from models import Course
from exts import db
import json
from flask_login import login_required,current_user

bp = Blueprint("course",__name__,url_prefix="/course")

@bp.route('/move',methods=['POST','GET'])
def move_course():
    data = request.get_json()
    front_id = data["course_id"]
    x = data["x"]
    y = data["y"]
    course = Course(x=x, y=y, front_id=front_id)

    db.session.add(course)
    db.session.commit()

    return {"success":200}

@bp.route('/insert',methods=['POST','GET'])
@login_required
def insert_course():
    data = request.get_json()
    id = Course.course_id
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    classroom = data["classroom"]
    teacher = data["teacher"]
    course_name = data["course_name"]
    course_color = data["course_color"]

    course = Course(id,classroom,teacher,course_name,course_color)
    sql = Course.front_id ==front_id and Course.user_email==current_user_email
    db.session.query(Course).filter_by(sql).update(course)
    db.session.commit()

    return {"success":200}

@bp.route('/delete',methods=['POST','GET'])
def delete_course():
    data = request.get_json()
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    sql = Course.front_id ==front_id and Course.user_email==current_user_email
    res = db.session.query(Course).filter(sql).delete()
    db.session.commit()
    db.session.close()

    return {"success":200}

@bp.route('/query_single_course',methods=['POST','GET'])
def query_single_course():
    data = request.get_json()
    front_id = data["course_id"]
    current_user_email = current_user.user_email
    sql = Course.front_id == front_id and Course.user_email == current_user_email
    single_course = db.session.query(Course).filter(sql)
    return jsonify({'classroom':single_course.classroom, 'teacher': single_course.teacher, 'course_name':single_course.course_name, 'course_color':single_course.course_color})

@bp.route('/user_all_course',methods=['POST','GET'])
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
    return jsonify(result)


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

@bp.route('/upload_excel', methods=['POST'])
@login_required

@bp.route('/excel_recognition', methods=['GET'])
@login_required
def excel_file_recognition():
    user_email = current_user.user_email
    file_name = request.args.get('file_name')
    if file_name.endswith('.xls'):
        xlfile = xlrd.open_workbook('2018级物联网工程专业课表.xls')
        sheet = xlfile.sheet_by_index(0)
        i = 0
        j = 0
        for row in sheet.get_rows():
            for cell in row:
                if cell.value != '':
                    result = cell.value.split('/')
                    if len(result) == 4:
                        print(j - 2, i - 2, result)
                j = j + 1
            i = i + 1
            j = 0
    if file_name.endswith('.xlsx'):
        wb = openpyxl.load_workbook('2018级物联网工程专业课表.xlsx')
        sheet = wb.worksheets[0]
        i = 0
        j = 0
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value != None:
                    result = cell.value.split('/')
                    if len(result) == 4:
                        print(j - 2, i - 2, result)
                j = j + 1
            i = i + 1
            j = 0