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

    condition = SelectField(
    'Condition',
    choices=[
        (1, 'New'),
        (2, 'Open-Box'),
        (3, 'Refurbished'),
        (4, 'Used'),
        (5, 'Like-New'),
        (6, 'Free')
    ],
    coerce=int,  # ensures data comes back as int
    validators=[DataRequired()])

    category = SelectField(
    'Category',
    choices=[
        (1, 'Electronics'),
        (2, 'Clothing & Accessories'),
        (3, 'Home & Garden'),
        (4, 'Sports & Outdoors'),
        (5, 'Books & Media'),
        (6, 'Toys & Games'),
        (7, 'Automotive'),
        (8, 'Health & Beauty'),
        (9, 'Jewelry & Watches'),
        (10, 'Collectibles & Antiques'),
        (11, 'Art & Crafts'),
        (12, 'Musical Instruments'),
        (13, 'Pet Supplies'),
        (14, 'Baby & Kids'),
        (15, 'Office'),
        (16, 'Tools & Hardware/Industrial'),
        (17, 'Photography & Video'),
        (18, 'Travel & Luggage'),
        (19, 'Furniture'),
        (20, 'Other')
    ],
    coerce=int,  # ensures it maps to your db int FK
    validators=[DataRequired()]) #validators=[DataRequired()]

    location = StringField('Location',validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=1)])

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
