import "./HeroSection.css";

import {
    FaCalendarAlt,
    FaMapMarkerAlt,
    FaUserCheck
}
from "react-icons/fa";

function HeroSection({ dashboard }) {

    return (

        <section className="hero-section">

            <div className="hero-left">

                <h1>

                    Welcome back,

                    <span>

                        {" "}
                        {dashboard?.farmer_name || "Farmer"}

                    </span>

                    👋

                </h1>

                <p>

                    Here's what's happening on your farm today.

                </p>

                <div className="hero-info">

                    <div className="hero-box">

                        <FaCalendarAlt />

                        <div>

                            <small>Today</small>

                            <h5>{dashboard.current_date}</h5>

                        </div>

                    </div>

                    <div className="hero-box">

                        <FaMapMarkerAlt />

                        <div>

                            <small>Location</small>

                            <h5>{dashboard.location}</h5>

                        </div>

                    </div>

                    <div className="hero-box">

                        <FaUserCheck />

                        <div>

                            <small>Role</small>

                            <h5>{dashboard.verified ? "Verified Farmer" : "Farmer"}</h5>

                        </div>

                    </div>

                </div>

            </div>

            <div className="hero-right">

                <img

                    src="/images/hero-farm.png"

                    alt="Farm"

                />

            </div>

        </section>

    );

}

export default HeroSection;