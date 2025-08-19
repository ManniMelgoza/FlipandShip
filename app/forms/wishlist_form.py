from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, NumberRange, Length

class WishlistForm(FlaskForm):
    title = StringField('Wishlist Title', validators=[DataRequired()])
