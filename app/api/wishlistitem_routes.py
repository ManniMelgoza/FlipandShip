from flask import Blueprint, jsonify, request
from app.models import Wishlist, Wishlistitem, db
from flask_login import login_required, current_user

wishlistitem_routes = Blueprint('wishlistitems', __name__)

# *********************************
#  GET all items for a wishlist
#**********************************
@wishlistitem_routes.route('/wishlist/<int:wishlist_id>')
@login_required
def get_wishlist_items(wishlist_id):

    wishlist = Wishlist.query.get_or_404(wishlist_id)

    if wishlist.owner_id != current_user.id:
        return {"Message": 'You are not authorized to add this item'}, 403

    items = [item.to_dict() for item in wishlist.wishlistitems]
    return items, 200

# *********************************
#  POST Items Added to  wishlist
#**********************************
@wishlistitem_routes.route('/', methods=['POST'])
@login_required
def add_items_wishlist():
    data_req = request.get_json()
    wishlist_id = data_req.get('wishlist_id')
    listing_id = data_req.get('listing_id')

    if not wishlist_id or not listing_id:
        return {'Message': 'wishlist_id and listing_id are required'}, 400

    wishlist = Wishlist.query.get(wishlist_id)

    if not wishlist:
        return {'Message': 'Wishlist Not Found'}, 404

    if wishlist.owner_id != current_user.id:
        return {'Message': 'Unauthorized access'}, 403

    existing_item = Wishlistitem.query.filter_by(
        wishlist_id=wishlist_id, listing_id=listing_id
    ).first()

    if existing_item:
        return {'Message': 'Item already added to your wishlist.'}

    item = Wishlistitem(wishlist_id=wishlist_id, listing_id=listing_id)
    db.session.add(item)
    db.session.commit()

    return item.to_dict()

# *********************************
#  DELETE Item from wishlist
#**********************************
@wishlistitem_routes.route('/<int:item_id>', methods=['DELETE'])
@login_required
def delete_item(item_id):

    item = Wishlistitem.query.get(item_id)

    if not item:
        return {'Message': 'Item Not Found'}, 404

    if item.wishlist.owner_id != current_user.id:
        return {"Message": 'You are not authorized to delete items from this wishlist'}, 403

    wishlist_title = item.wishlist.title

    db.session.delete(item)
    db.session.commit()
    return {'Message': f'Item has been removed from wishlist {wishlist_title}'}, 200
