import wtforms
from wtforms.validators import length,DataRequired,EqualTo,email

class LoginFrom(wtforms.Form):
    user_name = wtforms.StringField(validators=[length(min=3,max=20)])
    password = wtforms.StringField(validators=[length(min=3,max=20)])

class RegistForm(wtforms.Form):
    user_email = wtforms.StringField(validators=[DataRequired("邮箱不能为空"), email()])
    user_name = wtforms.StringField(validators=[DataRequired("用户名不能为空"), length(min=3, max=20)])
    password = wtforms.StringField(validators=[DataRequired("用户名不能为空"), length(min=8, max=20), EqualTo('confirm')])
    confirm = wtforms.StringField()


