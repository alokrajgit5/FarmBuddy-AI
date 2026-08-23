import {
  FaCloudSun,
  FaRobot,
  FaNewspaper,
  FaMapMarkerAlt,
  FaTint,
  FaWind
} from "react-icons/fa";

import "./RightSidebar.css";

function RightSidebar({ dashboard }) {

  return (

    <div className="right-sidebar">

      {/* Weather */}

      <div className="weather-widget">

        <div className="weather-top">

          <h4>

            <FaCloudSun />

            Live Weather

          </h4>

          <span className="live-badge">

            LIVE

          </span>

        </div>

        <p className="location">

          <FaMapMarkerAlt />

          {dashboard.weather.city}

        </p>

        <h1>

          {dashboard.weather.temperature}°C

        </h1>

        <h5>

          {dashboard.weather.status}

        </h5>

        <div className="weather-details">

          <div>

            <FaTint />

            <span>

              {dashboard.weather.humidity}%

            </span>

          </div>

          <div>

            <FaWind />

            <span>

              {dashboard.weather.wind_speed} km/h

            </span>

          </div>

        </div>

        <small>

          Updated {dashboard.weather.updated_at}

        </small>

      </div>

      {/* AI */}

      <div className="ai-widget">

        <div className="widget-title">

          <FaRobot />

          AI Recommendation

        </div>

        <div className="chat-box">

          {dashboard.ai_tip}

        </div>

      </div>

      {/* News */}

      <div className="news-widget">

        <div className="widget-title">

          <FaNewspaper />

          Farming Tips

        </div>

        <ul>

          <li>🌾 Use certified seeds</li>

          <li>💧 Irrigate in morning</li>

          <li>🌱 Check crop health weekly</li>

          <li>🚜 Book tractors early</li>

        </ul>

      </div>

    </div>

  );

}

export default RightSidebar;