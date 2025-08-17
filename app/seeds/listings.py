from app.models import db, Listing, environment, SCHEMA
from sqlalchemy.sql import text

def seed_listings():

    listings = [
        # Denver - owner_id 1 listing_id range(1-4)
        Listing(owner_id=1, item_title="Tripod Manfrotto", price=250, description="Lightweight yet sturdy Manfrotto tripod in excellent condition. Adjustable height, quick-release plate, and smooth panning head. Perfect for photography or videography.", location='80209', brand="Manfrotto", color="Black", quantity=4, condition_id=4, category_id=17),
        Listing(owner_id=1, item_title="Pro Gear Toolbox", price=120, description="Durable toolbox with secure latches and spacious compartments. Includes wheels for better handling. Ideal for storing hand tools or organizing your workspace. Light wear but fully functional.", location='80238', brand="RIGID", color="Black", quantity=7, condition_id=1, category_id=16),
        Listing(owner_id=1, item_title="TLC TV 32in", price=60, description="32-inch TCL HDTV with crisp display and vibrant colors. Great for bedrooms, dorms, or gaming setups. Includes remote, excellent condition.", location='80204', brand="TLC", color="Black", quantity=2, condition_id=2, category_id=1),
        Listing(owner_id=1, item_title="Surge Protective Device", price=540, description="Reliable Square D MA1IMA161 Surge Protective Device (Type 1) for residential or commercial panels. Protects equipment from voltage spikes. Compact, durable, and ready for installation.", location='80219', brand="Square D", color="Black", quantity=10, condition_id=1, category_id=1),

        # Aurora - owner_id 2 Listing_id range(5-8)
        Listing(owner_id=2, item_title="Specialized Bike", price=180, description="High-quality Specialized road bike with lightweight frame and smooth gear shifting. Ready for commuting, exercise, or weekend rides.", location='80013', brand="Specialized", color="Green", quantity=3, condition_id=4, category_id=5),
        Listing(owner_id=2, item_title="Saw Milwaukee", price=89, description="Powerful Milwaukee electric saw in good working condition. Cuts through wood and metal with ease — perfect for DIY or professional projects.", location='80010', brand="Milwaukee", color="Red", quantity=6, condition_id=3, category_id=16),
        Listing(owner_id=2, item_title="Samsung Stove", price=220, description="Stainless steel Samsung electric stove with smooth glass cooktop and spacious oven. Clean, fully tested, and ready for your kitchen.", location='80012', brand="Samsung", color="Black", quantity=1, condition_id=1, category_id=5),
        Listing(owner_id=2, item_title="Samsung Microwave", price=110, description="Compact yet powerful Samsung microwave with multiple cooking settings. Excellent condition and easy to clean.", location='80017', brand="Samsung", color="Black", quantity=5, condition_id=1, category_id=5),

        # Centennial - owner_id 3 (9-12)
        Listing(owner_id=3, item_title="Ryobi Drill", price=20, description="Cordless Ryobi drill with variable speed control and ergonomic grip. Battery included, ready for any home or work project.", location='80122', brand="Ryobi", color="Blue", quantity=8, condition_id=4, category_id=16),
        Listing(owner_id=3, item_title="Ray-Ban Glasses", price=145, description="Authentic Ray-Ban sunglasses in classic style. UV protection lenses, minimal wear, and includes carrying case.", location='80015', brand="Ray-Ban", color="Black/Gold", quantity=3, condition_id=5, category_id=2),
        Listing(owner_id=3, item_title="Hand-Held Test Kit Masterpact / PowerPact", price=650, description="S33594 Hand-Held Test Kit for Masterpact® and PowerPact® breakers. Portable, accurate, and built for durability. Includes multilingual labels in English, Spanish, and French. Excellent condition.", location='80121', brand="Square D", color="Black", quantity=9, condition_id=1, category_id=16),
        Listing(owner_id=3, item_title="Bell & Gossett P5001889 Seal Kit", price=540, description="Bell & Gossett P5001889 Seal Kit for 2in Series VSX pumps. Made with EPR, carbon, and silicon carbide for durability, chemical resistance, and long service life. Ensures a perfect fit for reliable pump performance in HVAC and industrial use.", location='80123', brand="Bell & Gossett", color="Silver/Black", quantity=2, condition_id=1, category_id=16),

        # Thornton - owner_id 4 (13 - 16)
        Listing(owner_id=4, item_title="Milwaukee Nailer", price=102, description="Heavy-duty Milwaukee nail gun in excellent working order. Fires smoothly and reliably — perfect for framing or carpentry projects.", location='80221', brand="Milwaukee", color="Red", quantity=6, condition_id=4, category_id=16),
        Listing(owner_id=4, item_title="Milwaukee Battery 2.0 Amp", price=77, description="Genuine Milwaukee 2.0Ah rechargeable battery. Holds full charge and compatible with M18 tools.", location='80229', brand="Milwaukee", color="Red", quantity=7, condition_id=1, category_id=16),
        Listing(owner_id=4, item_title="Medical Scissors", price=230, description="Leatherman Raptor medical shears with built-in strap cutter, ring cutter, and glass breaker. Designed for first responders. Excellent condition.", location='80233', brand="Leatherman Raptors", color="Red/Silver", quantity=5, condition_id=5, category_id=16),
        Listing(owner_id=4, item_title="Milwaukee Impact Drill", price=166, description="Milwaukee cordless impact driver with high torque performance. Ideal for tough fastening jobs. Fully functional.", location='80241', brand="Milwaukee", color="Red", quantity=4, condition_id=2, category_id=16),

        # Northglenn - owner_id 5 (17 - 20)
        Listing(owner_id=5, item_title="KitchenAid Mixer", price=190, description="Iconic KitchenAid stand mixer in working condition. Powerful motor, multiple speeds — perfect for baking or cooking enthusiasts.", location='80234', brand="KitchenAid", color="Red", quantity=1, condition_id=3, category_id=1),
        Listing(owner_id=5, item_title="Milwaukee Impact Drill", price=147, description="Milwaukee cordless impact driver with high torque performance. Ideal for tough fastening jobs. Fully functional.", location='80233', brand="Milwaukee", color="Red", quantity=8, condition_id=4, category_id=16),
        Listing(owner_id=5, item_title="DRD2M Light", price=40, description="High-intensity DRD2M light fixture — great for workspaces or photography. Minimal wear, works perfectly.", location='80241', brand="DMF Lighting", color="Black/White", quantity=3, condition_id=2, category_id=3),
        Listing(owner_id=5, item_title="Bose Headphones", price=200, description="Bose over-ear headphones with noise-canceling technology. Crisp sound, comfortable fit, excellent condition.", location='80260', brand="Bose", color="Black", quantity=9, condition_id=5, category_id=1),

        # Boulder - owner_id 6 (21 - 24)
        Listing(owner_id=6, item_title="Beats Headphones", price=140, description="Beats wireless headphones with deep bass and clear audio. Stylish design, folds for easy storage. Works perfectly.", location='80301', brand="Beats", color="Black", quantity=2, condition_id=1, category_id=1),
        Listing(owner_id=6, item_title="Vintage Vinyl Record Player", price=39, description="Classic turntable with built-in speakers. Works perfectly and delivers warm sound. Great for music lovers or vintage décor.", location='80304', brand="Crosley", color="Brown/Teal", quantity=1, condition_id=6, category_id=10),
        Listing(owner_id=6, item_title="Wireless Printer", price=99, description="All-in-one wireless inkjet printer with scanning and copying. Easy setup and great for home or office use.", location='80305', brand="HP", color="White", quantity=4, condition_id=5, category_id=15),
        Listing(owner_id=6, item_title="Mountain Bike", price=205, description="Durable mountain bike with front suspension and 21-speed gears. Perfect for trails, commuting, or weekend rides.", location='80303', brand="Trek", color="Black/Gray", quantity=7, condition_id=4, category_id=4),

        # Broomfield - owner_id 7 (25-28)
        Listing(owner_id=7, item_title="Electric Kettle", price=55, description="Fast-boiling electric kettle with auto shut-off and stainless steel body. Perfect for tea, coffee, or instant meals.", location='80020', brand="Hamilton Beach", color="Black", quantity=10, condition_id=2, category_id=1),
        Listing(owner_id=7, item_title="Leather Office Chair", price=185, description="Comfortable high-back leather office chair with adjustable height and smooth-rolling wheels. Excellent condition.", location='80021', brand="Staples", color="Black", quantity=3, condition_id=5, category_id=19),
        Listing(owner_id=7, item_title="Air Fryer", price=67, description="Compact air fryer with multiple presets for easy cooking. Makes crispy foods with less oil.", location='80023', brand="Phillips", color="Black", quantity=5, condition_id=3, category_id=1),
        Listing(owner_id=7, item_title="Cordless Leaf Blower", price=230, description="Powerful cordless leaf blower with long battery life. Great for yard cleanup or light snow removal.", location='80020', brand="STIHL", color="Orange/White", quantity=2, condition_id=4, category_id=16),

        # Golden - owner_id 8 (29-32)
        Listing(owner_id=8, item_title="Bluetooth Speaker", price=59, description="Portable Bluetooth speaker with deep bass and long battery life. Perfect for outdoor gatherings or home use.", location='80401', brand="JBL", color="Blue", quantity=6, condition_id=3, category_id=1),
        Listing(owner_id=8, item_title="Cordless Power Drill", price=208, description="Heavy-duty cordless drill with two batteries and charger. Ideal for DIY or professional projects.", location='80402', brand="DeWalt", color="Yellow", quantity=7, condition_id=4, category_id=16),
        Listing(owner_id=8, item_title="Camping Tent", price=74, description="Lightweight two-person tent with waterproof coating and easy setup. Great for camping or festivals.", location='80403', brand="Coleman", color="Green", quantity=1, condition_id=5, category_id=4),
        Listing(owner_id=8, item_title="Hand Mixer", price=130, description="Stand mixer with multiple speeds, great for baking and meal prep. Sturdy and reliable.", location='80419', brand="Sunbeam", color="White", quantity=4, condition_id=6, category_id=1),

        # Fort Collins - owner_id 9 (33-36)
        Listing(owner_id=9, item_title="Gaming Keyboard", price=95, description="Mechanical gaming keyboard with RGB backlighting and responsive keys. Great for gamers or work.", location='80521', brand="Razer", color="Black", quantity=5, condition_id=3, category_id=1),
        Listing(owner_id=9, item_title="Snowboard with Bindings", price=170, description="All-mountain snowboard with adjustable bindings. Ready for the slopes this winter.", location='80522', brand="Burton", color="White", quantity=2, condition_id=4, category_id=4),
        Listing(owner_id=9, item_title="Smartwatch", price=48, description="Smartwatch with fitness tracking, notifications, and customizable faces. Works perfectly.", location='80525', brand="Fitbit", color="Black", quantity=9, condition_id=3, category_id=1),
        Listing(owner_id=9, item_title="Car Roof Cargo Box", price=210, description="Spacious roof-mounted cargo box for extra storage on trips. Fits most vehicles.", location='80528', brand="Thule", color="Gray", quantity=6, condition_id=5, category_id=18),

        # Cherry Creek - owner_id 10 (37-40)
        Listing(owner_id=10, item_title="Espresso Machine", price=130, description="Compact espresso machine with steam wand for cappuccinos and lattes. Works great.", location='80110', brand="Breville", color="Silver", quantity=8, condition_id=4, category_id=1),
        Listing(owner_id=10, item_title="Electric Guitar", price=225, description="Solid-body electric guitar with smooth fretboard and clear sound. Great for any player.", location='80111', brand="Fender", color="Aqua", quantity=3, condition_id=5, category_id=12),
        Listing(owner_id=10, item_title="Cordless Vacuum", price=68, description="Lightweight cordless vacuum with strong suction and detachable handheld mode.", location='80112', brand="Shark", color="Brown", quantity=1, condition_id=6, category_id=1),
        Listing(owner_id=10, item_title="Patio Furniture Set", price=105, description="Three-piece patio set with weather-resistant wicker and cushions. Great for outdoor lounging.", location='80113', brand="Mainstays", color="White", quantity=2, condition_id=5, category_id=19),

    ]

    for listing in listings:
        db.session.add(listing)
    db.session.commit()

def undo_listings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.listings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM listings"))

    db.session.commit()
