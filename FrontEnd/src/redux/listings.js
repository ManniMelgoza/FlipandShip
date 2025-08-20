import { csrfFetch } from "./csrf";
// *********************************
//   ACTIONS
// **********************************
// LISITNGS
const GET_ALL_LISTINGS = 'listings/getAllListings';
const GET_SINGLE_LISTING = 'listings/getSingleListing';
const GET_CURRENT_USER_LISTINGS = 'listings/getCurrentUserListings';
const GET_CATEGORIES = 'listings/getCategories';
const GET_CONDITIONS = 'listings/getConditions';
const CREATE_LISTING = 'listings/createListing';
const EDIT_LISTING = 'listings/editListing';
const DELETE_LISTING = 'listings/deleteListing';

// COMMENTS
const GET_ALL_COMMENTS = 'comments/getAllComments';
const CREATE_COMMENT = 'comments/createComment';

// *********************************
//   ACTIONS CREATOR LISTINGS
// **********************************
const getAllListings = (listings) => ({
    type: GET_ALL_LISTINGS,
    payload: listings
});

const getCurrentUserListings = (listings) => ({
    type: GET_CURRENT_USER_LISTINGS,
    payload: listings
});

const getSingleListing = (singlelistings) => ({
    type: GET_SINGLE_LISTING,
    payload: singlelistings
})

const getConditions = (condition) => ({
    type: GET_CONDITIONS,
    payload: condition
})

const getCategories = (category) => ({
    type: GET_CATEGORIES,
    payload: category
})

const createListing = (createListing) => ({
    type: CREATE_LISTING,
    payload: createListing
});

const editListing = (editListing) => ({
    type: EDIT_LISTING,
    payload: editListing
});

const deleteListing = (deleteListing) => ({
    type: DELETE_LISTING,
    const: deleteListing
})

// *********************************
//   ACTIONS CREATOR COMMENTS
// **********************************
const getAllComments = (comments) => ({
    type: GET_ALL_COMMENTS,
    payload: comments
});

const createComment = (createComment) => ({
    type: CREATE_COMMENT,
    payload: createComment
});

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
            return { error: error.errors || ['Unable to retrive lsiting data']};
        }
    } catch (err) {
        console.error('Error retreiving ALL listings', err);
        return {"error": "Unable to retrive ALL listings data"}
    }
};

// -----------------------------
// SINGLE LISTING
// -----------------------------
export const thunkGetSingleListing = (listings_id) => async (dispatch) => {

    try {
        const response = await csrfFetch(`/api/listings/${listings_id}`);

        if(response.ok){
            const singleListing = await response.json();
            dispatch(getSingleListing(singleListing))
            return singleListing;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive single listing data']};
        }
    } catch (err) {
        console.error('Error retreiving single listing', err);
        return {"error": "Unable to retrive single listing data"}
    }
};

// -----------------------------
// USERS LISTINGS
// -----------------------------
export const thunkgetCurrentUerListings = () => async (dispatch) => {

    try {
        const response = await csrfFetch('/api/listings/current');

        if(response.ok){
            const userListings = await response.json();
            dispatch(getCurrentUserListings(userListings.User_Listings))
            return userListings;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive uer listings data']};
        }
    } catch (err) {
        console.error('Error retreiving user listings', err);
        return {"error": "Unable to retrive user listings data"}
    }
};

// -----------------------------
// EDIT LISTING
// -----------------------------
export const thunkCreateListing = (listing_id, listingEdit) => async (dispatch) => {

    try {
        const response = await csrfFetch(`/api/listings/${listing_id}/edit`, {
            method: "PUT",
            headers: {'Contenty-Type': 'application/json'},
            body: JSON.stringify(listingEdit)
        });

        if (response.ok) {
            const editListingData = await response.json();
            dispatch(editListing(editListingData));
            return editListingData;
        } else {
            const error = await response.json();
                return { error: error.errors || ["Not able to edit listing"] };
        }
    } catch (err) {
        console.error('Error editing listing', err);
        return  { "error": "Unable to edit the listing" };
    }
}

// -----------------------------
// CREATE LISTING
// -----------------------------
export const thunkEditLsiting = (listingData) => async (dispatch) => {

    try {
        const response = await csrfFetch('/api/listings/create', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(listingData)
        });
if (response.ok) {
            const newListingData = await response.json();
            dispatch(createPost(newListingData));
            return newListingData;
        } else {
            const error = await response.json();
            return { error: error.errors || ["Not able to create listing"] };
        }
    } catch (err) {
        console.error('Error creating listing', err);
        return { "error": "Unable to create the listing" };
    }
};

// -----------------------------
// DELETE LISTING
// -----------------------------
export const thunkDeleteListing = (listing_id) => async (dispatch) => {
        // Fixed: Added leading slash and used csrfFetch for proper authentication
        const response = await csrfFetch(`/api/listing/${listing_id}`, {
            method: 'DELETE'
        });

        if (response.ok) {
            // Fixed: Dispatch with post_id, not the action creator function
            dispatch(deletePost(listing_id));
            return response;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Listing Not DELETED']}
        }
};

// -----------------------------
// CATEGORY
// -----------------------------
export const thunkGetCategories = () => async (dispatch) => {

    try {
        const response = await csrfFetch('/api/listings/categories');

        if(response.ok){
            const categoriesData = await response.json();
            dispatch(getCategories(categoriesData.Categories))
            return categoriesData;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive categories data']};
        }
    } catch (err) {
        console.error('Error retreiving categories', err);
        return {"error": "Unable to retrive categories data"}
    }
};

// -----------------------------
// CONDITION
// -----------------------------
export const thunkGetConditions = () => async (dispatch) => {

    try {
        const response = await csrfFetch('/api/listings/conditions');

        if(response.ok){
            const conditionsData = await response.json();
            dispatch(getCategories(conditionsData.Categories))
            return conditionsData;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive conditions data']};
        }
    } catch (err) {
        console.error('Error retreiving conditions', err);
        return {"error": "Unable to retrive conditions data"}
    }
};

// *****************************************************************************************
//   COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS  COMMENTS
// ******************************************************************************************

// -----------------------------
// GET ALL COMMENTS
// -----------------------------
export const thunkGetAllComments = (listing_id) => async (dispatch) => {

    try {
        const response = await csrfFetch(`/api/comments/${listing_id}/comments`);

        if(response.ok){
            const listingData = await response.json();
            dispatch(getAllListings(listingData.Listings))
            return listingData;
        } else {
            const error = await response.json();
            return { error: error.errors || ['Unable to retrive lsiting data']};
        }
    } catch (err) {
        console.error('Error retreiving ALL listings', err);
        return {"error": "Unable to retrive ALL listings data"}
    }
};

// -----------------------------
// POST CREATE NEW COMMENTS
// -----------------------------

// *********************************
//   REDUCERS
// **********************************
