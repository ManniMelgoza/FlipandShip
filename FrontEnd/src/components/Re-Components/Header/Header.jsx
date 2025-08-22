import { Link } from "react-router-dom";
import './Header.css';
import OpenModalMenuItem from "../../Navigation/OpenModalMenuItem";
import LoginFormModal from "../../LoginFormModal/LoginFormModal";
import SignupFormModal from "../../SignupFormModal/SignupFormModal";

function Header() {
    return (
        <header className="header">
            <Link to="/">
                <h1 className="logo">Flip&Ship</h1>
            </Link>
            <div className="auth-buttons">
                <OpenModalMenuItem
                    itemText={<button className="auth-btn">Sign In</button>}
                    modalComponent={<LoginFormModal />}
                />
                <OpenModalMenuItem
                    itemText={<button className="auth-btn">Register</button>}
                    modalComponent={<SignupFormModal />}
                />
            </div>
        </header>
    )
}

export default Header;
