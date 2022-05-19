from flask import Blueprint, request, jsonify
from models import Administrator
from exts import db
from flask_login import login_required, current_user

bp = Blueprint("administrator", __name__, url_prefix="/adm")

@bp.route('/get_all_problems', methods=['GET'])
def get_all_problems():
    return