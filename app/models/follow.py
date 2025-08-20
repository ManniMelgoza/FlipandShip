from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Follow(db.Model, TimeStampMixin):
    __tablename__ = 'follows'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)

    # prevent users from follwoing the same user several times
    __table_args__ = (
        db.UniqueConstraint('follower_id', 'following_id', name='unique_follow'),
        # {"schema": SCHEMA} if environment == "production" else {}
    )
# Relationships
    follower = db.relationship('User', foreign_keys='Follow.follower_id', back_populates='follower_by_user')
    following = db.relationship('User', foreign_keys='Follow.following_id', back_populates='following_by_user')


    def to_dict(self):
        return {
            'id': self.id,
            'follower': self.follower.to_dict(),
            'following': self.following.to_dict(),
            'follower_id': self.follower.id,
            'following_id': self.following_id
        }
