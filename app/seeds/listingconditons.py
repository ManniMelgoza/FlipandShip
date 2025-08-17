from app.models import db, Listingcondition, environment, SCHEMA
from sqlalchemy.sql import text


def seed_listingconditions():
    conditions = [
        Listingcondition(condition_type='New'),          # 1
        Listingcondition(condition_type='Open-Box'),     # 2
        Listingcondition(condition_type='Refurbished'),  # 3
        Listingcondition(condition_type='Used'),         # 4
        Listingcondition(condition_type='Like-New'),     # 5
        Listingcondition(condition_type='Free'),         # 6

    ]

    for condition in conditions:
        db.session.add(condition)
    db.session.commit()

def undo_listingconditions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.listingconditions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM listingconditions"))

    db.session.commit()
