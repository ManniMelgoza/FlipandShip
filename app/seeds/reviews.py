from app.models import db, Review, environment, SCHEMA
from sqlalchemy.sql import text

def seed_reviews():

    Reviews = [
        # User 1 reviews (Demo)
        Review(reviewer_id=3, reviewed_user_id=1, rating=3, review_body="Demo was prompt and professional. Highly recommend!"),
        Review(reviewer_id=7, reviewed_user_id=1, rating=4, review_body="Great communication with Demo and a smooth experience."),
        Review(reviewer_id=9, reviewed_user_id=1, rating=1, review_body="Por communication from Demo."),

        # User 2 reviews (Manni)
        Review(reviewer_id=1, reviewed_user_id=2, rating=5, review_body="Manni was very helpful and easy to deal with."),
        Review(reviewer_id=4, reviewed_user_id=2, rating=3, review_body="Excellent collaboration with Manni, everything went well."),
        Review(reviewer_id=8, reviewed_user_id=2, rating=4, review_body="Highly trustworthy and friendly with Manni."),

        # User 3 reviews (Bobbie)
        Review(reviewer_id=2, reviewed_user_id=3, rating=5, review_body="Bobbie delivers on time and communicates clearly."),
        Review(reviewer_id=5, reviewed_user_id=3, rating=1, review_body="Bobbie was a good re-seller but poor quality item not as described."),
        Review(reviewer_id=6, reviewed_user_id=3, rating=3, review_body="Smooth transaction with Bobbie and highly recommended."),

        # User 4 reviews (Alex)
        Review(reviewer_id=1, reviewed_user_id=4, rating=5, review_body="Alex was knowledgeable and responsive."),
        Review(reviewer_id=3, reviewed_user_id=4, rating=4, review_body="Great experience with Alex, very courteous."),
        Review(reviewer_id=9, reviewed_user_id=4, rating=2, review_body="Very professional and prompt in responses with Alex."),

        # User 5 reviews (Sophia)
        Review(reviewer_id=2, reviewed_user_id=5, rating=1, review_body="Sophia was not helpful answering questions."),
        Review(reviewer_id=7, reviewed_user_id=5, rating=4, review_body="Reliable and easy to work with Sophia."),
        Review(reviewer_id=10, reviewed_user_id=5, rating=0, review_body="Never responded to my questions."),

        # User 6 reviews (James)
        Review(reviewer_id=1, reviewed_user_id=6, rating=3, review_body="James is professional and communicates clearly."),
        Review(reviewer_id=3, reviewed_user_id=6, rating=4, review_body="Very helpful and cooperative with James."),
        Review(reviewer_id=8, reviewed_user_id=6, rating=2, review_body="Smooth and efficient experience with James."),

        # User 7 reviews (Linda)
        Review(reviewer_id=2, reviewed_user_id=7, rating=2, review_body="Linda is friendly and dependable, item was in okay conditons."),
        Review(reviewer_id=4, reviewed_user_id=7, rating=3, review_body="Great experience with Linda, quick responses."),
        Review(reviewer_id=9, reviewed_user_id=7, rating=4, review_body="Highly recommended, excellent interaction with Linda."),

        # User 8 reviews (Michael)
        Review(reviewer_id=1, reviewed_user_id=8, rating=4, review_body="Michael was patient and very responsive."),
        Review(reviewer_id=5, reviewed_user_id=8, rating=3, review_body="Great communication and reliable with Michael."),
        Review(reviewer_id=10, reviewed_user_id=8, rating=5, review_body="Professional and courteous throughout with Michael."),

        # User 9 reviews (Natalie)
        Review(reviewer_id=2, reviewed_user_id=9, rating=5, review_body="Natalie is prompt and trustworthy."),
        Review(reviewer_id=6, reviewed_user_id=9, rating=4, review_body="Smooth transaction, very satisfied with Natalie."),
        Review(reviewer_id=7, reviewed_user_id=9, rating=5, review_body="Excellent cooperation, highly recommend Natalie."),

        # User 10 reviews (Ryan)
        Review(reviewer_id=1, reviewed_user_id=10, rating=4, review_body="Ryan was friendly and easy to work with."),
        Review(reviewer_id=3, reviewed_user_id=10, rating=3, review_body="Very professional and communicative with Ryan."),
        Review(reviewer_id=5, reviewed_user_id=10, rating=4, review_body="Highly recommended, great experience overall with Ryan."),
    ]

    for review in Reviews:
        db.session.add(review)
    db.session.commit()


def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
