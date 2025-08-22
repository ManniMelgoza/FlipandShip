import './Footer.css'

function Footer() {
    return (
        <>

    {/* Footer */}
    <footer className="footer">
    <div className="footer-content">
        {/* Brand Section */}
        <div className="footer-section">
        <div className="footer-brand">
            <div className="footer-logo"></div>
            <div className="footer-brand-content">
            <h3>Flip&Ship</h3>
            <p>
                Discover unbeatable deals on quality items. We specialize in
                giving products a second life and bringing exceptional value
                straight to your door.
            </p>
            </div>
        </div>
        </div>

        {/* Browse Section */}
        <div className="footer-section">
        <h3>Browse</h3>
        <ul>
            <li>
            <a href="/">Home</a>
            </li>
            <li>
            <a href="/about">About Us</a>
            </li>
            <li>
            <a href="/listings">All Listings</a>
            </li>
            {/* <li>
            <a href="/categories">Categories</a>
            </li>
            <li>
            <a href="/sellers">Top Sellers</a>
            </li> */}
        </ul>
        </div>

        {/* Services Section */}
        <div className="footer-section">
            <h3>Services</h3>
            <ul>
                <li>
                <a
                    href="/sell"
                    onClick={(e) => {
                    e.preventDefault(); // Prevent navigation
                    alert("Sell Your Items page coming soon!");
                    }}
                >
                    Sell Your Items
                </a>
                </li>
                <li>
                <a
                    href="/support"
                    onClick={(e) => {
                    e.preventDefault();
                    alert("Customer Support page coming soon!");
                    }}
                >
                    Customer Support
                </a>
                </li>
                <li>
                <a
                    href="/protection"
                    onClick={(e) => {
                    e.preventDefault();
                    alert("Buyer Protection page coming soon!");
                    }}
                >
                    Buyer Protection
                </a>
                </li>
            </ul>
            </div>

        {/* Contact Section */}
        <div className="footer-section">
        <h3>Contact</h3>
        <div className="footer-contact-info">
            📍 123 Commerce St, Your City
        </div>
        <div className="footer-contact-info">
            ✉️ support@flipandship.com
        </div>
        <div className="footer-contact-info">📞 1-800-FLIP-SHIP</div>
        </div>
    </div>

    {/* Footer Bottom */}
    <div className="footer-bottom">
        <p>© {new Date().getFullYear()} Flip&Ship. All rights reserved.</p>
        <a href="/privacy">Privacy Policy</a>
    </div>
    </footer>
    </>
    )
}

export default Footer;
