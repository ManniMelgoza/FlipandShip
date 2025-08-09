from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Review(db.Modal, TimeStampMixin):
    __tablename__ = 'reviews'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    reviewed_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_body = db.Column(db.String, nullable=False)

# RELATIONSHIPS

    def to_dict(self):
        return {
            'id': self.id,
            'rating': self.rating,
            'review_body': self.review_body
        }
