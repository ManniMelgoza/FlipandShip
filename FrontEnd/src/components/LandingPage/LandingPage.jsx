import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllListings } from "../../redux/listings";
import { Link } from "react-router-dom";
import "./LandingPage.css";
import Footer from "../Re-Components/Footer/Footer";
// import Header from "../ Re-Components/Header/Header";


const LandingPage = () => {
    const dispatch = useDispatch();
    const listingsObj = useSelector((state) => state.listings);

    console.log("LISTINGS before:", listingsObj);
    const listingsArr = Object.values(listingsObj);
    console.log("LISTINGS HERE:", listingsArr);
    // console.log("LISTINGS ARR TYPE:", typeof(listingsArr));

    useEffect(() => {
        dispatch(thunkGetAllListings());
    }, [dispatch]);

    return (
        <>
        <div className="landing-container">
            {/* <Header /> */}
        {/* Hero Section */}
        <section className="hero">
            <div className="hero-content">
            <h1>Smart Shopping, Second Chances</h1>
            <p>
                At Flip&Ship, every product has a story worth sharing. Discover
                unbeatable deals on brand-new, open-box, and gently used items — all
                handpicked for value and quality.
            </p>
            <Link to="/listings">
                <button className="cta-btn">Shop Now</button>
            </Link>
            </div>
            <div className="hero-image">
            <img
                src="https://res.cloudinary.com/dnfeiduuu/image/upload/v1755797054/ShoppingMain_ofexl2.jpg"
                alt="Shopping"
            />
            </div>
        </section>

        {/* Category Cards Section */}
        {/* <section className="categories">
    <div className="category-card">
        <h2>New Arrivals</h2>
        <p>Be the first to grab freshly listed deals.</p>
        <button className="card-btn">Shop Now</button>
    </div>
    <div className="category-card">
        <h2>Best Sellers</h2>
        <p>Discover what shoppers love most at Flip&Ship.</p>
        <button className="card-btn">Shop Now</button>
    </div>
    <div className="category-card">
        <h2>Curated Picks</h2>
        <p>Hand-selected favorites for every shopper.</p>
        <button className="card-btn">Shop Now</button>
    </div>
    </section> */}

      {/* Listings Grid */}
    <section className="listings-section">
  <h2>Posted Items</h2>
  <div className="listings-grid">
    {listingsArr.sort(() => 0.5 - Math.random()).slice(0, 7).map((listing) => (
      <Link
        to={`/listings/${listing.id}`}
        key={listing.id}
        className="listing-card"
      >
        <div className="listing-image">
          <img
            src={
              listing.images && listing.images.length > 0
                ? listing.images.find((img) => img.is_main)?.url ||
                  listing.images[0].url
                : "https://res.cloudinary.com/dnfeiduuu/image/upload/v1755820688/coming_soon_ptthmw.jpg"
            }
            alt={listing.item_title}
          />
        </div>
        <div className="listing-info">
          <h3>{listing.item_title}</h3>
          <p>${listing.price}</p>
          <p className="username">Listed by: {listing.owner}</p>
        </div>
      </Link>
    ))}
  </div>
</section>

    {/* Secondary Banner */}
    <section className="cta-banner">
    <h2>Ready to Find Your Next Deal?</h2>
    <Link to="/listings">
        <button className="cta-btn">Browse All Listings</button>
    </Link>
    </section>

    <Footer />

</div>
</>
);
};

export default LandingPage;
