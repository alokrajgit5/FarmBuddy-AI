import { useEffect, useState } from "react";
import api from "../api/axios";

import ProfileCompletion from "../components/ProfileCompletion";
import ProfileStats from "../components/ProfileStats";

import {
  FaUserCircle,
  FaPhone,
  FaMapMarkerAlt,
  FaSeedling,
  FaTint,
  FaTractor,
  FaEdit,
  FaSave
} from "react-icons/fa";

function Profile() {

  const [profile, setProfile] = useState({
    phone: "",
    state: "",
    district: "",
    village: "",
    land_area: "",
    soil_type: "",
    main_crop: "",
    irrigation: "",
    experience: "",
    bio: "",
    profile_image: ""
  });

  const [isUpdate, setIsUpdate] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {

    try {

      const token = localStorage.getItem("token");

      const response = await api.get(
        "/api/profile/me",
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      setProfile(response.data);
      setIsUpdate(true);

    } catch (error) {

      console.log("Profile not found.");

    } finally {

      setLoading(false);

    }

  };

  const handleChange = (e) => {

    setProfile({
      ...profile,
      [e.target.name]: e.target.value
    });

  };

  const saveProfile = async () => {

    try {

      const token = localStorage.getItem("token");

      if (isUpdate) {

        await api.put(
          "/api/profile/update",
          profile,
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        alert("✅ Profile Updated Successfully");

      } else {

        await api.post(
          "/api/profile/create",
          profile,
          {
            headers: {
              Authorization: `Bearer ${token}`
            }
          }
        );

        alert("✅ Profile Created Successfully");
        setIsUpdate(true);

      }

    } catch (error) {

      alert(
        error.response?.data?.detail ||
        "Something went wrong."
      );

    }

  };

  if (loading) {

    return (

      <div className="container text-center mt-5">

        <div
          className="spinner-border text-success"
          role="status"
        ></div>

        <h4 className="mt-3">

          Loading Profile...

        </h4>

      </div>

    );

  }

  return (

    <div className="container py-4">

      {/* Header */}

      <div
        className="rounded-4 p-4 mb-4 shadow"
        style={{
          background:
            "linear-gradient(135deg,#355E3B,#5D8A4A,#7BA05B)",
          color: "white"
        }}
      >

        <div className="row align-items-center">

          <div className="col-md-2 text-center">

            <FaUserCircle size={120} />

          </div>

          <div className="col-md-10">

            <h2 className="fw-bold">

              👨‍🌾 Farmer Profile

            </h2>

            <p className="mb-0">

              Manage your farming information and keep your FarmBuddy AI account updated.

            </p>

          </div>

        </div>

      </div>

      {/* Profile Completion */}

      <ProfileCompletion profile={profile} />

      {/* Profile Statistics */}

      <ProfileStats profile={profile} />

      {/* Profile Form */}

      <div className="card shadow-lg border-0 rounded-4 mt-4">

        <div className="card-body p-4">

          <div className="row">

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                <FaPhone className="me-2 text-success"/>

                Phone

              </label>

              <input
                className="form-control"
                name="phone"
                value={profile.phone}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                <FaMapMarkerAlt className="me-2 text-danger"/>

                State

              </label>

              <input
                className="form-control"
                name="state"
                value={profile.state}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                District

              </label>

              <input
                className="form-control"
                name="district"
                value={profile.district}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                Village

              </label>

              <input
                className="form-control"
                name="village"
                value={profile.village}
                onChange={handleChange}
              />

            </div>
                        <div className="col-md-6 mb-3">

              <label className="fw-bold">

                <FaTractor className="me-2 text-warning"/>

                Land Area

              </label>

              <input
                className="form-control"
                name="land_area"
                value={profile.land_area}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                Soil Type

              </label>

              <input
                className="form-control"
                name="soil_type"
                value={profile.soil_type}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                <FaSeedling className="me-2 text-success"/>

                Main Crop

              </label>

              <input
                className="form-control"
                name="main_crop"
                value={profile.main_crop}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                <FaTint className="me-2 text-primary"/>

                Irrigation

              </label>

              <input
                className="form-control"
                name="irrigation"
                value={profile.irrigation}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-6 mb-3">

              <label className="fw-bold">

                Experience

              </label>

              <input
                className="form-control"
                name="experience"
                value={profile.experience}
                onChange={handleChange}
              />

            </div>

            <div className="col-md-12 mb-3">

              <label className="fw-bold">

                About Farmer

              </label>

              <textarea
                rows="5"
                className="form-control"
                name="bio"
                value={profile.bio}
                onChange={handleChange}
              />

            </div>

          </div>

          <div className="text-end mt-4">

            <button
              className="btn btn-success btn-lg px-5"
              onClick={saveProfile}
            >

              {isUpdate ? (

                <>

                  <FaEdit className="me-2"/>

                  Update Profile

                </>

              ) : (

                <>

                  <FaSave className="me-2"/>

                  Create Profile

                </>

              )}

            </button>

          </div>

        </div>

      </div>

    </div>

  );

}

export default Profile;