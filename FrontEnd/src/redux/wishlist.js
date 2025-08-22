import { csrfFetch } from "./csrf";
// *********************************
//   ACTIONS TYPE
// **********************************
const GET_USER_WISHLISTS = 'wishlists/getUserWishlists';
const GET_WISHLIST = 'wishlists/getWishlist';
const CREATE_WISHLIST = 'wishlists/createWishlist';
const EDIT_WISHLIST = 'wishlists/editWishlist';
const DELETE_WISHLIST = 'wishlist/deleteWishlist';

// *********************************
//   ACTIONS
// **********************************
const getUserWishlists = (wishlists) => ({
    type: GET_USER_WISHLISTS,
    payload: wishlists
});

const getWishlist = (wishlist) => ({
    type: GET_WISHLIST,
    payload: wishlist
});

const createWishlistAction = (wishlist) => ({
    type: CREATE_WISHLIST,
    payload: wishlist
});

const editWishlistAction = (wishlist) => ({
    type: EDIT_WISHLIST,
    payload: wishlist
});

const deleteWishlistAction = (wishlistId) => ({
    type: DELETE_WISHLIST,
    payload: wishlistId
});


// *********************************
//   THUNKS
// **********************************

// -----------------------------
// GET ALL USER WISHLISTS
// -----------------------------
export const thunkGetUserWishlists = () => async (dispatch) => {
    try {
        const response = await csrfFetch('/api/wishlists/');

        if (response.ok) {
            const data = await response.json();
            dispatch(getUserWishlists(data.Wishlists));
            return data;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrieve wishlists'] };
        }
    } catch (err) {
        console.error('Error retrieving wishlists', err);
        return { error: 'Unable to retrieve wishlists' };
    }
};

// -----------------------------
// GET SINGLE WISHLIST
// -----------------------------
export const thunkGetWishlist = (wishlistId) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlists/${wishlistId}`);

        if (response.ok) {
            const data = await response.json();
            dispatch(getWishlist(data));
            return data;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrieve wishlist'] };
        }
    } catch (err) {
        console.error('Error retrieving wishlist', err);
        return { error: 'Unable to retrieve wishlist' };
    }
};

// -----------------------------
// CREATE WISHLIST
// -----------------------------
export const thunkCreateWishlist = (newWishlist) => async (dispatch) => {
    try {
        const response = await csrfFetch('/api/wishlists/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ newWishlist })
        });

        if (response.ok) {
            const data = await response.json();
            dispatch(createWishlistAction(data));
            return data;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to create wishlist'] };
        }
    } catch (err) {
        console.error('Error creating wishlist', err);
        return { error: 'Unable to create wishlist' };
    }
};

// -----------------------------
// EDIT WISHLIST
// -----------------------------
export const thunkEditWishlist = (wishlistId, wishlistEdit) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlists/${wishlistId}/edit`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ wishlistEdit })
        });

        if (response.ok) {
            const data = await response.json();
            dispatch(editWishlistAction(data));
            return data;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to edit wishlist'] };
        }
    } catch (err) {
        console.error('Error editing wishlist', err);
        return { error: 'Unable to edit wishlist' };
    }
};

// -----------------------------
// DELETE WISHLIST
// -----------------------------
export const thunkDeleteWishlist = (wishlistId) => async (dispatch) => {
    try {
        const response = await csrfFetch(`/api/wishlists/${wishlistId}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            dispatch(deleteWishlistAction(wishlistId));
            return response;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to delete wishlist'] };
        }
    } catch (err) {
        console.error('Error deleting wishlist', err);
        return { error: 'Unable to delete wishlist' };
    }
};

// *********************************
//   REDUCERS
// **********************************

const initialState = {
    wishlists: {},
    currentWishlist: null,
};

function wishlistReducer(state = initialState, action) {
    switch (action.type) {
        case GET_USER_WISHLISTS: {
        const wishlists = {};
        action.payload.forEach((wishlist) => (wishlists[wishlist.id] = wishlist));
        return { ...state, wishlists };
        }

        case GET_WISHLIST: {
        return { ...state, currentWishlist: action.payload };
        }

        case CREATE_WISHLIST: {
        return {
            ...state,
            wishlists: {
            ...state.wishlists,
            [action.payload.id]: action.payload,
            },
        };
        }

        case EDIT_WISHLIST: {
        return {
            ...state,
            wishlists: {
            ...state.wishlists,
            [action.payload.id]: action.payload,
            },
        };
        }

        case DELETE_WISHLIST: {
        const newWishlists = { ...state.wishlists };
        delete newWishlists[action.payload]; // payload = id
        return { ...state, wishlists: newWishlists };
        }

        default:
        return state;
    }
}

export default wishlistReducer;
