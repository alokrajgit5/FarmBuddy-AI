import { useState } from "react";
import { NavLink, Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

import {
  FaLeaf,
  FaUserCircle,
  FaSignOutAlt,
  FaCloudSun,
  FaRobot,
  FaUser,
  FaSeedling,
  FaTractor,
  FaUsers,
  FaShoppingBasket,
  FaCog,
  FaBell,
  FaMoon,
  FaSun,
  FaGlobe,
  FaSearch,
  FaEnvelope,
  FaTachometerAlt,
  FaStar,
  FaCheckCircle
} from "react-icons/fa";

function Navbar() {

  const navigate = useNavigate();

  const username =
    localStorage.getItem("username") || "Farmer";

  const email =
    localStorage.getItem("email") ||
    "farmer@gmail.com";

  const [darkMode, setDarkMode] =
    useState(false);

  const toggleDarkMode = () => {

    setDarkMode(!darkMode);

    document.body.classList.toggle(
      "dark-theme"
    );

  };

  const logout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("username");

    navigate("/login");

  };

  return (

<nav
className="navbar navbar-expand-lg navbar-dark shadow"
style={{
background:
"linear-gradient(90deg,#1B5E20,#2E7D32,#43A047)"
}}
>

<div className="container-fluid px-4">

<Link
className="navbar-brand fw-bold fs-3"
to="/"
>

<FaLeaf className="me-2"/>

FarmBuddy AI

</Link>

<button
className="navbar-toggler"
type="button"
data-bs-toggle="collapse"
data-bs-target="#navbarNav"
>

<span className="navbar-toggler-icon"></span>

</button>

<div
className="collapse navbar-collapse"
id="navbarNav"
>

<ul className="navbar-nav ms-auto align-items-center">

{/* Dashboard */}

<li className="nav-item">

<NavLink
to="/"
className={({isActive}) =>
isActive
?
"nav-link active-link"
:
"nav-link"
}
>

Dashboard

</NavLink>

</li>

{/* Profile */}

<li className="nav-item">

<NavLink
to="/profile"
className={({isActive}) =>
isActive
?
"nav-link active-link"
:
"nav-link"
}
>

<FaUser className="me-1"/>

Profile

</NavLink>

</li>

{/* Crops */}

<li className="nav-item">

<NavLink
to="/crop"
className={({isActive}) =>
isActive
?
"nav-link active-link"
:
"nav-link"
}
>

<FaSeedling className="me-1"/>

Crops

</NavLink>

</li>

{/* Weather */}

<li className="nav-item">

<NavLink
to="/weather"
className={({isActive}) =>
isActive
?
"nav-link active-link"
:
"nav-link"
}
>

<FaCloudSun className="me-1"/>

Weather

</NavLink>

</li>

{/* AI */}

<li className="nav-item">

<NavLink
to="/chat"
className={({isActive}) =>
isActive
?
"nav-link active-link"
:
"nav-link"
}
>

<FaRobot className="me-1"/>

AI Chat

</NavLink>

</li>

{/* Search */}

<li className="nav-item mx-3">

<div className="search-box">

<FaSearch className="search-icon"/>

<input
type="text"
placeholder="Search..."
className="form-control"
/>

</div>

</li>

{/* Tractor */}

<li className="nav-item dropdown">

<a
href="#"
className="nav-link dropdown-toggle"
data-bs-toggle="dropdown"
>

<FaTractor className="me-1"/>

Tractors

</a>

<ul className="dropdown-menu shadow">

<li>

<Link
to="/tractors"
className="dropdown-item"
>

🚜 Tractor Marketplace

</Link>

</li>

<li>

<Link
to="/my-tractor-bookings"
className="dropdown-item"
>

📋 My Tractor Bookings

</Link>

</li>

</ul>

</li>

{/* Labor */}

<li className="nav-item dropdown">

<a
href="#"
className="nav-link dropdown-toggle"
data-bs-toggle="dropdown"
>

<FaUsers className="me-1"/>

Labors

</a>

<ul className="dropdown-menu shadow">

<li>

<Link
to="/labors"
className="dropdown-item"
>

👷 Labor Marketplace

</Link>

</li>

<li>

<Link
to="/my-labor-bookings"
className="dropdown-item"
>

📋 My Labor Bookings

</Link>

</li>

</ul>

</li>
            {/* Seeds */}

            <li className="nav-item dropdown">

              <a
                href="#"
                className="nav-link dropdown-toggle"
                data-bs-toggle="dropdown"
              >

                <FaShoppingBasket className="me-1" />

                Seeds

              </a>

              <ul className="dropdown-menu shadow">

                <li>

                  <Link
                    to="/seeds"
                    className="dropdown-item"
                  >

                    🌱 Seed Marketplace

                  </Link>

                </li>

                <li>

                  <Link
                    to="/my-seed-purchases"
                    className="dropdown-item"
                  >

                    🛒 My Seed Purchases

                  </Link>

                </li>

              </ul>

            </li>

            {/* Notification */}

            <li className="nav-item me-3">

              <button
                className="btn position-relative text-white"
              >

                <FaBell size={20} />

                <span className="notification-count position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">

                  3

                </span>

              </button>

            </li>

            {/* Language */}

            <li className="nav-item dropdown me-3">

              <a
                href="#"
                className="nav-link"
                data-bs-toggle="dropdown"
              >

                <FaGlobe size={20} />

              </a>

              <ul className="dropdown-menu dropdown-menu-end">

                <li>

                  <button className="dropdown-item">

                    🇮🇳 Hindi

                  </button>

                </li>

                <li>

                  <button className="dropdown-item">

                    🇬🇧 English

                  </button>

                </li>

              </ul>

            </li>

            {/* Dark Mode */}

            <li className="nav-item me-3">

              <button
                className="btn btn-light rounded-circle"
                onClick={toggleDarkMode}
              >

                {

                  darkMode ?

                  <FaSun color="#FFC107"/>

                  :

                  <FaMoon/>

                }

              </button>

            </li>

            {/* My Account */}

            <li className="nav-item dropdown">

              <a
                href="#"
                className="nav-link dropdown-toggle d-flex align-items-center"
                data-bs-toggle="dropdown"
              >

                <div className="position-relative">

                  <FaUserCircle
                    size={36}
                  />

                  <span className="online-dot"></span>

                </div>

                <span className="ms-2">

                  {username}

                </span>

              </a>

              <ul className="dropdown-menu dropdown-menu-end profile-dropdown shadow">

                <div className="profile-header">

                  <FaUserCircle
                    size={80}
                    className="profile-avatar"
                  />

                  <h5>

                    {username}

                  </h5>

                  <p>

                    {email}

                  </p>

                  <span className="badge bg-success">

                    <FaCheckCircle className="me-1"/>

                    Verified Farmer

                  </span>

                </div>

                <li>

                  <hr className="dropdown-divider"/>

                </li>

                <li>

                  <Link
                    className="dropdown-item"
                    to="/"
                  >

                    <FaTachometerAlt className="me-2"/>

                    Dashboard

                  </Link>

                </li>

                <li>

                  <Link
                    className="dropdown-item"
                    to="/profile"
                  >

                    <FaUser className="me-2"/>

                    Profile

                  </Link>

                </li>

                <li>

                  <Link
                    className="dropdown-item"
                    to="/chat"
                  >

                    <FaEnvelope className="me-2"/>

                    Messages

                  </Link>

                </li>

                <li>

                  <Link
                    className="dropdown-item"
                    to="/favorites"
                  >

                    <FaStar className="me-2"/>

                    Favorites

                  </Link>

                </li>

                <li>

                  <Link
                    className="dropdown-item"
                    to="/settings"
                  >

                    <FaCog className="me-2"/>

                    Settings

                  </Link>

                </li>

                <li>

                  <hr className="dropdown-divider"/>

                </li>

                <li>

                  <button
                    className="dropdown-item logout-btn"
                    onClick={logout}
                  >

                    <FaSignOutAlt className="me-2"/>

                    Logout

                  </button>

                </li>

              </ul>

            </li>

          </ul>

        </div>

      </div>

    </nav>

  );

}

export default Navbar;