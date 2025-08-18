from flask import Blueprint, jsonify, request
from app.models import Listing, Comment, db
from app.forms import  CommentForm
from flask_login import login_required, current_user

# url_prefix='/api/comments') NOTE
comment_routes = Blueprint('comments', __name__)

# *********************************
#   EDIT Comment by id
#**********************************
@comment_routes.route('/<int:comment_id>/edit', methods=['PUT'])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return {"Message": 'comment not found in post'}, 404

    if comment.user_id != current_user.id:
        return {'Message': 'You are not authorized to edit this comment'}, 403

    edit_comment = CommentForm(obj=comment)
    edit_comment['csrf_token'].data = request.cookies['csrf_token']

    if edit_comment.validate_on_submit():
        comment.comment_body=edit_comment.data['comment_body']

        db.session.commit()
        return comment.to_dict(), 200
    return {'Errors': edit_comment.errors}, 400

# *********************************
#   DELTE Comment
#**********************************
@comment_routes.route('/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    comment_delete = Comment.query.get(comment_id)

    if not comment_delete:
        return {'Message': 'Comment not found'}, 404
    if comment_delete.user_id != current_user.id:
        return {"Message": 'You are not authorized to delete this comment'}, 403

    db.session.delete(comment_delete)
    db.session.commit()
    return {"Message": 'Your comment has being DELETED'}, 200
