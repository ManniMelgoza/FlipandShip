from flask import Blueprint, jsonify, request
from app.models import Listing, db
from app.forms import  ListingForm
from flask_login import login_required, current_user


listing_routes = Blueprint('listings', __name__)

# *********************************
#   GET All Listingss Route Homepage
#**********************************
@listing_routes.route('/')
def all_listings():
    listings = Listing.query.all()
    return {'Listings': [listings.to_dict() for item in listings]}

# ***************************************
#   POST Create NEW Listing
#****************************************
@listing_routes.route('/products')
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
            quantity = listing.data['quantity']
        )
        db.session.add(create_listing)
        db.session.commit()
        return create_listing.to_dict(), 201
    return listing.errors, 400


# ***************************************
#   GET Current User's Posts Route
#****************************************
# @listing_routes.route('/<int:user_id>')
