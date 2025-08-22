// src/components/AddToWishlistModal/AddToWishlistModal.jsx
import { useDispatch, useSelector } from "react-redux";
import { thunkGetUserWishlists } from "../../redux/wishlist";
import { thunkAddItemToWishlist } from "../../redux/wishlistitems";
import { useEffect } from "react";
import { useModal } from "../../context/Modal";

function AddToWishlistModal({ listingId }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const wishlists = useSelector((state) => state.wishlist?.wishlists || {});
    const wishlistsArr = Object.values(wishlists);

    useEffect(() => {
        dispatch(thunkGetUserWishlists());
    }, [dispatch]);

    const handleAdd = async (wishlistId) => {
        await dispatch(thunkAddItemToWishlist(wishlistId, listingId));
        closeModal();
    };

    return (
        <div className="wishlist-modal">
        <h2>Select a Wishlist</h2>
        {wishlistsArr.length === 0 ? (
            <p>No wishlists available. Create one first!</p>
        ) : (
            <ul>
            {wishlistsArr.map((wl) => (
                <li key={wl.id}>
                <button onClick={() => handleAdd(wl.id)}>{wl.title}</button>
                </li>
            ))}
            </ul>
        )}
        </div>
    );
}

export default AddToWishlistModal;
