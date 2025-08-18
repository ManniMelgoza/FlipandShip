from flask import Blueprint, jsonify, request
from app.models import Listing, Comment, Listingimage, db, Listingcategory, Listingcondition
from app.forms import  ListingForm, CommentForm
from flask_login import login_required, current_user


listing_routes = Blueprint('listings', __name__)

# *********************************
#   GET All Listingss Route Homepage
#**********************************
@listing_routes.route('/')
def all_listings():
    listings = Listing.query.all()
    return {'Listings': [item.to_dict() for item in listings]}

# *********************************
#   GET Single Listings
#**********************************
@listing_routes.route('/<int:listing_id>')
def single_listing(listing_id):
    listing = Listing.query.get(listing_id)

    if not listing:
        return {"Mesasge": 'Listing was Not Found'}, 404

    return listing.to_dict(), 200

# ***************************************
#   POST Create NEW Listing
#****************************************
@listing_routes.route('/', methods=['POST'])
@login_required
def create_listing():
    listing = ListingForm()
    listing['csrf_token'].data = request.cookies['csrf_token']

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

        if listing.data.get('listing_img1'):
            main_image = Listingimage(
                listing_id=create_listing.id,
                listing_img=listing.data['listing_img1'],
                is_main=True
            )
            db.session.add(main_image)
        if listing.data.get("listing_img2"):
            img2 = Listingimage(
                listing_id=create_listing.id,
                listing_img=listing.data["listing_img2"],
                is_main=False
            )
            db.session.add(img2)

        if listing.data.get("listing_img3"):
            img3 = Listingimage(
                listing_id=create_listing.id,
                listing_img=listing.data["listing_img3"],
                is_main=False
            )
            db.session.add(img3)

        if listing.data.get("listing_img4"):
            img4 = Listingimage(
                listing_id=create_listing.id,
                listing_img=listing.data["listing_img4"],
                is_main=False
            )
            db.session.add(img4)

        if listing.data.get("listing_img5"):
            img5 = Listingimage(
                listing_id=create_listing.id,
                listing_img=listing.data["listing_img5"],
                is_main=False
            )
            db.session.add(img5)
        db.session.commit()

        return create_listing.to_dict(), 201
    return {'Errors': listing.errors}, 400

# ***************************************
#   GET categories for dropdown
#****************************************
@listing_routes.route('/categories')
def get_categories():
    categories = Listingcategory.query.all()
    return {'Categories': [category.to_dict() for category in categories]}

# ***************************************
#   GET Condition for dropdown
#****************************************
@listing_routes.route('/conditions')
def get_conditions():
    conditions =Listingcondition.query.all()
    return {'Conditions': [condition.to_dict() for condition in conditions]}

# ***************************************
#   GET ALL Current User's Posts Route
#****************************************
@listing_routes.route('/current')
@login_required
def get_current_user_listings():
    user_listings = Listing.query.filter_by(owner_id=current_user.id).all()
    return {'Listings': [item.to_dict() for item in user_listings]}

# ***************************************
#   PUT Edit Listing
#****************************************
@listing_routes.route('/<int:listing_id>/edit', methods=['PUT'])
@login_required
def edit_listing(listing_id):
    listing_edit = Listing.query.get(listing_id)

    if not listing_edit:
        return {"Message": 'This listing does not exits'}, 404

    if listing_edit.owner_id != current_user.id:
        return {"Message": 'You are not authorized to edit this listing'}, 403

    edit_form = ListingForm(obj=listing_edit)

    edit_form['csrf_token'].data = request.cookies['csrf_token']

    if edit_form.validate_on_submit():

        listing_edit.item_title=edit_form.data['item_title']
        listing_edit.price=edit_form.data['price']
        listing_edit.description=edit_form.data['description']
        listing_edit.location=edit_form.data['location']
        listing_edit.brand=edit_form.data['brand']
        listing_edit.color=edit_form.data['color']
        listing_edit.quantity=edit_form.data['quantity']
        listing_edit.condition_id=edit_form.data['condition']
        listing_edit.category_id=edit_form.data['category']

        db.session.commit()
        return listing_edit.to_dict(), 200
    return {'Errors': edit_form.errors}, 400

# *********************************
#  DELETE Listing Route
#**********************************
@listing_routes.route('/<int:listing_id>', methods=['DELETE'])
@login_required
def delete_listings(listing_id):
    listing_delete = Listing.query.get(listing_id)

    if not listing_delete:
        return {"Message": "Listing was not found"}, 404
    if listing_delete.owner_id != current_user.id:
        return {"Message": "You are not authorized to DELETE this listing"}, 403

    db.session.delete(listing_delete)
    db.session.commit()
    return {"Message": 'Your listing was DELETED'}, 200

# *************************************************************************************************************************
#   COMMENTS ROUTES BELOW   COMMENTS ROUTES BELOW   COMMENTS ROUTES BELOW   COMMENTS ROUTES BELOW   COMMENTS ROUTES BELOW
#**************************************************************************************************************************

# *********************************
#   GET All Comments per Listing
#**********************************
@listing_routes.route('/<int:listing_id>/comments')
def all_comments(listing_id):
    # listing_id=listing_id (table_column=actual route variable)
    comments = Comment.query.filter_by(listing_id=listing_id).all()

    return {'Comments': [comment.to_dict() for comment in comments]}

# **************************************
#   POST Create NEW Comment to listing
#***************************************
@listing_routes.route('/<int:listing_id>/comments', methods=['POST'])
@login_required

def create_comment(listing_id):
    comment = CommentForm()
    comment['csrf_token'].data = request.cookies['csrf_token']

    if comment.validate_on_submit():
        create_comment = Comment(
            comment_body = comment.data['comment_body'],
            user_id=current_user.id,
            listing_id=listing_id
        )

        db.session.add(create_comment)
        db.session.commit()
        return create_comment.to_dict(), 201
    return comment.errors, 400
