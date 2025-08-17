from flask import Blueprint, jsonify, request
from app.models import Listing, db
from app.models.lookuptables import Listingcategory, Listingcondition
from app.forms import  ListingForm
from flask_login import login_required, current_user


listing_routes = Blueprint('listings', __name__)

# *********************************
#   GET All Listingss Route Homepage
#**********************************
@listing_routes.route('/')
def all_listings():
    listings = Listing.query.all()
    return {'Listings': [item.to_dict() for item in listings]}

# ***************************************
#   POST Create NEW Listing
#****************************************
@listing_routes.route('/', methods=['POST'])
@login_required
def create_listing():
    listing = ListingForm()
    listing['csrf_token'].data = request.cookies['csrf-token']

    if listing.validate_on_submit():
        create_listing = Listing(
            owner_id = current_user.id,
            item_title = listing.data['item_title'],
            price = listing.data['price'],
            description = listing.data['description'],
            location = listing.data['location'],
            brand = listing.data['brand'],
            color = listing.data['color'],
            quantity = listing.data['quantity'],
            category_id = listing.data['category'],
            condition_id = listing.data['condition']
        )
        db.session.add(create_listing)
        db.session.commit()
        return create_listing.to_dict(), 201
    return listing.errors, 400


# ***************************************
#   GET categories for dropdown
#****************************************
@listing_routes.route('/categories')
def get_categories():
    categories = Listingcategory.query.all()
    return {'categories': [category.to_dict() for category in categories]}

# ***************************************
#   GET condition for dropdown
#****************************************
@listing_routes.route('/conditions')
def get_conditions():
    conditions =Listingcondition.query.all()
    return {'conditions': [condition.to_dict() for condition in conditions]}

# ***************************************
#   GET Current User's Posts Route
#****************************************
# @listing_routes.route('/<int:user_id>')
