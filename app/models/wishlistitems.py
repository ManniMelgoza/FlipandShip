from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin


class Wishlistitem(db.Model, TimeStampMixin):
    __tablename__ = 'wishlistitems'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    wishlist_id = db.Column(db.Integer, nullable=False)
    listing_id = db.Column(db.Integer, nullable=False)

# Relationships

    def to_dict(self):
        return {
            'id': self.id,
            'wishlist_id': self.wishlist_id,
            'listing_id': self.listing_id
        }
