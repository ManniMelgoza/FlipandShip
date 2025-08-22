// // src/components/ListingsDetailPage/ListingsDetailPage.jsx

// import { useEffect, useState } from "react";
// import { useParams } from "react-router-dom";
// import { useDispatch, useSelector } from "react-redux";
// import { thunkGetSingleListing } from "../../redux/listings";
// // import Header from "../Re-Components/Header/Header";
// import Footer from "../Re-Components/Footer/Footer";
// import "./ListingsDetailPage.css";

// function ListingsDetailPage() {
//     const { listingId } = useParams();
//     const dispatch = useDispatch();

//     const listing = useSelector((state) => state.listings.currentListing);

//     const [selectedImage, setSelectedImage] = useState(null);
//     const [quantity, setQuantity] = useState(0);

//     useEffect(() => {
//         if (listingId) {
//         dispatch(thunkGetSingleListing(listingId));
//         }
//     }, [dispatch, listingId]);

//     useEffect(() => {
//         if (listing?.images?.length > 0) {
//         setSelectedImage(listing.images[0].url);
//         }
//     }, [listing]);

//     if (!listing) return <div>Loading...</div>;

//     const handleQuantityChange = (e) => {
//         let value = Number(e.target.value);

//         if (value < 1) value = 1; // never less than 1
//         if (value > listing.quantity) value = listing.quantity; // never above stock

//         setQuantity(value);
//     };

//     const handleAddToCart = () => {
//         if (quantity > listing.quantity) {
//         alert("Not enough stock available.");
//         return;
//         }
//         // alert(`Added ${quantity} of "${listing.item_title}" to cart!`);
//         alert(`Feature coming soon`);
//     };

//     return (
//         <>
//         {/* <Header /> */}
//         <div className="product-page">
//             {/* Left: Images */}
//             <div className="images-column">
//             <div className="main-image">
//                 <img src={selectedImage} alt={listing.item_title} />
//             </div>
//             <div className="thumbnails">
//                 {listing.images?.map((img) => (
//                 <img
//                     key={img.id}
//                     src={img.url}
//                     alt={listing.item_title}
//                     className={img.url === selectedImage ? "active-thumb" : ""}
//                     onClick={() => setSelectedImage(img.url)}
//                 />
//                 ))}
//             </div>
//             </div>

//             {/* Right: Product Info */}
//             <div className="info-column">
//             <h1>{listing.item_title}</h1>
//             <p className="brand">Brand: {listing.brand}</p>
//             <p className="price">${listing.price}</p>

//             <div className="purchase-section">
//                 <label htmlFor="quantity">Quantity:</label>
//                 <input
//                 type="number"
//                 id="quantity"
//                 min="1"
//                 max={listing.quantity} // enforce max stock
//                 value={quantity}
//                 onChange={handleQuantityChange}
//                 />
//                 <button
//                 onClick={handleAddToCart}
//                 disabled={listing.quantity === 0} // disable if out of stock
//                 >
//                 {listing.quantity === 0 ? "Out of Stock" : "Add to Cart"}
//                 </button>
//             </div>

//             <div className="additional-info">
//                 <p>Available Stock: {listing.quantity}</p>
//                 <p>Color: {listing.color}</p>
//                 <p>Condition: {listing.condition?.condition_type}</p>
//                 <p>Category: {listing.category?.category_type}</p>
//                 <p>Location: {listing.location}</p>
//             </div>

//             <div className="description">
//                 <h3>Product Description</h3>
//                 <p>{listing.description}</p>
//             </div>
//             </div>
//         </div>
//         <Footer />
//         </>
//     );
//     }

// export default ListingsDetailPage;

// src/components/ListingsDetailPage/ListingsDetailPage.jsx

import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetSingleListing } from "../../redux/listings";
import Footer from "../Re-Components/Footer/Footer";
import OpenModalButton from "../OpenModalButton/OpenModalButton";
import AddToWishlistModal from "../AddtoWishList/AddtoWishlist";
import "./ListingsDetailPage.css";

function ListingsDetailPage() {
  const { listingId } = useParams();
  const dispatch = useDispatch();

  const listing = useSelector((state) => state.listings.currentListing);
  const loggedUser = useSelector((state) => state.session.user);

  const [selectedImage, setSelectedImage] = useState(null);
  const [quantity, setQuantity] = useState(0);

  useEffect(() => {
    if (listingId) {
      dispatch(thunkGetSingleListing(listingId));
    }
  }, [dispatch, listingId]);

  useEffect(() => {
    if (listing?.images?.length > 0) {
      setSelectedImage(listing.images[0].url);
    }
  }, [listing]);

  if (!listing) return <div>Loading...</div>;

  const handleQuantityChange = (e) => {
    let value = Number(e.target.value);

    if (value < 1) value = 1;
    if (value > listing.quantity) value = listing.quantity;

    setQuantity(value);
  };

  const handleAddToCart = () => {
    if (quantity > listing.quantity) {
      alert("Not enough stock available.");
      return;
    }
    alert(`Feature coming soon`);
  };

  return (
    <>
      <div className="product-page">
        {/* Left: Images */}
        <div className="images-column">
          <div className="main-image">
            <img src={selectedImage} alt={listing.item_title} />
          </div>
          <div className="thumbnails">
            {listing.images?.map((img) => (
              <img
                key={img.id}
                src={img.url}
                alt={listing.item_title}
                className={img.url === selectedImage ? "active-thumb" : ""}
                onClick={() => setSelectedImage(img.url)}
              />
            ))}
          </div>
        </div>

        {/* Right: Product Info */}
        <div className="info-column">
          <h1>{listing.item_title}</h1>
          <p className="brand">Brand: {listing.brand}</p>
          <p className="price">${listing.price}</p>

          <div className="purchase-section">
            <label htmlFor="quantity">Quantity:</label>
            <input
              type="number"
              id="quantity"
              min="1"
              max={listing.quantity}
              value={quantity}
              onChange={handleQuantityChange}
            />
            <button
              onClick={handleAddToCart}
              disabled={listing.quantity === 0}
            >
              {listing.quantity === 0 ? "Out of Stock" : "Add to Cart"}
            </button>

            {/* ✅ Add to Wishlist button only if logged in */}
            {loggedUser && (
              <OpenModalButton
                buttonText="Add to Wishlist"
                modalComponent={<AddToWishlistModal listingId={listing.id} />}
              />
            )}
          </div>

          <div className="additional-info">
            <p>Available Stock: {listing.quantity}</p>
            <p>Color: {listing.color}</p>
            <p>Condition: {listing.condition?.condition_type}</p>
            <p>Category: {listing.category?.category_type}</p>
            <p>Location: {listing.location}</p>
          </div>

          <div className="description">
            <h3>Product Description</h3>
            <p>{listing.description}</p>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default ListingsDetailPage;
