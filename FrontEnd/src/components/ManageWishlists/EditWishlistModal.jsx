import { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkEditWishlist, thunkGetUserWishlists } from "../../redux/wishlist";
import { useModal } from "../../context/Modal";

// import "./EditWishlistModal.css";

function EditWishlistModal({ wishlist }) {
  const dispatch = useDispatch();
  const { closeModal } = useModal();
  const [title, setTitle] = useState(wishlist.title);
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const updatedData = { title };

    const res = await dispatch(thunkEditWishlist(wishlist.id, updatedData));

    if (res.error) {
      setErrors(res.error);
    } else {
      // refresh wishlists after edit
      await dispatch(thunkGetUserWishlists());
      closeModal();
    }
  };

  return (
    <div className="edit-wishlist-modal">
      <h2>Edit Wishlist</h2>
      {errors.length > 0 && (
        <ul className="error-list">
          {errors.map((err, i) => <li key={i}>{err}</li>)}
        </ul>
      )}
      <form onSubmit={handleSubmit}>
        <label>
          Wishlist Title:
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </label>
        <div className="modal-buttons">
          <button type="submit" className="update-btn">Update</button>
          <button type="button" className="cancel-btn" onClick={closeModal}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

export default EditWishlistModal;
