import React from "react";

function LaborCard({ labor, onHire }) {
  return (
    <div className="card shadow-sm h-100 border-0">

      <img
        src={
          labor.image_url ||
          "https://via.placeholder.com/400x250?text=Labor"
        }
        className="card-img-top"
        alt={labor.full_name}
        style={{
          height: "220px",
          objectFit: "cover"
        }}
      />

      <div className="card-body">

        <h5 className="fw-bold">
          👷 {labor.full_name}
        </h5>

        <p className="mb-2">
          <strong>Experience :</strong>{" "}
          {labor.experience} Years
        </p>

        <p className="mb-2">
          <strong>Location :</strong>{" "}
          📍 {labor.location}
        </p>

        <p className="mb-2">
          <strong>Skill :</strong>{" "}
          {labor.skill}
        </p>

        <p className="mb-2">
          <strong>Daily Wage :</strong>{" "}
          <span className="text-success fw-bold">
            ₹{labor.daily_wage}/day
          </span>
        </p>

        <p className="mb-3">
          <strong>Status :</strong>

          {labor.available ? (
            <span className="badge bg-success ms-2">
              Available
            </span>
          ) : (
            <span className="badge bg-danger ms-2">
              Busy
            </span>
          )}
        </p>

        <button
          className="btn btn-success w-100"
          disabled={!labor.available}
          onClick={() => onHire(labor)}
        >
          👷 Hire Now
        </button>

      </div>

    </div>
  );
}

export default LaborCard;