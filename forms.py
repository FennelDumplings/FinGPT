from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    comment = TextAreaField('提供企业数据与查询需求', validators=[DataRequired()])
    submit = SubmitField('提交')


