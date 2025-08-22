// src/components/ManageListings/ManageListings.jsx
import { useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetCurrentUserListings } from "../../redux/listings";
import ManageDeleteListingModal from "./DeleteListings";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import Footer from "../Re-Components/Footer/Footer";
import "./ManageListings.css";

function ManageListings() {
  const dispatch = useDispatch();
  const listingsAll = useSelector((state) => state.listings.listings); // Slice has .listings
  const loggedUser = useSelector((state) => state.session?.user);

  useEffect(() => {
    dispatch(thunkGetCurrentUserListings());
  }, [dispatch]);

  if (!listingsAll || !loggedUser) return <div>Loading...</div>;

  const listingsArray = Object.values(listingsAll);

  return (
    <>
      <div className="landing-container">
        <h1>Manage Your Listings</h1>
        <Link to="/listings/create" className="cta-btn">
          Create a New Listing
        </Link>

        {listingsArray.length === 0 ? (
          <p>No listings available</p>
        ) : (
          <section className="listings-section">
            <div className="listings-grid">
              {listingsArray.map((listing) => (
                <div key={listing.id} className="listing-card">
                  <Link
                    to={`/listings/${listing.id}`}
                    style={{ textDecoration: "none", color: "inherit" }}
                  >
                    <div className="listing-image">
                      <img
                        src={
                          listing.images && listing.images.length > 0
                            ? listing.images.find((img) => img.is_main)?.url ||
                              listing.images[0].url
                            : "/placeholder.jpg"
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
                  <div style={{ marginTop: "8px" }}>
                    <Link
                      to={`/listings/${listing.id}/edit`}
                      className="quick-view"
                      style={{ marginRight: "8px" }}
                    >
                      Update
                    </Link>
                    <OpenModalButton
                      buttonText="Delete"
                      className="quick-view"
                      modalComponent={<ManageDeleteListingModal listingId={listing.id} />}
                    />
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}
      </div>
      <Footer />
    </>
  );
}

export default ManageListings;
