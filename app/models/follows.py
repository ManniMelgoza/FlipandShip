from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from .timestampmixin import TimeStampMixin

class Follow(db.Model, TimeStampMixin):
    __tablename__ = 'follows'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primery_key=True)
    follower_id = db.Column(db.Integer, (add_prefix_for_prod('users.id')), nullable=False)
    following_id = db.Column(db.Integer, (add_prefix_for_prod('users.id')), nullable=False)

# Relationships

def to_dict(self):
    return {
        'id': self.id,
        'follower_id': self.follower.id,
        'following_id': self.following_id
    }


