from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[InputRequired()])
    password = PasswordField('Mật khẩu', validators=[InputRequired()])
    submit = SubmitField('Đăng nhập')

class RegisterForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('Mật khẩu', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Đăng ký')
