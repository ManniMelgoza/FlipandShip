from flask import Blueprint, jsonify, request
from app.models import User, Review, db
from app.forms import  ReviewForm
from flask_login import login_required, current_user

review_routes = Blueprint('reviews', __name__)

# *********************************
#   GET All Reviews for user
#**********************************
@review_routes.route('/<int:user_id>')
@login_required
def all_reviews(user_id):
    reviews = Review.query.filter_by(reviewed_id=user_id).all()
    return {'Reviews': [review.to_dict() for review in reviews]}, 200

# *********************************
#   GET a SINGLE review
#**********************************
@review_routes.route('/<int:review_id>')
@login_required
def single_review(review_id):
    review = Review.query.get(review_id)

    if not review:
        return {'Message': 'Review was Not Found'}, 404

    return review.to_dict(), 200

# *********************************
#   POST CREATE REVIEW Review
#**********************************
@review_routes.route('/<int:user_id>', methods=['POST'])
@login_required
def create_review(user_id):

    if current_user.id == user_id:
        return {'Message': 'You cannot leave a review for yourself.'}, 403

    review = ReviewForm()
    review['csrf_token'].data = request.cookies['csrf_token']

    if review.validate_on_submit():
        create_review = Review(
            reviewer_id=current_user.id,
            reviewed_id=user_id,
            rating=review.data['rating'],
            review_body=review.data['review_body']
        )

        db.session.add(create_review)
        db.session.commit()
        return create_review.to_dict(), 201
    return review.errors, 400

# *********************************
#   UPDATE Review
#**********************************
@review_routes.route('/<int:review_id>', methods=['PUT'])
@login_required
def update_review(review_id):
    review = Review.query.get(review_id)

    if not review:
        return {'Message': 'Review Not Found'}, 404

    if review.reviewer_id != current_user.id:
        return  {"Message": 'You are not authorized to edit this review'}, 403

    review_form = ReviewForm(obj=review)
    review_form['csrf_token'].data = request.cookies['csrf_token']

    if review_form.validate_on_submit():
        # review.rating = form.rating.data
        # review.review_body = form.review_body.data
        review.rating = review_form.data['rating']
        review.review_body = review_form.data['review_body']

        db.session.commit()
        return review.to_dict(), 200
    return {'Errors': review_form.errors}, 400

# *********************************
#   DELETE Review
#**********************************
@review_routes.route('/<int:review_id>', methods=['DELETE'])
@login_required
def delete_review(review_id):
    review = Review.query.get(review_id)

    if not review:
        return {"Message": "Review was not found"}, 404
    if review.reviewer_id != current_user.id:
        return {"Message": "You are not authorized to DELETE this Review"}, 403

    db.session.delete(review)
    db.session.commit()
    return {'Message': 'Your Review has been deleted'}, 200
