from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin


class Listing(db.Model, TimeStampMixin):
    __tablename__ = 'listing'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    listing_title = db.Column(db.String(255), nullable=False,)
