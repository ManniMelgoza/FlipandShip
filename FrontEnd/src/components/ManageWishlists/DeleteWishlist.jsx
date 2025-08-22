import { useDispatch } from "react-redux";
import { thunkDeleteWishlist } from '../../redux/wishlist';
import { useModal } from "../../context/Modal";

function ManageDeleteWishlistgModal({ wishlistId }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault();
        try {
            await dispatch(thunkDeleteWishlist(wishlistId));
            closeModal();
        } catch (err) {
            console.error("Failed to delete wishlist", err);
        }
    };

    return (
        <>
            <h1>Confirm Delete</h1>
            <p>Are you sure you want to remove this wishlist?</p>
            <button
                onClick={handleDelete}
                style={{ color: "white", backgroundColor: "red" }}
            >
                Yes (Delete wishlist)
            </button>
            <button
                onClick={closeModal}
                style={{ color: "white", backgroundColor: "gray" }}
            >
                No (Keep wishlist)
            </button>
        </>
    );
}

export default ManageDeleteWishlistgModal;
