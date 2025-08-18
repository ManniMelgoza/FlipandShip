from flask import Blueprint, jsonify, request
from app.models import Wishlist, Wishlistitem, db
from flask_login import login_required, current_user

wishlist_routes = Blueprint('wishlists', __name__)


# *********************************
#   GET all Users wishlists
#**********************************
@wishlist_routes.route('/')
@login_required
def get_users_wishlists():

    wishlists = Wishlist.query.filter_by(owner_id=current_user.id).all()
    return {'Wishlists': [list.to_dixt() for list in wishlists]}

# *********************************
#   GET single wishlist by id
#**********************************
@wishlist_routes.route('/<int:wishlist_id>')
@login_required
def get_wishlist(wishlist_id):

    wishlist = Wishlist.query.get(wishlist_id)

    if wishlist.owner_id != current_user.id:
        return {"Message": 'Unauthorized access'}, 403

    wishlist_items = wishlist.to_dict()
