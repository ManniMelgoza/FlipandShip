import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import LandingPage from '../components/LandingPage/LandingPage';
import Listings from '../components/ListingsPage/Listings';
import AboutUs from '../components/AboutUs/AboutUs';
import ManageListings from '../components/ManageListings/ManageListings'
import ListingFormModal from '../components/ListingFormModal/ListingFormModal'
import Wishlists from '../components/ManageWishlists/ManageWishlists';
import Layout from './Layout';
import ListingsDetailPage from '../components/ListingsDetailPage/ListingsDetailPage';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <LandingPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "listings",
        element: <Listings />,
      },
      {
      path: "listings/:listingId",
      element: <ListingsDetailPage />
      },
      {
        path: '/current',
        element: <ManageListings />
      },
        {
        path: '/wishlists',
        element: <Wishlists />
      },
      {
        path: 'listing/create',
        element: <ListingFormModal />
      },
      {
        path: "about",
        element: <AboutUs />,
      },
    ],
  },
]);
