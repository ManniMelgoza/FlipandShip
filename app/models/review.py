from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Review(db.Model, TimeStampMixin):
    __tablename__ = 'reviews'

    if environment == 'production':
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    reviewer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    reviewed_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_body = db.Column(db.String, nullable=False)

# RELATIONSHIPS
    reviewer = db.relationship('User', foreign_keys=[reviewer_id], back_populates='reviews_given_by_user')
    reviewed = db.relationship('User', foreign_keys=[reviewed_id], back_populates='review_given_by_other_users')

    def to_dict(self):
        return {
            'id': self.id,
            'reviewer_id': self.reviewer_id,
            'reviewed_id': self.reviewed_id,
            'rating': self.rating,
            'review_body': self.review_body
        }
