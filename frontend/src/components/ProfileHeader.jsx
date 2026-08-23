import "./ProfileHeader.css";
import { FaCamera } from "react-icons/fa";

function ProfileHeader({ profile }) {

  return (

    <div className="profile-header">

      <div className="cover-image">

        <div className="overlay">

          <div className="profile-avatar">

            <img
              src={
                profile?.profile_image ||
                "https://i.pravatar.cc/180?img=12"
              }
              alt="Profile"
            />

            <button>

              <FaCamera />

            </button>

          </div>

          <h2>

            {profile?.farmer_name || "Farmer"}

          </h2>

          <p>

            🌾 Smart Farmer • FarmBuddy AI

          </p>

        </div>

      </div>

    </div>

  );

}

export default ProfileHeader;