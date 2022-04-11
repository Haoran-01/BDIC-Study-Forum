from flask import Blueprint, request, render_template
from forms import QuestionForm

bp = Blueprint("forum", __name__, url_prefix="/")

@bp.route("/", method=['GET', 'POST'])
def forum_index():
    if request.method == 'GET':
        return render_template("forum.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data;
            content = form.content.data;



