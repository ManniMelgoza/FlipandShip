import { csrfFetch } from "./csrf";
// *********************************
//  Action Types
// *********************************
const GET_WISHLIST_ITEMS = "wishlistItems/GET_WISHLIST_ITEMS";
const ADD_WISHLIST_ITEM = "wishlistItems/ADD_WISHLIST_ITEM";
const DELETE_WISHLIST_ITEM = "wishlistItems/DELETE_WISHLIST_ITEM";

// *********************************
//  Action Creators
// *********************************
const getWishlistItems = (items) => ({
    type: GET_WISHLIST_ITEMS,
    payload: items,
});

const addWishlistItem = (item) => ({
    type: ADD_WISHLIST_ITEM,
    payload: item,
});

const deleteWishlistItem = (itemId) => ({
    type: DELETE_WISHLIST_ITEM,
    payload: itemId,
});

// *********************************
//  Thunks
// *********************************
// -----------------------------
// GET WISHLIST ITEMS
// -----------------------------
export const wishlistItemsReducer = (wishlistId) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlistitems/wishlist/${wishlistId}`);

        if (response.ok) {
            const wishlistItems = await response.json();
            dispatch(getWishlistItems(wishlistItems));
            return wishlistItems;
        } else {
            const error = await respoånse.json();
            return { error: error.errors || ["Unable to retrieve wishlist items"] };
        }
    } catch (err) {
        console.error("Error retrieving wishlist items", err);
        return { error: "Unable to retrieve wishlist items" };
    }
};

// -----------------------------
// ADD ITEM TO WISHLIST
// -----------------------------
export const thunkAddWishlistItem = (wishlistId, listingId) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlistitems/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ wishlist_id: wishlistId, listing_id: listingId }),
        });

        if (response.ok) {
            const newItem = await response.json();
            dispatch(addWishlistItem(newItem));
            return newItem;
        } else {
            const error = await response.json();
            return { error: error.errors || ["Unable to add item to wishlist"] };
        }
    } catch (err) {
        console.error("Error adding wishlist item", err);
        return { error: "Unable to add item to wishlist" };
    }
};

// -----------------------------
// REMOVE ITEM FROM WISHLIST
// -----------------------------
export const thunkRemoveWishlistItem = (itemId) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlistitems/${itemId}`, {
            method: "DELETE",
        });

        if (response.ok) {
            dispatch(deleteWishlistItem(itemId));
            return response;
        } else {
            const error = await response.json();
            return { error: error.errors || ["Unable to remove wishlist item"] };
        }
    } catch (err) {
        console.error("Error removing wishlist item", err);
        return { error: "Unable to remove wishlist item" };
    }
};

//  *********************************
//  Reducer
// *********************************
const initialState = {
    wishlistItems: {}, // store items normalized by id
};

const wishlistItemsReducer = (state = initialState, action) => {
    switch (action.type) {
        case GET_WISHLIST_ITEMS: {
            const items = {};
            action.payload.forEach((item) => {
                items[item.id] = item;
            });
            return { ...state, wishlistItems: items };
        }

        case ADD_WISHLIST_ITEM: {
            return {
                ...state,
                wishlistItems: {
                    ...state.wishlistItems,
                    [action.payload.id]: action.payload,
                },
            };
        }

        case DELETE_WISHLIST_ITEM: {
            const newState = { ...state, wishlistItems: { ...state.wishlistItems } };
            delete newState.wishlistItems[action.payload];
            return newState;
        }

        default:
            return state;
    }
};

export default wishlistItemsReducer;
