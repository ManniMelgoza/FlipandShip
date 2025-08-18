from flask import Blueprint, jsonify, request
from app.models import Follow, db
from flask_login import login_required, current_user

follow_routes = Blueprint('follows', __name__)

# *********************************
#   GET Followings
#**********************************
@follow_routes.route('/<int:user_id>/following', methods=['GET'])
def get_following(user_id):

    following = Follow.query.filter_by(follower_id=user_id).all()
    return [follow.to_dict() for follow in following], 200

# *********************************
#   GET Followers
#**********************************
@follow_routes.route('/<int:user_id>/followers', methods=['GET'])
def get_followers(user_id):

    followers = Follow.query.filter_by(following_id=user_id).all()
    return [follower.to_dict() for follower in followers], 200

# *********************************
#   POST Follow User
#**********************************
@follow_routes.route('/<int:user_id>/follow', methods=['POST'])
@login_required

def follow_user(user_id):

    follow = request.get_json()
    following_id = follow.get('following_id')

    if not following_id:
        return {'Message': 'following_id is required'}, 400

    if user_id == following_id:
        return {'Message': 'You cannot follow yourself'}, 400

    existing_follow = Follow.query.filter_by(follower_id=user_id, following_id=following_id).first()
    if existing_follow:
        return {'Message': 'You are already following this user'}, 400

    new_follow = Follow(follower_id=user_id, following_id=following_id)
    db.session.add(new_follow)
    db.session.commit()

    return new_follow.to_dict(), 201

# *********************************
#   DELETE Un-Follow User
#**********************************
@follow_routes.route('/<int:user_id>/unfollow', methods=['DELETE'])
@login_required
def unfollow_user(user_id):
    unfollow = request.get_json()
    following_id = unfollow.get('following_id')

    follow = Follow.query.filter_by(follower_id=user_id, following_id=following_id).first()
    if not follow:
        return {'Message': 'Not following this user'}, 404

    db.session.delete(follow)
    db.session.commit()
    return {'Message': 'Successfully unfollowed user'}, 200
