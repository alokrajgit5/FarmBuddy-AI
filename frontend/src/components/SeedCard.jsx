import React from "react";

function SeedCard({ seed, onBuy }) {

  return (

    <div className="card shadow-sm border-0 h-100">

      <img

        src={
          seed.image_url ||
          "https://via.placeholder.com/400x250?text=Seed"
        }

        className="card-img-top"

        alt={seed.seed_name}

        style={{

          height: "220px",

          objectFit: "cover"

        }}

      />

      <div className="card-body">

        <h5 className="fw-bold">

          🌱 {seed.seed_name}

        </h5>

        <p className="mb-2">

          <strong>Brand :</strong>

          {" "}

          {seed.brand}

        </p>

        <p className="mb-2">

          <strong>Category :</strong>

          {" "}

          {seed.category}

        </p>

        <p className="mb-2">

          <strong>Stock :</strong>

          {" "}

          {seed.quantity} KG

        </p>

        <p className="mb-2">

          <strong>Price :</strong>

          <span className="text-success fw-bold">

            ₹{seed.price}/KG

          </span>

        </p>

        <p className="mb-3">

          <strong>Status :</strong>

          {

            seed.quantity > 0

            ?

            <span className="badge bg-success ms-2">

              Available

            </span>

            :

            <span className="badge bg-danger ms-2">

              Out of Stock

            </span>

          }

        </p>

        <button

          className="btn btn-success w-100"

          disabled={seed.quantity <= 0}

          onClick={() => onBuy(seed)}

        >

          🛒 Buy Now

        </button>

      </div>

    </div>

  );

}

export default SeedCard;