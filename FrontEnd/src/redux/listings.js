import { csrfFetch } from "./csrf";
// *********************************
//   ACTIONS
// **********************************
// LISITNGS
const GET_ALL_LISTINGS = 'listings/getAllListings';
// const GET_SINGLE_LISTING = 'listings/getSingleListing';
// const GET_CURRENT_USER_LISTINGS = 'listings/getCurrentUserListings';
// const GET_CATEGORIES = 'listings/getCategories';
// const GET_CONDITIONS = 'listings/getConditions';
// const CREATE_LISTING = 'listings/createListing';
// const EDIT_LISTING = 'listings/editListing';
// const DELETE_LISTING = 'listings/deleteListing';

// COMMENTS
// const GET_ALL_COMMENTS = 'comments/getAllComments';
// const CREATE_COMMENT = 'comments/createComment';

// *********************************
//   ACTIONS CREATOR LISTINGS
// **********************************
const getAllListings = (listings) => ({
    type: GET_ALL_LISTINGS,
    payload: listings
});

// const getCurrentUserListings = (userListings) => ({
//     type: GET_CURRENT_USER_LISTINGS,
//     payload: userListings
// });

// const getSingleListing = (listing) => ({
//     type: GET_SINGLE_LISTING,
//     payload: listing
// })

// const getConditions = (condition) => ({
//     type: GET_CONDITIONS,
//     payload: condition
// })

// const getCategories = (category) => ({
//     type: GET_CATEGORIES,
//     payload: category
// })

// const createListing = (listing) => ({
//     type: CREATE_LISTING,
//     payload: listing
// });

// const editListing = (listing) => ({
//     type: EDIT_LISTING,
//     payload: listing
// });

// const deleteListing = (listingId) => ({
//     type: DELETE_LISTING,
//     const: listingId
// })

// *********************************
//   ACTIONS CREATOR COMMENTS
// **********************************
// const getAllComments = (comments) => ({
//     type: GET_ALL_COMMENTS,
//     payload: comments
// });

// const createComment = (createComment) => ({
//     type: CREATE_COMMENT,
//     payload: createComment
// });

// *********************************
//   THUNKS
// **********************************

// -----------------------------
// ALL LISTINGS
// -----------------------------
export const thunkGetAllListings = () => async (dispatch) => {

    try {
        const response = await csrfFetch('/api/listings');

        if(response.ok){
            const listingData = await response.json();
            dispatch(getAllListings(listingData.Listings))
            return listingData;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive listing data']};
        }
    } catch (err) {
        console.error('Error retreiving ALL listings', err);
        return {"error": "Unable to retrive ALL listings data"}
    }
};

// -----------------------------
// SINGLE LISTING
// -----------------------------
// export const thunkGetSingleListing = (listings_id) => async (dispatch) => {

//     try {
//         const response = await csrfFetch(`/api/listings/${listings_id}`);

//         if(response.ok){
//             const singleListing = await response.json();
//             dispatch(getSingleListing(singleListing))
//             return singleListing;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Unable to retrive single listing data']};
//         }
//     } catch (err) {
//         console.error('Error retreiving single listing', err);
//         return {"error": "Unable to retrive single listing data"}
//     }
// };

// -----------------------------
// USERS LISTINGS
// -----------------------------
// export const thunkGetCurrentUserListings = () => async (dispatch) => {

//     try {
//         const response = await csrfFetch('/api/listings/current');

//         if(response.ok){
//             const userListings = await response.json();
//             dispatch(getCurrentUserListings(userListings.User_Listings))
//             return userListings;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Unable to retrive uer listings data']};
//         }
//     } catch (err) {
//         console.error('Error retreiving user listings', err);
//         return {"error": "Unable to retrive user listings data"}
//     }
// };

// -----------------------------
// EDIT LISTING
// -----------------------------
// export const thunkEditLsiting = (listing_id, listingEdit) => async (dispatch) => {

//     try {
//         const response = await csrfFetch(`/api/listings/${listing_id}/edit`, {
//             method: "PUT",
//             headers: {'Content-Type': 'application/json'},
//             body: JSON.stringify(listingEdit)
//         });

//         if (response.ok) {
//             const editListingData = await response.json();
//             dispatch(editListing(editListingData));
//             return editListingData;
//         } else {
//             const error = await response.json();
//                 return { error: error.errors || ["Not able to edit listing"] };
//         }
//     } catch (err) {
//         console.error('Error editing listing', err);
//         return  { "error": "Unable to edit the listing" };
//     }
// }

// -----------------------------
// CREATE LISTING
// -----------------------------
// export const thunkCreateListing = (listingData) => async (dispatch) => {

//     try {
//         const response = await csrfFetch('/api/listings/create', {
//             method: "POST",
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(listingData)
//         });
// if (response.ok) {
//             const newListingData = await response.json();
//             dispatch(createListing(newListingData));
//             return newListingData;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ["Not able to create listing"] };
//         }
//     } catch (err) {
//         console.error('Error creating listing', err);
//         return { "error": "Unable to create the listing" };
//     }
// };

// -----------------------------
// DELETE LISTING
// -----------------------------
// export const thunkDeleteListing = (listing_id) => async (dispatch) => {
//         // Fixed: Added leading slash and used csrfFetch for proper authentication
//         const response = await csrfFetch(`/api/listings/${listing_id}`, { method: 'DELETE' });

//         if (response.ok) {
//             // Fixed: Dispatch with post_id, not the action creator function
//             dispatch(deleteListing(listing_id));
//             return response;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Listing Not DELETED']}
//         }
// };

// -----------------------------
// CATEGORY
// -----------------------------
// export const thunkGetCategories = () => async (dispatch) => {

//     try {
//         const response = await csrfFetch('/api/listings/categories');

//         if(response.ok){
//             const categoriesData = await response.json();
//             dispatch(getCategories(categoriesData.Categories))
//             return categoriesData;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Unable to retrive categories data']};
//         }
//     } catch (err) {
//         console.error('Error retreiving categories', err);
//         return {"error": "Unable to retrive categories data"}
//     }
// };

// -----------------------------
// CONDITION
// -----------------------------
// export const thunkGetConditions = () => async (dispatch) => {

//     try {
//         const response = await csrfFetch('/api/listings/conditions');

//         if(response.ok){
//             const conditionsData = await response.json();
//             dispatch(getConditions(conditionsData.Conditions))
//             return conditionsData;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Unable to retrive conditions data']};
//         }
//     } catch (err) {
//         console.error('Error retreiving conditions', err);
//         return {"error": "Unable to retrive conditions data"}
//     }
// };

// *****************************************************************************************
//   COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS
// ******************************************************************************************

// // -----------------------------
// // GET ALL COMMENTS
// // -----------------------------
// export const thunkGetAllComments = (listing_id) => async (dispatch) => {

//     try {
//         const response = await csrfFetch(`/api/listings/${listing_id}/comments`);

//         if(response.ok){
//             const commentsData = await response.json();
//             dispatch(getAllComments(commentsData.Comments))
//             return commentsData;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ['Unable to retrive comments data']};
//         }
//     } catch (err) {
//         console.error('Error retreiving ALL comments', err);
//         return {"error": "Unable to retrive ALL comments data"}
//     }
// };

// // -----------------------------
// // POST CREATE NEW COMMENTS
// // -----------------------------
// export const thunkCreateComment = (listing_id, commentData) => async (dispatch) => {

//     try {
//         const response = await csrfFetch(`/api/listings/${listing_id}/create`, {
//             method: "POST",
//             headers: { 'Content-Type': 'application/json' },
//             body: JSON.stringify(commentData)
//         });
//         if (response.ok) {
//             const newCommentData = await response.json();
//             dispatch(createComment(newCommentData));
//             return newCommentData;
//         } else {
//             const error = await response.json();
//             return { error: error.errors || ["Not able to create comment"] };
//         }
//     } catch (err) {
//         console.error('Error creating comment', err);
//         return { "error": "Unable to create the comment" };
//     }
// };
// *********************************
//   REDUCERS
// **********************************
const initialState = {
    listings: {}
    // categories: {},
    // conditions: {},
    // currentListing: null
};

function listingReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_LISTINGS: {
        const newState = {};
        action.payload.forEach((listing) => (newState[listing.id] = listing));
        return newState ;
        }

        // case GET_CATEGORIES: {
        // const categories = {};
        // action.payload.forEach((cat) => (categories[cat.id] = cat));
        // return { ...state, categories };
        // }

        // case GET_CONDITIONS: {
        // const conditions = {};
        // action.payload.forEach((cond) => (conditions[cond.id] = cond));
        // return { ...state, conditions };
        // }

        // case GET_SINGLE_LISTING: {
        // return { ...state, currentListing: action.payload };
        // }

        // case CREATE_LISTING: {
        // return {
        //     ...state,
        //     listings: { ...state.listings, [action.payload.id]: action.payload }
        // };
        // }

        // case EDIT_LISTING: {
        // return {
        //     ...state,
        //     listings: { ...state.listings, [action.payload.id]: action.payload }
        // };
        // }

        // case DELETE_LISTING: {
        // const newListings = { ...state.listings };
        // delete newListings[action.payload];
        // return { ...state, listings: newListings };
        // }

        // // --- Comments nested inside listings ---
        // case GET_ALL_COMMENTS: {
        // const { listingId, comments } = action.payload;
        // const listing = state.listings[listingId];
        // if (!listing) return state;

        // return {
        //     ...state,
        //     listings: {
        //     ...state.listings,
        //     [listingId]: {
        //         ...listing,
        //         comments: comments.reduce((acc, comment) => {
        //         acc[comment.id] = comment;
        //         return acc;
        //         }, {})
        //     }
        //     }
        // };
        // }

        // case CREATE_COMMENT: {
        // const comment = action.payload;
        // const listingId = comment.listingId;
        // const listing = state.listings[listingId];
        // if (!listing) return state;

        // return {
        //     ...state,
        //     listings: {
        //     ...state.listings,
        //     [listingId]: {
        //         ...listing,
        //         comments: { ...listing.comments, [comment.id]: comment }
        //     }
        //     }
        // };
        // }

        default:
        return state;
    }
}

export default listingReducer;

// const initialState = {};
// function listings_commentsReducer(state = initialState, action) {
//     switch(action.type) {
//         case GET_ALL_LISTINGS: {
//             const newState = {}
//             action.payload.forEach((listing) => (newState[listing.id] = listing))
//             return newState;
//         };
//         case GET_CURRENT_USER_LISTINGS: {
//             const newState = {}
//             action.payload.forEach((listing) => (newState[listing.id] = listing))
//             return newState;
//         };
//         case GET_SINGLE_LISTING: {
//             return { ...state, currentListing: action.payload }
//         };
//         case CREATE_LISTING: {
//             const newState = { ...state };
//             newState[action.payload.id] = { ...action.payload }
//             return newState;
//         };
//         case EDIT_LISTING: {
//             return { ...state, [action.payload.id]: action.payload };
//         };
//         case DELETE_LISTING: {
//             const newState = { ...state };
//             delete newState[action.payload];
//             return newState;
//         }
//         case GET_CATEGORIES: {
//             const newState = {}
//             action.payload.forEach((category) => (newState[category.id] = category))
//             return newState;
//         };
//         case GET_CONDITIONS: {
//             const newState = {}
//             action.payload.forEach((conditon) => (newState[conditon.id] = conditon))
//             return newState;
//         };
//         // ----------------
//         // COMMENTS THUNK
//         // ----------------
//         case GET_ALL_COMMENTS: {
//             const newState = {}
//             action.payload.forEach((comment) => (newState[comment.id] = comment))
//             return newState;
//         };
//         case CREATE_COMMENT: {
//             const newState = { ...state };
//             newState[action.payload.id] = { ...action.payload }
//             return newState;
//         };
//         default:
//             return state;
//     }
// }

// export default listings_commentsReducer;
