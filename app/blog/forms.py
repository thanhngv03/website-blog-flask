from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed

class PostForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[InputRequired()])
    content = TextAreaField('Nội dung', validators=[InputRequired()])
    image = FileField('Hình ảnh', validators=[
        FileAllowed(['jpg', 'png','jpeg','gif'], 'Chỉ chấp nhận hình ảnh JPG, PNG, JPEG, GIF.')])
    submit = SubmitField('Đăng bài')
