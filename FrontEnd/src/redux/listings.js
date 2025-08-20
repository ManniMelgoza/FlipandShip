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
// const GET_ALL_COMMENTS = 'comments/getAllComments';
// const CREATE_COMMENT = 'comments/createComment';

// *********************************
//   ACTIONS CREATOR
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
//   THUNKS
// **********************************
export const thunkGetAllListings = () => async (dispatch) => {
    try {}


}


// *********************************
//   REDUCERS
// **********************************
