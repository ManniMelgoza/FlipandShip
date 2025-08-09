# LOOKUP TABLE
from ..db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from ..timestampmixin import TimeStampMixin


class Listingcondition(db.Model, TimeStampMixin):
    __tablename__ = 'listingconditions'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    condition_type = db.Column(db.String, nullable=False)

# Relationships
    listings = db.relationship('Listing', back_populates='condition')

    def to_dict(self):
        return {
            'id': self.id,
            'condition_type': self.condition_type
        }
