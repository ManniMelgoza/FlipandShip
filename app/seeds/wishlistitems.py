from app.models import db, Wishlistitem, environment, SCHEMA
from sqlalchemy.sql import text

def seed_wishlistitems():

    Wishlistitems = [
        # User Demo WishLists (owner_id = 1)

        # Tools
        Wishlistitem(wishlist_id = 1, listing_id = 6),  # Saw Milwaukee
        Wishlistitem(wishlist_id = 1, listing_id = 13), # Milwaukee Nailer
        Wishlistitem(wishlist_id = 1, listing_id = 18), # KitchenAid Mixer
        Wishlistitem(wishlist_id = 1, listing_id = 9), # Ryobi Drill

        # Photography
        Wishlistitem(wishlist_id = 2, listing_id = 1),  # Tripod Manfrotto
        Wishlistitem(wishlist_id = 2, listing_id = 21), # Beats Headphones (audio for music/photography)

        # Home Electronics
        Wishlistitem(wishlist_id = 3, listing_id = 3),  # TLC TV 32in
        Wishlistitem(wishlist_id = 3, listing_id = 4),  # Surge Protective Device
        Wishlistitem(wishlist_id = 3, listing_id = 33), # Gaming Keyboard

        # User Marnie WishLists (owner_id = 2)

        # Bikes
        Wishlistitem(wishlist_id = 4, listing_id = 5),  # Specialized Bike
        Wishlistitem(wishlist_id = 4, listing_id = 24), # Mountain Bike

        # Power Tools
        Wishlistitem(wishlist_id = 5, listing_id = 9),  # Ryobi Drill
        Wishlistitem(wishlist_id = 5, listing_id = 13), # Milwaukee Nailer
        Wishlistitem(wishlist_id = 5, listing_id = 14), # Milwaukee Battery 2.0 Amp
        Wishlistitem(wishlist_id = 5, listing_id = 2), #

        # Kitchen Appliances
        Wishlistitem(wishlist_id = 6, listing_id = 7),  # Samsung Stove
        Wishlistitem(wishlist_id = 6, listing_id = 8),  # Samsung Microwave

        # User Bobbie WishLists (owner_id = 3)

        # Power Tools
        Wishlistitem(wishlist_id = 7, listing_id = 2),  # Pro Gear Toolbox
        Wishlistitem(wishlist_id = 7, listing_id = 6),  # Saw Milwaukee

        # Fashion & Accessories
        Wishlistitem(wishlist_id = 8, listing_id = 10), # Ray-Ban Glasses
        Wishlistitem(wishlist_id = 8, listing_id = 15), # Medical Scissors (could count as accessory in this context)

        # Industrial Equipment
        Wishlistitem(wishlist_id = 9, listing_id = 11), # Hand-Held Test Kit
        Wishlistitem(wishlist_id = 9, listing_id = 14), # Milwaukee Battery 2.0 Amp

        # User Alex WishLists (owner_id = 4)

        # Power Tools
        Wishlistitem(wishlist_id = 10, listing_id = 2),  # Pro Gear Toolbox
        Wishlistitem(wishlist_id = 10, listing_id = 6),  # Saw Milwaukee

        # Medical Gear
        Wishlistitem(wishlist_id = 11, listing_id = 12), # Medical Scissors
        Wishlistitem(wishlist_id = 11, listing_id = 10), # Ray-Ban Glasses (stretch as accessory)

        # User Sophia WishLists (owner_id = 5)

        # Kitchen Appliances
        Wishlistitem(wishlist_id = 12, listing_id = 7),  # Samsung Stove
        Wishlistitem(wishlist_id = 12, listing_id = 8),  # Samsung Microwave

        # Power Tools
        Wishlistitem(wishlist_id = 13, listing_id = 13), # Milwaukee Nailer
        Wishlistitem(wishlist_id = 13, listing_id = 6),  # Saw Milwaukee

        # Electronics
        Wishlistitem(wishlist_id = 14, listing_id = 3),  # TLC TV 32in
        Wishlistitem(wishlist_id = 14, listing_id = 21), # Beats Headphones
        Wishlistitem(wishlist_id = 14, listing_id = 35), # SmartWatch

        # User James WishLists (owner_id = 6)

        # Audio & Music
        Wishlistitem(wishlist_id = 15, listing_id = 21), # Beats Headphones
        Wishlistitem(wishlist_id = 15, listing_id = 22), # Vintage Vinyl Record Player
        Wishlistitem(wishlist_id = 15, listing_id = 35), # SmartWatch

        # Vintage Items
        Wishlistitem(wishlist_id = 16, listing_id = 22), # Vintage Vinyl Record Player
        Wishlistitem(wishlist_id = 16, listing_id = 20), # Bose Headphones
        Wishlistitem(wishlist_id = 16, listing_id = 38), # Electric Guitar

        # Sports & Outdoors
        Wishlistitem(wishlist_id = 17, listing_id = 5),  # Specialized Bike
        Wishlistitem(wishlist_id = 17, listing_id = 28), # Mountain Bike
        Wishlistitem(wishlist_id = 17, listing_id = 36), # Car Roof Cargo Box
        Wishlistitem(wishlist_id = 17, listing_id = 28), # Cordless Leaf Blower

        # User Linda WishLists (owner_id = 7)

        # Kitchen Appliances
        Wishlistitem(wishlist_id = 18, listing_id = 7),  # Samsung Stove
        Wishlistitem(wishlist_id = 18, listing_id = 8),  # Samsung Microwave

        # Office Furniture
        Wishlistitem(wishlist_id = 19, listing_id = 26), # Leather Office Chair
        Wishlistitem(wishlist_id = 19, listing_id = 29), # Bluetooth Speaker
        Wishlistitem(wishlist_id = 19, listing_id = 22), # Vinyl

        # Yard Tools
        Wishlistitem(wishlist_id = 20, listing_id = 30), # Cordless Power Drill
        Wishlistitem(wishlist_id = 20, listing_id = 28), # Cordless Leaf Blower
        Wishlistitem(wishlist_id = 20, listing_id = 14), # Milwaukee Battery 2.0 Amp

        # User Michael WishLists (owner_id = 8)

        # Audio & Music
        Wishlistitem(wishlist_id = 21, listing_id = 21), # Beats Headphones
        Wishlistitem(wishlist_id = 21, listing_id = 22), # Vintage Vinyl Record Player

        # Power Tools
        Wishlistitem(wishlist_id = 22, listing_id = 6),  # Saw Milwaukee
        Wishlistitem(wishlist_id = 22, listing_id = 13), # Milwaukee Nailer
        Wishlistitem(wishlist_id = 22, listing_id = 14), # Milwaukee Battery 2.0 Amp

        # Camping Gear
        Wishlistitem(wishlist_id = 23, listing_id = 30), # Camping Tent
        Wishlistitem(wishlist_id = 23, listing_id = 31), # Stand Mixer
        Wishlistitem(wishlist_id = 23, listing_id = 24), # Mountain Bike
        Wishlistitem(wishlist_id = 23, listing_id = 10), # Ray-Ban Glasses

        # User Natalie WishLists (owner_id = 9)

        # Gaming Gear & Sports
        Wishlistitem(wishlist_id = 24, listing_id = 21), # Beats Headphones
        Wishlistitem(wishlist_id = 24, listing_id = 34), # Snowboard with Bindings
        Wishlistitem(wishlist_id = 24, listing_id = 31), # Camping Tent

        # Winter Sports
        Wishlistitem(wishlist_id = 25, listing_id = 34), # Snowboard with Bindings
        Wishlistitem(wishlist_id = 25, listing_id = 32), # Smartwatch

        # Travel Gear
        Wishlistitem(wishlist_id = 26, listing_id = 36), # Car Roof Cargo Box
        Wishlistitem(wishlist_id = 26, listing_id = 31), # Camping Tent

        # User Ryan WishLists (owner_id = 10)

        # Coffee & Kitchen
        Wishlistitem(wishlist_id = 27, listing_id = 7),  # Samsung Stove
        Wishlistitem(wishlist_id = 27, listing_id = 8),  # Samsung Microwave

        # Musical Instruments
        Wishlistitem(wishlist_id = 28, listing_id = 38), # Electric Guitar
        Wishlistitem(wishlist_id = 28, listing_id = 21), # Beats

        # Home Furniture
        Wishlistitem(wishlist_id = 29, listing_id = 40), # Patio Furniture Set
        Wishlistitem(wishlist_id = 29, listing_id = 26), # Leather Office Chair
        Wishlistitem(wishlist_id = 29, listing_id = 20), # DRD2M Light
        Wishlistitem(wishlist_id = 29, listing_id = 3), # "TLC TV 32in
    ]

    for item in Wishlistitems:
        db.session.add(item)
    db.session.commit()


def undo_wishlistitems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.wishlistitems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM wishlistitems"))

    db.session.commit()
