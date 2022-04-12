import wtforms
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import length, DataRequired, EqualTo, email, Length
from models import EmailCaptchaModel,User


class LoginFrom(wtforms.Form):
    user_email = wtforms.StringField(validators=[email()])
    user_password = wtforms.StringField(validators=[length(min=3, max=20)])

    # def validate_user_password(self,field):
    #     user_password = field.data
    #     user_email = self.user_email.data
    #     user_model = User.query.filter_by(user_email=user_email).first()
    #     if not user_model and user_model.user_password != user_password:
    #         raise wtforms.ValidationError("密码错误")


class RegisterForm(wtforms.Form):
    user_email = wtforms.StringField(validators=[DataRequired("邮箱不能为空"), email()])
    user_name = wtforms.StringField(validators=[DataRequired("用户名不能为空"), length(min=3, max=20)])
    user_password = wtforms.StringField(validators=[DataRequired("密码不能为空"), length(min=3, max=20)])
    confirm = wtforms.StringField(validators=[EqualTo('user_password')])
    captcha = wtforms.StringField(validators=[length(min=6, max=6)])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.user_email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model and captcha_model.captcha.lower() != captcha:
            raise wtforms.ValidationError("验证码错误")

    def validate_user_email(self, field):
        email = field.data
        user_model = User.query.filter_by(user_email=email).first()
        if user_model:
            raise wtforms.ValidationError("邮箱已注册")

class EditProfileForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    about_me=TextAreaField('About_me',validators=[Length(min=0,max=140)])
    submit=SubmitField('Submit')

class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[DataRequired("title cannot be empty"), length(min=3, max=50)])
    content = wtforms.StringField(validators=[DataRequired("content cannot be empty"), length(min=5, max=200)])

class ForgetFormEmail(wtforms.Form):
    user_email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=6, max=6)])

    def validate_user_email(self, field):
        email = field.data
        user_model = User.query.filter_by(user_email=email).first()
        if not user_model:
            raise wtforms.ValidationError("邮箱未注册")

    def validate_captcha(self, field):
        captcha = field.data
        email = self.user_email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model and captcha_model.captcha.lower() != captcha:
            raise wtforms.ValidationError("验证码错误")


class ForgetFormPassword(wtforms.Form):
    user_password = wtforms.StringField(validators=[DataRequired("密码不能为空"), length(min=3, max=20)])
    confirm = wtforms.StringField(validators=[EqualTo('user_password')])