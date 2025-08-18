from flask.cli import AppGroup
from .users import seed_users, undo_users
from .follows import seed_follows, undo_follows
from .listings import seed_listings, undo_listings
from .listingimages import seed_listingimages, undo_listingimages
from .comments import seed_comments, undo_comments
from .reviews import seed_reviews, undo_reviews
from .wishlistitems import seed_wishlistitems, undo_wishlistitems
from .wishlists import seed_wishlists, undo_wishlists
from .listingcategories import seed_listingcategories, undo_listingcategories
from .listingconditons import seed_listingconditions, undo_listingconditions

from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_users()
        undo_follows()
        undo_listings()
        undo_listingimages()
        undo_comments()
        undo_reviews()
        undo_wishlistitems()
        undo_wishlists()
        undo_listingcategories()
        undo_listingconditions()


    # Add other seed functions here
    seed_users()
    seed_follows()
    seed_listings()
    seed_listingimages()
    seed_comments()
    seed_reviews()
    seed_wishlistitems()
    seed_wishlists()
    seed_listingcategories()
    seed_listingconditions()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    # Add other undo functions here
    undo_users()
    undo_follows()
    undo_listings()
    undo_listingimages()
    undo_comments()
    undo_reviews()
    undo_wishlistitems()
    undo_wishlists()
    undo_listingcategories()
    undo_listingconditions()
