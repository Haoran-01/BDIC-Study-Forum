from flask import Blueprint, request, jsonify
from models import Course, Classroom

bp = Blueprint("search_empty_class", __name__, url_prefix="/search_empty_class")


@bp.route("/time_view", methods=['POST','GET'])
def time_view():
    data = request.get_json(silent=True)
    floor = data['floor']
    date = data['date']
    classroom_number_range = range(floor*100, floor*100+30)
    data_list = []
    for i in classroom_number_range:
        courses = Classroom.query.filter(Classroom.courses).all()
        today_courses = []
        dic = {
            "class_room_number" : i,
            "first_class": "empty",
            "second_class": "empty",
            "third_class": "empty",
            "fourth_class": "empty",
            "fifth_class": "empty",
            "sixth_class": "empty"
        }
        for j in courses:
            if j.x == date:
                today_courses.append(j)
        for k in today_courses:
            if k.y == 0:
                dic["first_class"] = "full"
            elif k.y == 1:
                dic["second_class"] = "full"
            elif k.y == 2:
                dic["third_class"] = "full"
            elif k.y == 3:
                dic["fourth_class"] = "full"
            elif k.y == 4:
                dic["fifth_class"] = "full"
            elif k.y == 5:
                dic["sixth_class"] = "full"
        data_list.append(dic)
    return jsonify(data=data_list), 200

