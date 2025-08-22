import { useDispatch } from "react-redux";
import { thunkDeleteListing } from '../../redux/listings';
import { useModal } from "../../context/Modal";

function ManageDeleteListingModal({ listingId }) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();

    const handleDelete = async (e) => {
        e.preventDefault();
        try {
            await dispatch(thunkDeleteListing(listingId));
            closeModal();
        } catch (err) {
            console.error("Failed to delete listing", err);
        }
    };

    return (
        <>
            <h1>Confirm Delete</h1>
            <p>Are you sure you want to remove this listings from the listings?</p>
            <button
                onClick={handleDelete}
                style={{ color: "white", backgroundColor: "red" }}
            >
                Yes (Delete listing)
            </button>
            <button
                onClick={closeModal}
                style={{ color: "white", backgroundColor: "gray" }}
            >
                No (Keep listing)
            </button>
        </>
    );
}

export default ManageDeleteListingModal;
