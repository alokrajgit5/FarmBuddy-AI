import {
  FaHome,
  FaUser,
  FaSeedling,
  FaCloudSun,
  FaRobot,
  FaTractor,
  FaUsers,
  FaShoppingBasket,
  FaClipboardList,
  FaEnvelope,
  FaHeart,
  FaWallet,
  FaChartBar,
  FaCog,
  FaSignOutAlt,
  FaCrown
} from "react-icons/fa";

import "./Sidebar.css";

function Sidebar() {

  return (

    <aside className="sidebar">

      {/* Farmer */}

      <div className="sidebar-profile">

        <img
          src="/images/farmer.png"
          alt="farmer"
        />

        <h4>Farmer</h4>

        <span className="verified">

          ● Verified Farmer

        </span>

        <span className="online">

          ● Online

        </span>

      </div>

      {/* Menu */}

      <ul className="sidebar-menu">

        <li className="active">

          <FaHome />

          Dashboard

        </li>

        <li>

          <FaUser />

          Profile

        </li>

        <li>

          <FaSeedling />

          Crops

        </li>

        <li>

          <FaCloudSun />

          Weather

        </li>

        <li>

          <FaRobot />

          AI Chat

        </li>

        <li>

          <FaTractor />

          Tractors

        </li>

        <li>

          <FaUsers />

          Labors

        </li>

        <li>

          <FaShoppingBasket />

          Seeds

        </li>

        <li>

          <FaClipboardList />

          My Bookings

        </li>

        <li>

          <FaEnvelope />

          Messages

        </li>

        <li>

          <FaHeart />

          Favorites

        </li>

        <li>

          <FaWallet />

          Payments

        </li>

        <li>

          <FaChartBar />

          Reports

        </li>

        <li>

          <FaCog />

          Settings

        </li>

        <li className="logout">

          <FaSignOutAlt />

          Logout

        </li>

      </ul>

      {/* Premium */}

      <div className="upgrade-card">

        <img

          src="/images/farmer-premium.png"

          alt="premium"

        />

        <h5>

          <FaCrown />

          Go Premium

        </h5>

        <p>

          Unlock AI Farming Features

        </p>

        <button>

          Upgrade

        </button>

      </div>

    </aside>

  );

}

export default Sidebar;