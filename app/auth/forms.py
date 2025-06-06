from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        InputRequired(message='Vui lòng nhập tên đăng nhập'),
        Length(min=4, max=25, message='Tên đăng nhập phải từ 4-25 ký tự')
    ])
    password = PasswordField('Mật khẩu', validators=[
        InputRequired(message='Vui lòng nhập mật khẩu')
    ])
    submit = SubmitField('Đăng nhập')


class RegisterForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        InputRequired(message='Vui lòng nhập tên đăng nhập'),
        Length(min=4, max=25, message='Tên đăng nhập phải từ 4-25 ký tự')
    ])
    password = PasswordField('Mật khẩu', validators=[
        InputRequired(message='Vui lòng nhập mật khẩu'),
        Length(min=6, message='Mật khẩu phải ít nhất 6 ký tự')
    ])
    confirm = PasswordField('Xác nhận mật khẩu', validators=[
        InputRequired(message='Vui lòng xác nhận mật khẩu'),
        EqualTo('password', message='Mật khẩu không khớp')
    ])
    submit = SubmitField('Đăng ký')
