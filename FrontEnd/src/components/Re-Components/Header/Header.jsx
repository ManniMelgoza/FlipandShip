import { Link } from "react-router-dom";
import './Header.css'

function Header() {
    return (
        <header className="header">
            <Link to="/">
                <h1 className="logo">Flip&Ship</h1>
            </Link>
            <div className="auth-buttons">
            <button className="auth-btn">Sign In</button>
            <button className="auth-btn">Register</button>
            </div>
        </header>
    )
}

export default Header;
