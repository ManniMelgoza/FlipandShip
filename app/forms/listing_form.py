from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError, URL, Optional, Regexp, NumberRange
# Used for pattern matching and text validation for the https url in the listing_img1
import re

class ListingForm(FlaskForm):
    item_title = StringField('Title', validators=[DataRequired()])
    price = DecimalField(
        'Price',
        places = 2,
        rounding=None,
        validators=[DataRequired(),
        NumberRange(min=0, max=9999.99)
        ])
    condition = SelectField('Condition', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    category = SelectField('Category', coerce=int, validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])

    # IMAGES
    listing_img1 = StringField('Listing Image Main', validators=[
        DataRequired(),
        Regexp(
            r'^https://.+\.(jpg|jpeg|png|gif|webp)(\?.*)?$',
            flags=re.IGNORECASE,
            message='Please enter a valid HTTPS image URL (jpg, jpeg, png, gif, webp)'
        )
        ])
    listing_img2 = StringField("Listing image", validators=[Optional(), URL()])
    listing_img3 = StringField("Listing image", validators=[Optional(), URL()])
    listing_img4 = StringField("Listing image", validators=[Optional(), URL()])
    listing_img5 = StringField("Listing image", validators=[Optional(), URL()])
