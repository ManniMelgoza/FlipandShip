from app.models import db, Wishlist, environment, SCHEMA
from sqlalchemy.sql import text


def seed_wishlists():

    wishlists = [

        # User 1 wishlist (Demo)
        Wishlist(title='Tools', owner_id=1),
        Wishlist(title='Photography', owner_id=1),
        Wishlist(title='Home Electronics', owner_id=1),

        # User 2 wishlist (Manni)
        Wishlist(title='Bikes', owner_id=2),
        Wishlist(title='Power Tools', owner_id=2),
        Wishlist(title='Kitchen Appliances', owner_id=2),

        # User 3 wishlist (Bobbie)
        Wishlist(title='Power Tools', owner_id=3),
        Wishlist(title='Fashion & Accessories', owner_id=3),
        Wishlist(title='Industrial Equipment', owner_id=3),

        # User 4 wishlist (Alex)
        Wishlist(title='Power Tools', owner_id=4),
        Wishlist(title='Furnature&Appliances', owner_id=4),

        # User 5 wishlist (Sophia)
        Wishlist(title='Kitchen Appliances', owner_id=5),
        Wishlist(title='Power Tools', owner_id=5),
        Wishlist(title='Electronics', owner_id=5),

        # User 6 wishlist (James)
        Wishlist(title='Audio & Music', owner_id=6),
        Wishlist(title='Vintage Items', owner_id=6),
        Wishlist(title='Sports & Outdoors', owner_id=6),

        # User 7 wishlist (Linda)
        Wishlist(title='Kitchen Appliances', owner_id=7),
        Wishlist(title='Office Furniture', owner_id=7),
        Wishlist(title='Yard Tools', owner_id=7),

        # User 8 wishlist (Michael)
        Wishlist(title='Audio & Music', owner_id=8),
        Wishlist(title='Power Tools', owner_id=8),
        Wishlist(title='Camping Gear', owner_id=8),

        # User 9 wishlist (Natalie)
        Wishlist(title='Gaming Gear & Sports', owner_id=9),
        Wishlist(title='Winter Sports', owner_id=9),
        Wishlist(title='Travel Gear', owner_id=9),

        # User 10 wishlist (Ryan)
        Wishlist(title='Coffee & Kitchen', owner_id=10),
        Wishlist(title='Musical Instruments', owner_id=10),
        Wishlist(title='Home Furniture', owner_id=10),
    ]

    for list in wishlists:
        db.session.add(list)
    db.session.commit()


def undo_wishlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.wishlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM wishlists"))

    db.session.commit()
