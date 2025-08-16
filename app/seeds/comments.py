from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


def seed_comments():

    comments = [
        # Comments for listing_id 1 (Tripod Manfrotto - owner_id 1)
        Comment(user_id=3, listing_id=1, comment_body="Is this still available? Looking for a good tripod for photography."),
        Comment(user_id=7, listing_id=1, comment_body="Great price! Does it come with the carrying case?"),
        Comment(user_id=5, listing_id=1, comment_body="What's the maximum height when fully extended?"),

        # Comments for listing_id 2 (Pro Gear Toolbox - owner_id 1)
        Comment(user_id=4, listing_id=2, comment_body="Perfect for my workshop! Is pickup only or do you deliver?"),
        Comment(user_id=8, listing_id=2, comment_body="How many compartments does it have inside?"),

        # Comments for listing_id 3 (TLC TV 32in - owner_id 1)
        Comment(user_id=2, listing_id=3, comment_body="Does it have smart TV features or just basic HDTV?"),
        Comment(user_id=6, listing_id=3, comment_body="Great for a bedroom setup! Any dead pixels or issues?"),
        Comment(user_id=9, listing_id=3, comment_body="I'll take it if it's still available! Can I pick up today?"),

        # Comments for listing_id 4 (Surge Protective Device - owner_id 1)
        Comment(user_id=10, listing_id=4, comment_body="Do you have the installation manual for this?"),

        # Comments for listing_id 5 (Specialized Bike - owner_id 2)
        Comment(user_id=1, listing_id=5, comment_body="What size frame is this?"),
        Comment(user_id=6, listing_id=5, comment_body="Beautiful bike! Any maintenance records?"),
        Comment(user_id=9, listing_id=5, comment_body="I was wondering if the price is negotiable?"),

        # Comments for listing_id 6 (Saw Milwaukee - owner_id 2)
        Comment(user_id=3, listing_id=6, comment_body="Is this a circular saw or reciprocating saw?"),
        Comment(user_id=4, listing_id=6, comment_body="Milwaukee makes great tools! Does it include extra blades?"),

        # Comments for listing_id 7 (Samsung Stove - owner_id 2)
        Comment(user_id=5, listing_id=7, comment_body="Perfect timing! My old stove just died. Is it gas or electric?"),
        Comment(user_id=7, listing_id=7, comment_body="What are the dimensions? Need to make sure it fits my space."),

        # Comments for listing_id 8 (Samsung Microwave - owner_id 2)
        Comment(user_id=1, listing_id=8, comment_body="How many watts? Looking for something powerful enough for large meals."),

        # Comments for listing_id 9 (Ryobi Drill - owner_id 3)
        Comment(user_id=2, listing_id=9, comment_body="Amazing price! Is the battery 18V or 20V?"),
        Comment(user_id=5, listing_id=9, comment_body="Does it come with a charger too?"),
        Comment(user_id=8, listing_id=9, comment_body="I'll take it! Can we meet today?"),

        # Comments for listing_id 10 (Ray-Ban Glasses - owner_id 3)
        Comment(user_id=4, listing_id=10, comment_body="What model are these? They look like Aviators."),
        Comment(user_id=6, listing_id=10, comment_body="Do you have the case protector?"),

        # Comments for listing_id 11 (Hand-Held Test Kit - owner_id 3)
        Comment(user_id=7, listing_id=11, comment_body="This is exactly what I need for work! Still available?"),

        # Comments for listing_id 12 (Bell & Gossett Seal Kit - owner_id 3)
        Comment(user_id=10, listing_id=12, comment_body="What year was this manufactured?"),

        # Comments for listing_id 13 (Milwaukee Nailer - owner_id 4)
        Comment(user_id=1, listing_id=13, comment_body="Does this nailer come with a hard case or bag?"),
        Comment(user_id=3, listing_id=13, comment_body="Great tool! Any jams or issues?"),

        # Comments for listing_id 14 (Milwaukee Battery 2.0 Amp - owner_id 4)
        Comment(user_id=2, listing_id=14, comment_body="I need this for my M18 impact driver. How's the battery life?"),
        Comment(user_id=8, listing_id=14, comment_body="Will this work with older M18 tools?"),

        # Comments for listing_id 15 (Medical Scissors - owner_id 4)
        Comment(user_id=5, listing_id=15, comment_body="Are you in the medical field? These look professional grade."),
        Comment(user_id=9, listing_id=15, comment_body="Leatherman makes the best tools! Interested if still available."),

        # Comments for listing_id 16 (Milwaukee Impact Drill - owner_id 4)
        Comment(user_id=6, listing_id=16, comment_body="How much torque does this have? Need it for heavy-duty work."),

        # Comments for listing_id 17 (KitchenAid Mixer - owner_id 5)
        Comment(user_id=1, listing_id=17, comment_body="This is a classic! What attachments come with it?"),
        Comment(user_id=3, listing_id=17, comment_body="Perfect for holiday baking! Any cosmetic issues?"),
        Comment(user_id=7, listing_id=17, comment_body="I've been wanting one of these forever! Still for sale?"),

        # Comments for listing_id 18 (Milwaukee Impact Drill - owner_id 5)
        Comment(user_id=4, listing_id=18, comment_body="Another great Milwaukee tool! Battery included?"),

        # Comments for listing_id 19 (DRD2M Light - owner_id 5)
        Comment(user_id=2, listing_id=19, comment_body="What type of bulb does this use? LED or halogen?"),

        # Comments for listing_id 20 (Bose Headphones - owner_id 5)
        Comment(user_id=6, listing_id=20, comment_body="Bose has the best noise canceling! Which model are these?"),
        Comment(user_id=8, listing_id=20, comment_body="Do they come with the original case and cables?"),
        Comment(user_id=10, listing_id=20, comment_body="Great for travel! Are these the QuietComfort series?"),

        # Comments for listing_id 21 (Beats Headphones - owner_id 6)
        Comment(user_id=2, listing_id=21, comment_body="How's the battery life?"),
        Comment(user_id=4, listing_id=21, comment_body="Do these work with Android phones well?"),

        # Comments for listing_id 22 (Vintage Vinyl Record Player - owner_id 6)
        Comment(user_id=1, listing_id=22, comment_body="Love the vintage look! Does it play 33 and 45 RPM?"),
        Comment(user_id=7, listing_id=22, comment_body="Can you connect external speakers to this?"),
        Comment(user_id=9, listing_id=22, comment_body="This would be perfect for my apartment! Very interested."),

        # Comments for listing_id 23 (Wireless Printer - owner_id 6)
        Comment(user_id=3, listing_id=23, comment_body="Does it print in color or just black and white?"),
        Comment(user_id=5, listing_id=23, comment_body="How much are replacement ink cartridges typically?"),

        # Comments for listing_id 24 (Mountain Bike - owner_id 6)
        Comment(user_id=8, listing_id=24, comment_body="Trek makes excellent bikes! What size frame?"),
        Comment(user_id=10, listing_id=24, comment_body="Perfect for Colorado trails! Any recent tune-ups?"),

        # Comments for listing_id 25 (Electric Kettle - owner_id 7)
        Comment(user_id=1, listing_id=25, comment_body="How fast does it boil water? Looking for something quick."),
        Comment(user_id=4, listing_id=25, comment_body="Great price! Is it stainless steel inside too?"),

        # Comments for listing_id 26 (Leather Office Chair - owner_id 7)
        Comment(user_id=2, listing_id=26, comment_body="Perfect for my home office! How's the lumbar support?"),
        Comment(user_id=6, listing_id=26, comment_body="Does it recline or just adjust height?"),

        # Comments for listing_id 27 (Air Fryer - owner_id 7)
        Comment(user_id=3, listing_id=27, comment_body="Ninja makes great air fryers! What's the capacity?"),
        Comment(user_id=9, listing_id=27, comment_body="Been wanting to try air frying! Is this easy to clean?"),

        # Comments for listing_id 28 (Cordless Leaf Blower - owner_id 7)
        Comment(user_id=5, listing_id=28, comment_body="DeWalt tools are reliable! How long does the battery last?"),

        # Comments for listing_id 29 (Bluetooth Speaker - owner_id 8)
        Comment(user_id=1, listing_id=29, comment_body="JBL has great sound quality! Is it waterproof?"),
        Comment(user_id=7, listing_id=29, comment_body="Perfect for camping trips! How's the Bluetooth range?"),

        # Comments for listing_id 30 (Cordless Power Drill - owner_id 8)
        Comment(user_id=2, listing_id=30, comment_body="Makita is top quality! Are both batteries the same voltage?"),
        Comment(user_id=4, listing_id=30, comment_body="Two batteries is a great deal! What's the chuck size?"),

        # Comments for listing_id 31 (Camping Tent - owner_id 8)
        Comment(user_id=6, listing_id=31, comment_body="Coleman tents are reliable! How many seasons is this rated for?"),
        Comment(user_id=10, listing_id=31, comment_body="Perfect for summer camping! Does it have a rainfly?"),

        # Comments for listing_id 32 (Stand Mixer - owner_id 8)
        Comment(user_id=3, listing_id=32, comment_body="Good alternative to KitchenAid! What's the bowl capacity?"),

        # Comments for listing_id 33 (Gaming Keyboard - owner_id 9)
        Comment(user_id=1, listing_id=33, comment_body="Razer makes the best gaming gear! What type of switches?"),
        Comment(user_id=5, listing_id=33, comment_body="Love the RGB lighting! Is it mechanical or membrane?"),

        # Comments for listing_id 34 (Snowboard with Bindings - owner_id 9)
        Comment(user_id=2, listing_id=34, comment_body="Burton is the best brand! What length is the board?"),
        Comment(user_id=8, listing_id=34, comment_body="Perfect timing for ski season! What boot size do the bindings fit?"),

        # Comments for listing_id 35 (Smartwatch - owner_id 9)
        Comment(user_id=4, listing_id=35, comment_body="Great price for a Fitbit! Does it track sleep too?"),
        Comment(user_id=7, listing_id=35, comment_body="How accurate is the heart rate monitor?"),

        # Comments for listing_id 36 (Car Roof Cargo Box - owner_id 9)
        Comment(user_id=6, listing_id=36, comment_body="Thule makes the best roof equipment! What's the weight capacity?"),

        # Comments for listing_id 37 (Espresso Machine - owner_id 10)
        Comment(user_id=1, listing_id=37, comment_body="De'Longhi makes great espresso! Does it use pods or ground coffee?"),
        Comment(user_id=3, listing_id=37, comment_body="Perfect for my morning routine! How's the crema quality?"),

        # Comments for listing_id 38 (Electric Guitar - owner_id 10)
        Comment(user_id=5, listing_id=38, comment_body="Fender is legendary! What pickup configuration does it have?"),
        Comment(user_id=9, listing_id=38, comment_body="Beautiful sunburst finish! Does it come with a case or gig bag?"),

        # Comments for listing_id 39 (Cordless Vacuum - owner_id 10)
        Comment(user_id=2, listing_id=39, comment_body="Shark vacuums are great! How long does the battery last?"),
        Comment(user_id=8, listing_id=39, comment_body="Perfect for quick cleanups! Does it work well on pet hair?"),

        # Comments for listing_id 40 (Patio Furniture Set - owner_id 10)
        Comment(user_id=4, listing_id=40, comment_body="Great for outdoor entertaining! Are the cushions weather resistant?"),
        Comment(user_id=6, listing_id=40, comment_body="Does the set have any sun damage?"),
    ]

    for comment in comments:
        db.session.add(comment)
    db.session.commit()


def undo_follows():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.commentss RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
