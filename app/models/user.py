from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

# Relationships
    listings = db.relationship('Listing', back_populates='owner', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='user')
    wishlists = db.relationship('Wishlist', foreign_keys='Wishlist.owner_id', back_populates='owner', cascade='all, delete-orphan')
    # All the reviews the user has given to others
    reviews_given_by_user = db.relationship('Review', foreign_keys='Review.reviewer_id', back_populates='reviewer', cascade='all, delete-orphan')
    # ALl the reviews that user has received
    review_given_by_other_users = db.relationship('Review', foreign_keys='Review.reviewed_id', back_populates='reviewed', cascade='all, delete-orphan')

    follower_by_user = db.relationship('Follow', foreign_keys='Follow.follower_id', back_populates='follower', cascade='all, delete-orphan')
    following_by_user = db.relationship('Follow', foreign_keys='Follow.following_id', back_populates='following', cascade='all, delete-orphan')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
