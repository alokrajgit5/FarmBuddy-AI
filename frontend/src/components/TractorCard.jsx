import React from "react";

function TractorCard({ tractor, onBook }) {
  return (
    <div className="card shadow-sm h-100 border-0">

      <img
        src={
          tractor.image_url ||
          "https://via.placeholder.com/400x250?text=Tractor"
        }
        className="card-img-top"
        alt={tractor.tractor_name}
        style={{
          height: "220px",
          objectFit: "cover"
        }}
      />

      <div className="card-body">

        <h5 className="card-title fw-bold">
          🚜 {tractor.tractor_name}
        </h5>

        <p className="mb-2">
          <strong>Brand :</strong> {tractor.brand}
        </p>

        <p className="mb-2">
          <strong>Model :</strong> {tractor.model}
        </p>

        <p className="mb-2">
          <strong>Location :</strong> 📍 {tractor.location}
        </p>

        <p className="mb-2">
          <strong>Price :</strong>

          <span className="text-success fw-bold">
            ₹{tractor.price_per_day}/day
          </span>
        </p>

        <p className="mb-3">

          <strong>Status :</strong>

          {tractor.available ? (

            <span className="badge bg-success ms-2">

              Available

            </span>

          ) : (

            <span className="badge bg-danger ms-2">

              Booked

            </span>

          )}

        </p>

        <button
          className="btn btn-success w-100"
          disabled={!tractor.available}
          onClick={() => onBook(tractor)}
        >
          🚜 Book Now
        </button>

      </div>

    </div>
  );
}

export default TractorCard;