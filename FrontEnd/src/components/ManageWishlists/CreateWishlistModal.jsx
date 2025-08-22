// src/components/CreateWishlistModal/CreateWishlistModal.jsx
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkCreateWishlist, thunkGetUserWishlists } from "../../redux/wishlist";

function CreateWishlistModal() {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const [title, setTitle] = useState("");
  const [errors, setErrors] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await dispatch(thunkCreateWishlist({ title }));

    if (res.error) {
      setErrors(res.error);
    } else {
      // refresh wishlist sidebar
      await dispatch(thunkGetUserWishlists());
      closeModal(); 
    }
  };

  return (
    <div className="create-wishlist-modal">
      <h2>Create New Wishlist</h2>
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
          <button type="submit" className="create-btn">Create Wishlist</button>
          <button type="button" className="cancel-btn" onClick={closeModal}>
            Cancel
          </button>
        </div>
      </form>
    </div>
  );
}

export default CreateWishlistModal;
