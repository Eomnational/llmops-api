from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionReq(FlaskForm):
    # 必填 长度最大为2000
    query = StringField("query", validators=[
        DataRequired(message="用户问题不能为空"),
        Length(max=2000, message="用户的提问最大长度是2000"),
    ])
