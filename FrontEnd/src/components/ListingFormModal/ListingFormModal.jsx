import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal"
import { useNavigate } from "react-router-dom";
// import { Link } from "react-router-dom";
import Footer from "../Re-Components/Footer/Footer";
import { thunkGetCategories, thunkGetConditions, thunkCreateListing } from "../../redux/listings";
import "./ListingFormModal.css";

function ListingFormModal() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
    const { closeModal } = useModal();


  // Form state
  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");
  const [categoryId, setCategoryId] = useState("");
  const [conditionId, setConditionId] = useState("");
  const [location, setLocation] = useState("");
  const [description, setDescription] = useState("");
  const [brand, setBrand] = useState("");
  const [color, setColor] = useState("");
  const [quantity, setquantity] = useState("");
  const [imageUrl, setImageUrl] = useState(""); // New image field
  const [errors, setErrors] = useState([]);

  // Redux state
const categories = useSelector(state => state.listings.categories) || [];
const conditions = useSelector(state => state.listings.conditions) || [];

  // Ensure arrays for map()
  const categoryArray = Array.isArray(categories) ? categories : Object.values(categories || []);
  const conditionArray = Array.isArray(conditions) ? conditions : Object.values(conditions || []);


  useEffect(() => {
    dispatch(thunkGetCategories());
    dispatch(thunkGetConditions());
  }, [dispatch]);

  // Helper to validate image URLs
  // const isValidImageURL = (url) => {
  //   return /\.(jpeg|jpg|png)$/i.test(url);
  // };



  const handleSubmit = async (e) => {
    e.preventDefault();

    const validationErrors = [];

    if (!title) validationErrors.push("Title is required");
    if (!description) validationErrors.push("Description is required");
    if (!price) validationErrors.push("Price is required");
    if (!color) validationErrors.push("Color is required");
    if (!location) validationErrors.push("Location is required");
    if (!brand) validationErrors.push("Brand is required");
    if (!quantity) validationErrors.push("Quantity is required");
    if (!categoryId) validationErrors.push("Category is required");
    if (!conditionId) validationErrors.push("Condition is required");
    if (!imageUrl) validationErrors.push("Image URL is required");
    // else if (!isValidImageURL(imageUrl)) validationErrors.push("Image URL must end in .jpg, .jpeg, or .png");

      if (validationErrors.length > 0) {
    return setErrors(validationErrors);
    }

    const listingData = {
      title,
      description,
      price,
      color,
      location,
      brand,
      quantity,
      category_id: categoryId,
      condition_id: conditionId,
      images: [{ listing_img: imageUrl, is_main: true }] // include image in payload
    };

    try {

      const result = await dispatch(thunkCreateListing(listingData));

      if (result.error) {
          setErrors(Array.isArray(result.error) ? result.error : [result.error]);
      } else {
        closeModal(); // Close the modal on successful creation
        navigate(`/`);
      }

    } catch (err) {
  if (err.errors) setErrors(Array.isArray(err.errors) ? err.errors : [err.errors]);
  else console.error('Unexpected error:', err);
      }
    };

  return (

    <>
    <div className="listing-form-modal">
      <h2 className="listing-form-title">Create Listing</h2>

      {errors.length > 0 && (
        <ul className="listing-form-errors">
          {errors.map((error, idx) => <li key={idx} className="listing-form-error">{error}</li>)}
        </ul>
      )}

      <form onSubmit={handleSubmit} className="listing-form">
        <label className="listing-form-label">
          Title
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter listing title"
            required
            className="listing-form-input"
          />
        </label>

        <label className="listing-form-label">
          Description
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Enter listing description"
            required
            className="listing-form-textarea"
          />
        </label>

        <label className="listing-form-label">
          Location
          <input
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            placeholder="Enter listing location"
            required
            className="listing-form-textarea"
          />
        </label>

        <label className="listing-form-label">
          Brand
          <input
            value={brand}
            onChange={(e) => setBrand(e.target.value)}
            placeholder="Enter listing brand"
            required
            className="listing-form-textarea"
          />
        </label>

        <label className="listing-form-label">
          Color
          <input
            value={color}
            onChange={(e) => setColor(e.target.value)}
            placeholder="Enter listing color"
            required
            className="listing-form-textarea"
          />
        </label>

        <label className="listing-form-label">
          Quantity
          <input
            value={quantity}
            onChange={(e) => setquantity(e.target.value)}
            placeholder="Enter listing quantity"
            required
            className="listing-form-textarea"
          />
        </label>

        <label className="listing-form-label">
          Price
          <input
            type="number"
            step="0.01"
            value={price}
            onChange={(e) => setPrice(e.target.value)}
            placeholder="Enter price"
            required
            className="listing-form-input"
          />
        </label>

        <label className="listing-form-label">
          Category
          <select
            value={categoryId}
            onChange={(e) => setCategoryId(e.target.value)}
            required
            className="listing-form-select"
          >
            <option value="">Select category</option>
            {categoryArray.map((cat) => (
              <option key={cat.id} value={cat.id}>{cat.category_type}</option>
            ))}
          </select>
        </label>

        <label className="listing-form-label">
          Condition
          <select
            value={conditionId}
            onChange={(e) => setConditionId(e.target.value)}
            required
            className="listing-form-select"
          >
            <option value="">Select condition</option>
            {conditionArray.map((cond) => (
              <option key={cond.id} value={cond.id}>{cond.condition_type}</option>
            ))}
          </select>
        </label>

        <label className="listing-form-label">
          Image URL
          <input
            type="text"
            value={imageUrl}
            onChange={(e) => setImageUrl(e.target.value)}
            placeholder="Enter main image URL (.jpg, .jpeg, .png)"
            required
            className="listing-form-input"
          />
        </label>

        <div className="listing-form-buttons">
          <button type="submit" className="listing-form-submit">Create Listing</button>
          {/* <button type="button" onClick={closeModal} className="listing-form-cancel">Cancel</button> */}
        </div>
      </form>
    </div>
    <Footer />
    </>
  );
}

export default ListingFormModal;
