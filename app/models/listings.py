from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin


class Listing(db.Model, TimeStampMixin):
    __tablename__ = 'listings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    descrition = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.Integer, nullable=False, unique=True)
    brand = db.Column(db.String(255), nullable=False)
    color = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# RELATIONSHIPS


    def to_dict(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'title': self.title,
            'price': self.price,
            'condition': self.condition,
            'description': self.descrition,
            'location': self.location,
            'catagory': self.category,
            'brand': self.brand,
            'color': self.color,
            'quantity': self.quantity
        }
