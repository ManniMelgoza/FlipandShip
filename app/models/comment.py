from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin


class Comment(db.Model, TimeStampMixin):
    __tablename__ = 'comments'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('listings.id')), nullable=False)
    comment_body = db.Column(db.String, nullable=False)

# Relationships
    user = db.relationship('User', back_populates='comments')

def to_dict(self):
    return {
        'id': self.id,
        'user_id': self.user_id,
        'listing_id': self.listing_id,
        'comment_body': self.comment_body
    }
