from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, NumberRange, Length
from wtforms.validators import DataRequired, ValidationError

class ReviewForm(FlaskForm):
    rating = IntegerField(
        'Review Star Rating',
        validators=[DataRequired(),
        NumberRange(min=0, max=5)
    ])
    review_body = TextAreaField('Leave a review message here...', validators=[DataRequired(), Length(max=255, message='Review must be less than 255 characters')])
