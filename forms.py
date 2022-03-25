import wtforms
from wtforms.validators import length,DataRequired,EqualTo,email
from models import EmailCaptchaModel

class LoginFrom(wtforms.Form):
    # user_name = wtforms.StringField(validators=[length(min=3,max=20)])
    user_email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=3,max=20)])

    def validate_password(self,field):

        pass


class RegisterForm(wtforms.Form):
    user_email = wtforms.StringField(validators=[DataRequired("邮箱不能为空"), email()])
    user_name = wtforms.StringField(validators=[DataRequired("用户名不能为空"), length(min=3, max=20)])
    user_password = wtforms.StringField(validators=[DataRequired("密码不能为空"), length(min=3, max=20), EqualTo('confirm')])
    confirm = wtforms.StringField()
    captcha = wtforms.StringField(validators=[length(min=6,max=6)])

    def validate_captcha(self, field):
        captcha = field.data
        email = self.user_email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not captcha_model and captcha_model.captcha.lower() != captcha:
            raise wtforms.ValidationError("验证码错误")

    def validate_user_email(self,field):
        email = self.user_email.data
        user_model = EmailCaptchaModel.query.filter_by(email=email).first
        if user_model:
            raise wtforms.ValidationError("邮箱已注册")


