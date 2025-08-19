from flask import Blueprint, jsonify, request
from app.models import Wishlist, Wishlistitem, db
from flask_login import login_required, current_user
from app.forms import WishlistForm

wishlist_routes = Blueprint('wishlists', __name__)

# *********************************
#   GET all Users wishlists
#**********************************
@wishlist_routes.route('/')
@login_required
def get_users_wishlists():

    wishlists = Wishlist.query.filter_by(owner_id=current_user.id).all()
    return {'Wishlists': [wishlist.to_dict() for wishlist in wishlists]}

# *********************************
#   GET single wishlist by id
#**********************************
@wishlist_routes.route('/<int:wishlist_id>')
@login_required
def get_wishlist(wishlist_id):

    wishlist = Wishlist.query.get(wishlist_id)

    if not wishlist:
        return {'Message': 'Wishlist Not Found'}, 404

    if wishlist.owner_id != current_user.id:
        return {"Message": 'Unauthorized access'}, 403

    wishlist_items = wishlist.to_dict()
    wishlist_items['items'] = [item.to_dict() for item in wishlist.wishlistitems]
    return wishlist_items, 200

# *********************************
#   GET New Wishlist
#**********************************
@wishlist_routes.route('/', methods=['POST'])
@login_required
def create_wishlist():

    data_req = request.get_json()
    title = data_req.get('title')

    if not title:
        return {'Message': 'Title is required'}, 400

    new_wishlist = Wishlist(
        title = title,
        owner_id = current_user.id
    )
    db.session.add(new_wishlist)
    db.session.commit()

    return new_wishlist.to_dict(), 201

# *********************************
#   DELETE Wishlist
#**********************************
@wishlist_routes.route('/<int:wishlist_id>', methods=['DELETE'])
@login_required
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)

    if not wishlist:
        return {"Message": "Wishlist was not found"}, 404
    if  wishlist.owner_id != current_user.id:
        return {"Message": "You are not authorized to DELETE this wishlist"}, 403

    db.session.delete(wishlist)
    db.session.commit()
    return {'Message': 'Wishlist deleted successfully'}, 200

# *********************************
#   PUT EDIT Wishlist TITLE
#**********************************
@wishlist_routes.route('/<int:wishlist_id>/edit', methods=['PUT'])
@wishlist_routes.route('/<int:wishlist_id>/edit', methods=['PUT'])
@login_required
def edit_wishlist(wishlist_id):
    wishlist = Wishlist.query.get(wishlist_id)

    if not wishlist:
        return {"Message": "Wishlist was not found"}, 404
    if  wishlist.owner_id != current_user.id:
        return {"Message": "You are not authorized to DELETE this wishlist"}, 403

    wishlist_form = WishlistForm(obj=wishlist)

    wishlist_form['csrf_token'].data = request.cookies.get('csrf_token')

    if wishlist_form.validate_on_submit():

        wishlist.title=wishlist_form.data['title']

        db.session.commit()
        return wishlist.to_dict(), 200
    return {'Errors': wishlist_form.errors}, 400
