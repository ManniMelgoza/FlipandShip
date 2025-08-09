from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Wishlist(db.Model, TimeStampMixin):
    __tablename__= 'wishlists'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)


# Relationships

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id
        }
