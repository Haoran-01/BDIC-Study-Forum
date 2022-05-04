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

@bp.route('/course/insert',methods=['POST','GET'])
@login_required
def insert_course():
    data = request.get_json()
    #id = Course.course_id
    front_id = data["course_id"]
    user_email = current_user.user_email
    #user_email = "2769059069@qq.com"
    classroom = data["classroom"]
    teacher = data["teacher"]
    # 前端写成title了，先改成这样
    course_name = data["course_title"]
    #course_color = data["course_color"]

    sql = Course.front_id ==front_id and Course.user_email==user_email
    db.session.query(Course).filter(sql).update({"classroom":classroom,"teacher":teacher,"course_name":course_name,"user_email":user_email})
    db.session.commit()

    return {"success":200}

@bp.route('/course/delete',methods=['POST','GET'])
@login_required
def delete_course():
    data = request.get_json()
    front_id = data["course_id"]
    user_email = current_user.user_email
    sql = Course.front_id ==front_id and Course.user_email==user_email
    res = db.session.query(Course).filter(sql).delete()
    db.session.commit()
    db.session.close()

    return {"success":200}

@bp.route('/query_single_course',methods=['POST','GET'])
@login_required
def query_single_course():
    data = request.get_json()
    front_id = data["course_id"]
    user_email = current_user.user_email
    sql = Course.front_id == front_id and Course.user_email == user_email
    single_course = db.session.query(Course).filter(sql)
    #return jsonify({'classroom':single_course.classroom, 'teacher': single_course.teacher, 'course_name':single_course.course_name, 'course_color':single_course.course_color})
    return jsonify({'classroom':single_course.classroom, 'teacher': single_course.teacher, 'course_name':single_course.course_name})


@bp.route('/user_all_course',methods=['POST','GET'])
@login_required
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


@bp.route('/excel_recognition', methods=['GET'])
@login_required
def excel_file_recognition():
    user_email = current_user.user_email
    file_name = request.files.get('file_name')
    fn = file_name.name
    if fn.endswith('.xls'):
        file = file_name.read()
        wb = xlrd.open_workbook(file_contents=file)
        sheet = wb.sheet_by_index(0)
        i = 0
        j = 0
        for row in sheet.get_rows():
            for cell in row:
                if cell.value != '':
                    result = cell.value.split('/')
                    if len(result) == 4:
                        print(j - 2, i - 2, result)
                        course = Course
                j = j + 1
            i = i + 1
            j = 0
    if fn.endswith('.xlsx'):
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


"""@bp.route('/excel_recognition', methods=['GET'])
@login_required
def excel_file_recognition():
    user_email = current_user.user_email
    file_name = request.files.get('file_name')
    fn = file_name.name
    if fn.endswith('.xls'):
        file = file_name.read()
        wb = xlrd.open_workbook(file_contents=file)
        sheet = wb.sheet_by_index(0)
        i = 0
        j = 0
        for row in sheet.get_rows():
            for cell in row:
                if cell.value != '':
                    result = cell.value.split('/')
                    if len(result) == 4:
                        print(j - 2, i - 2, result)
                        course = Course
                j = j + 1
            i = i + 1
            j = 0
    if fn.endswith('.xlsx'):
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
"""
