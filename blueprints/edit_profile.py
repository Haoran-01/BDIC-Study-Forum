from flask import Blueprint, redirect, url_for, render_template
from sqlalchemy.sql.functions import current_user

import app
from forms import EditProfileForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired,ValidationError,Email,EqualTo,Length
from exts import db
from flask import request,session
from flask import flash
from models import User,UserProfile
from flask_login import login_required


bp = Blueprint("userprofile",__name__,url_prefix="/")

"""@bp.route('/user/<user_email>')
@login_required
def user(user_email):
    user = User.query.filter_by(user_email = user_email).first_or_404()

    # posts=[
    #     {'author':user,'body':'Test post #1'},
    #     {'author':user,'body':'Test post #2'}
    # ]
    return render_template('user.html',user_email = session.get("user_email"))"""



@bp.route('/profile',methods=['GET','POST'])
#@login_required
def edit_profile():
    #print('begin edit')

    user_name=request.form["UserName"]
    introduction=request.form["Introduction"]
    user_email = request.form["E-mail"]
    grade=request.form["Grade"]
    department =request.form["Department"]
    #major=request.get()

    #userprofile = UserProfile(user_name="SQ",introduction="aaaaa",user_email="d1@dfa",grade=2020,department="BDIC",major="SE")
    userprofile = UserProfile(user_name,introduction,user_email,grade,department)

    db.session.add(userprofile)
    db.session.commit()
    return "successfully"


""" form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()

        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)"""