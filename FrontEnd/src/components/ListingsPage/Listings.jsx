import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllListings } from "../../redux/listings";
import { Link } from "react-router-dom";
import Footer from "../Re-Components/Footer/Footer";
// import Header from "../Re-Components/Header/Header";

function Listings() {
    const dispatch = useDispatch();
    const listingsObj = useSelector((state) => state.listings);
    const listingsArr = Object.values(listingsObj);

    useEffect(() => {
        dispatch(thunkGetAllListings());
    }, [dispatch]);

    return (
        <>
        {/* <Header /> */}
        <div className="landing-container">
            <h2>All Listings</h2>
            {listingsArr.length === 0 ? (
            <p>No listings available</p>
            ) : (
            <section className="listings-section">
                <div className="listings-grid">
                {listingsArr.map((listing) => (
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
            )}
        </div>
        <Footer />
        </>
    );
}

export default Listings;
