from flask import Blueprint, redirect, url_for, render_template
from sqlalchemy.sql.functions import current_user
from forms import EditProfileForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from exts import db
from flask import request
from flask import flash


bp = Blueprint("edit_profile",__name__,url_prefix="/")


@bp.route('/edit_profile',methods=['GET','POST'])

def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()

        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)