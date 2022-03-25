from flask import Blueprint

bp = Blueprint("Page",__name__,url_prefix="/")

@bp.route("/")
def login():
    return "论坛首页"

