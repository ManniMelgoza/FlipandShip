from app.models import db, Follow, environment, SCHEMA
from sqlalchemy.sql import text


def seed_follows():

    follows = [
        # User 1 follows 2, 3, 4
        Follow(follower_id=1, following_id=2),
        Follow(follower_id=1, following_id=3),
        Follow(follower_id=1, following_id=4),

        # User 2 follows 3, 5, 6
        Follow(follower_id=2, following_id=3),
        Follow(follower_id=2, following_id=5),
        Follow(follower_id=2, following_id=6),

        # User 3 follows 4, 7, 8
        Follow(follower_id=3, following_id=4),
        Follow(follower_id=3, following_id=7),
        Follow(follower_id=3, following_id=8),

        # User 4 follows 5, 9, 10
        Follow(follower_id=4, following_id=5),
        Follow(follower_id=4, following_id=9),
        Follow(follower_id=4, following_id=10),

        # User 5 follows 1, 6, 7
        Follow(follower_id=5, following_id=1),
        Follow(follower_id=5, following_id=6),
        Follow(follower_id=5, following_id=7),

        # User 6 follows 2, 8, 9
        Follow(follower_id=6, following_id=2),
        Follow(follower_id=6, following_id=8),
        Follow(follower_id=6, following_id=9),

        # User 7 follows 3, 10, 1
        Follow(follower_id=7, following_id=3),
        Follow(follower_id=7, following_id=10),
        Follow(follower_id=7, following_id=1),

        # User 8 follows 4, 2, 5
        Follow(follower_id=8, following_id=4),
        Follow(follower_id=8, following_id=2),
        Follow(follower_id=8, following_id=5),

        # User 9 follows 6, 3, 1
        Follow(follower_id=9, following_id=6),
        Follow(follower_id=9, following_id=3),
        Follow(follower_id=9, following_id=1),

        # User 10 follows 7, 8, 2
        Follow(follower_id=10, following_id=7),
        Follow(follower_id=10, following_id=8),
        Follow(follower_id=10, following_id=2),
    ]

    for follow in follows:
        db.session.add(follow)
    db.session.commit()

def undo_follows():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.follows RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM follows"))

    db.session.commit()
