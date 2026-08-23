import "./ProfileStats.css";

import {
  FaTractor,
  FaSeedling,
  FaTint,
  FaUserGraduate,
  FaHome,
  FaAward
} from "react-icons/fa";

function ProfileStats({ profile }) {

  const level =
    profile.experience >= 10
      ? "Gold Farmer"
      : profile.experience >= 5
      ? "Silver Farmer"
      : "Bronze Farmer";

  return (

    <div className="row g-4 mb-4">

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaTractor
            className="stat-icon"
          />

          <h6>Total Land</h6>

          <h4>

            {profile.land_area || 0}

          </h4>

        </div>

      </div>

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaSeedling
            className="stat-icon"
          />

          <h6>Main Crop</h6>

          <h5>

            {profile.main_crop || "-"}

          </h5>

        </div>

      </div>

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaTint
            className="stat-icon"
          />

          <h6>Irrigation</h6>

          <h5>

            {profile.irrigation || "-"}

          </h5>

        </div>

      </div>

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaUserGraduate
            className="stat-icon"
          />

          <h6>Experience</h6>

          <h4>

            {profile.experience || 0} Yr

          </h4>

        </div>

      </div>

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaHome
            className="stat-icon"
          />

          <h6>Village</h6>

          <h5>

            {profile.village || "-"}

          </h5>

        </div>

      </div>

      <div className="col-lg-2 col-md-4 col-6">

        <div className="profile-stat-card">

          <FaAward
            className="stat-icon"
          />

          <h6>Level</h6>

          <h5>

            {level}

          </h5>

        </div>

      </div>

    </div>

  );

}

export default ProfileStats;