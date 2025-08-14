from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, NumberRange, TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError

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
    category = IntegerField('Category', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    quatity = IntegerField('Quantity', validators=[DataRequired()])

    # TODO: Add Images from listingimage.py

    