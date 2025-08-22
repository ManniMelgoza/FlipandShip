import "./AboutUs.css";
// import Header from "../Re-Components/Header/Header";
import Footer from "../Re-Components/Footer/Footer";

const AboutUs = () => {
  return (
    <>
      <div className="about-container">
        {/* <Header /> */}

        {/* Hero Section */}
        <section className="hero">
          <div className="hero-content">
            <h1>About Flip&Ship</h1>
            <p>
              At Flip&Ship, every product has a story worth sharing. Our mission
              is to connect buyers with high-quality, gently used, and open-box
              items at unbeatable prices. Whether you’re looking for new treasures
              or sustainable shopping options, Flip&Ship is here to help you save
              money while making smart choices.
            </p>
          </div>
          <div className="hero-image">
            <img
              src="https://res.cloudinary.com/dnfeiduuu/image/upload/v1755841849/People_vy1tdc.jpg"
              alt="Flip&Ship Team"
            />
          </div>
        </section>

        {/* Mission Section */}
        <section className="listings-section">
          <h2>Our Mission</h2>
          <p>
            To make second-hand shopping convenient, reliable, and fun. Flip&Ship
            empowers sellers to share their items with a wider audience while
            helping buyers discover unique deals they won’t find anywhere else.
          </p>
        </section>

        <Footer />
      </div>
    </>
  );
};

export default AboutUs;
