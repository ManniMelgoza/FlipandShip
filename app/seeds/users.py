from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():

    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='Manni', email='manni@aa.io', password='password')
    bobbie = User(
        username='Bobbie', email='bobbie@aa.io', password='password')
    alex = User(
        username='Alex', email='alex@aa.io', password='password')
    sophia = User(
        username='Sophia', email='sophia@aa.io', password='password')
    james = User(
        username='James', email='james@aa.io', password='password')
    linda = User(
        username='Linda', email='linda@aa.io', password='password')
    michael = User(
        username='Michael', email='michael@aa.io', password='password')
    natalie = User(
        username='Natalie', email='natalie@aa.io', password='password')
    ryan = User(
        username='Ryan', email='ryan@aa.io', password='password')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(alex)
    db.session.add(sophia)
    db.session.add(james)
    db.session.add(linda)
    db.session.add(michael)
    db.session.add(natalie)
    db.session.add(ryan)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
