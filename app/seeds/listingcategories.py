from app.models import db, Listingcategory, environment, SCHEMA
from sqlalchemy.sql import text


def seed_listingcategories():
    categories = [
        Listingcategory(category_type='Electronics'),                  # 1
        Listingcategory(category_type='Clothing & Accessories'),       # 2
        Listingcategory(category_type='Home & Garden'),                # 3
        Listingcategory(category_type='Sports & Outdoors'),            # 4
        Listingcategory(category_type='Books & Media'),                # 5
        Listingcategory(category_type='Toys & Games'),                 # 6
        Listingcategory(category_type='Automotive'),                   # 7
        Listingcategory(category_type='Health & Beauty'),              # 8
        Listingcategory(category_type='Jewelry & Watches'),            # 9
        Listingcategory(category_type='Collectibles & Antiques'),      # 10
        Listingcategory(category_type='Art & Crafts'),                 # 11
        Listingcategory(category_type='Musical Instruments'),          # 12
        Listingcategory(category_type='Pet Supplies'),                 # 13
        Listingcategory(category_type='Baby & Kids'),                  # 14
        Listingcategory(category_type='Office'),                       # 15
        Listingcategory(category_type='Tools & Hardware/Industrial'),  # 16
        Listingcategory(category_type='Photography & Video'),          # 17
        Listingcategory(category_type='Travel & Luggage'),             # 18
        Listingcategory(category_type='Furniture'),                    # 19
        Listingcategory(category_type='Other')                         # 20
    ]

    for category in categories:
        db.session.add(category)
    db.session.commit()

def undo_listingcategories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.listingcategories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM listingcategories"))

    db.session.commit()
