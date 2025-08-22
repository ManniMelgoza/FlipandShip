// src/components/ManageWishlists/ManageWishlists.jsx
import { useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetUserWishlists } from "../../redux/wishlist";
import ManageDeleteWishlistgModal from './DeleteWishlist'
import OpenModalButton from "../OpenModalButton/OpenModalButton";

import Footer from "../Re-Components/Footer/Footer";
import "./ManageWishlists.css";

function ManageWishlists() {
  const dispatch = useDispatch();
  const wishlistsAll = useSelector((state) => state.wishlist?.wishlists || {});
  const loggedUser = useSelector((state) => state.session?.user);

  useEffect(() => {
    if (loggedUser) dispatch(thunkGetUserWishlists());
  }, [dispatch, loggedUser]);

  if (!wishlistsAll || !loggedUser) return <div>Loading...</div>;

  const wishlistsArray = Object.values(wishlistsAll);

  return (
    <>
      <div className="landing-container">
        <h1>Manage Your Wishlists</h1>
        <Link to="/wishlist/create" className="cta-btn">
          Create a New Wishlist
        </Link>

        {wishlistsArray.length === 0 ? (
          <p>No wishlists available</p>
        ) : (
          <section className="listings-section">
            <div className="listings-grid">
              {wishlistsArray.map((wishlist) => {
                const itemsArray = wishlist.wishlistitems || [];

                return (
                  <div key={wishlist.id} className="listing-card">
                    <h3 className="wishlist-title">{wishlist.title}</h3>
                    <OpenModalButton
                      buttonText="Delete"
                      className="quick-view"
                      modalComponent={<ManageDeleteWishlistgModal wishlistId={wishlist.id} />}
                    />
                    {itemsArray.length === 0 ? (
                      <p className="no-items">No items in this wishlist</p>
                    ) : (
                      <div className="wishlist-items-grid">
                        {itemsArray.map((item) => (
                          <Link
                            key={item.id}
                            to={`/listings/${item.listing_id}`}
                            style={{ textDecoration: "none", color: "inherit" }}
                          >
                            <div className="wishlist-item-card">
                              <div className="listing-image">
                                <img
                                  src={item.listing?.images?.[0]?.url || "/placeholder.jpg"}
                                  alt={item.listing?.item_title || "Listing"}
                                />
                              </div>
                              <div className="listing-info">
                                <p>{item.listing?.item_title || "Item"}</p>
                                <p>${item.listing?.price || 0}</p>
                              </div>
                            </div>
                          </Link>
                        ))}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </section>
        )}
      </div>
      <Footer />
    </>
  );
}

export default ManageWishlists;
