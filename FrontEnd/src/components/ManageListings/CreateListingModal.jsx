// src/components/CreateListingModal/CreateListingModal.jsx
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkCreateListing, thunkGetCurrentUserListings, thunkGetCategories, thunkGetConditions } from "../../redux/listings";
// import "./ListingFormModal.css";

function CreateListingModal() {
  const dispatch = useDispatch();
  const { closeModal } = useModal();

  const [title, setTitle] = useState("");
  const [price, setPrice] = useState("");
  const [categoryId, setCategoryId] = useState("");
  const [conditionId, setConditionId] = useState("");
  const [location, setLocation] = useState("");
  const [description, setDescription] = useState("");
  const [brand, setBrand] = useState("");
  const [color, setColor] = useState("");
  const [quantity, setQuantity] = useState("");
  const [imageUrl, setImageUrl] = useState("");
  const [errors, setErrors] = useState([]);

  const categories = useSelector((state) => state.listings.categories) || {};
  const conditions = useSelector((state) => state.listings.conditions) || {};

  const categoryArray = Object.values(categories);
  const conditionArray = Object.values(conditions);

  useEffect(() => {
    dispatch(thunkGetCategories());
    dispatch(thunkGetConditions());
  }, [dispatch]);

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

    if (validationErrors.length > 0) {
      return setErrors(validationErrors);
    }

    const listingData = {
      item_title: title,
      description,
      price,
      color,
      location,
      brand,
      quantity,
      category: categoryId,
      condition: conditionId,
      listing_img1: imageUrl,
    };

    const res = await dispatch(thunkCreateListing(listingData));

    if (res.error) {
      setErrors(Array.isArray(res.error) ? res.error : [res.error]);
    } else {
      await dispatch(thunkGetCurrentUserListings()); // refresh user listings
      closeModal(); // close modal
    }
  };

  return (
    <div className="listing-form-modal">
      <h2>Create Listing</h2>

      {errors.length > 0 && (
        <ul className="listing-form-errors">
          {errors.map((err, i) => (
            <li key={i}>{err}</li>
          ))}
        </ul>
      )}

      <form onSubmit={handleSubmit}>
        <label>
          Title
          <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </label>

        <label>
          Description
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />
        </label>

        <label>
          Location
          <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} required />
        </label>

        <label>
          Brand
          <input type="text" value={brand} onChange={(e) => setBrand(e.target.value)} required />
        </label>

        <label>
          Color
          <input type="text" value={color} onChange={(e) => setColor(e.target.value)} required />
        </label>

        <label>
          Quantity
          <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} required />
        </label>

        <label>
          Price
          <input type="number" step="0.01" value={price} onChange={(e) => setPrice(e.target.value)} required />
        </label>

        <label>
          Category
          <select value={categoryId} onChange={(e) => setCategoryId(e.target.value)} required>
            <option value="">Select category</option>
            {categoryArray.map((cat) => (
              <option key={cat.id} value={cat.id}>{cat.category_type}</option>
            ))}
          </select>
        </label>

        <label>
          Condition
          <select value={conditionId} onChange={(e) => setConditionId(e.target.value)} required>
            <option value="">Select condition</option>
            {conditionArray.map((cond) => (
              <option key={cond.id} value={cond.id}>{cond.condition_type}</option>
            ))}
          </select>
        </label>

        <label>
          Image URL
          <input type="text" value={imageUrl} onChange={(e) => setImageUrl(e.target.value)} required />
        </label>

        <div className="listing-form-buttons">
          <button type="submit">Create Listing</button>
        </div>
      </form>
    </div>
  );
}

export default CreateListingModal;
