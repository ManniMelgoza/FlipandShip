from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin
from .listingimage import Listingimage

class Listing(db.Model, TimeStampMixin):
    __tablename__ = 'listings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    item_title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# LookUp Tables connection
    condition_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('listingconditions.id')),
        nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod('listingcategories.id')),
        nullable=False)

# RELATIONSHIPS
    owner = db.relationship('User', back_populates = 'listings')
    condition = db.relationship('Listingcondition', back_populates = 'listings')
    category = db.relationship('Listingcategory', back_populates = 'listings')
    wishlistitems = db.relationship('Wishlistitem', back_populates = 'listing', cascade="all, delete-orphan")
    listing_images = db.relationship('Listingimage', back_populates='listing', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'item_title': self.item_title,
            'price': str(self.price),
            'description': self.description,
            'location': self.location,
            'brand': self.brand,
            'color': self.color,
            'quantity': self.quantity,
            'condition': self.condition.to_dict() if self.condition else None,
            'category': self.category.to_dict() if self.category else None,
            'images': [
                {
                    'id': img.id,
                    'url': img.listing_img,
                    'is_main':img.is_main
                }
                for img in self.listing_images
            ]
        }
