from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[InputRequired()])
    content = TextAreaField('Nội dung', validators=[InputRequired()])
    submit = SubmitField('Đăng bài')
