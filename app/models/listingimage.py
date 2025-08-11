from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Listingimage(db.Model, TimeStampMixin):
    __tablename__ = 'listingimages'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('listings.id')), nullable=False)
    listing_img = db.Column(db.String(255), nullable=False)

# Relationships
    listing = db.relationship("Listing", back_populates='listing_images')

    def to_dict(self):
        return{
            'id': self.id,
            'listing_id': self.listing_id,
            'listing_img': self.listing_img
        }
