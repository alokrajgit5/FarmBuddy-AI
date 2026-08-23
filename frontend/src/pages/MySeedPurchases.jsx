import React, { useEffect, useState } from "react";

import { getMySeedPurchases } from "../api/seedPurchaseApi";

function MySeedPurchases() {

  const [purchases, setPurchases] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const loadPurchases = async () => {

    try {

      setLoading(true);

      const data = await getMySeedPurchases();

      setPurchases(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Failed to load seed purchases.");

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    loadPurchases();

  }, []);

  if (loading) {

    return (

      <div className="container mt-5 text-center">

        <div
          className="spinner-border text-success"
          role="status"
        ></div>

        <h5 className="mt-3">

          Loading Seed Purchases...

        </h5>

      </div>

    );

  }

  return (

    <div className="container mt-4">

      <h2 className="fw-bold mb-4">

        🌱 My Seed Purchases

      </h2>

      {error && (

        <div className="alert alert-danger">

          {error}

        </div>

      )}

      {purchases.length === 0 ? (

        <div className="alert alert-warning">

          No seed purchases found.

        </div>

      ) : (

        <div className="table-responsive">

          <table className="table table-bordered table-hover">

            <thead className="table-success">

              <tr>

                <th>ID</th>

                <th>Seed</th>

                <th>Purchase Date</th>

                <th>Quantity</th>

                <th>Total Price</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              {purchases.map((purchase) => (

                <tr key={purchase.id}>

                  <td>{purchase.id}</td>

                  <td>

                    {purchase.seed_name ||
                      purchase.seed?.seed_name ||
                      purchase.seed_id}

                  </td>

                  <td>

                    {purchase.purchase_date}

                  </td>

                  <td>

                    {purchase.quantity} KG

                  </td>

                  <td>

                    ₹{purchase.total_price}

                  </td>

                  <td>

                    <span
                      className={`badge ${
                        purchase.status === "Completed"

                          ? "bg-success"

                          : purchase.status === "Pending"

                          ? "bg-warning text-dark"

                          : purchase.status === "Cancelled"

                          ? "bg-danger"

                          : "bg-secondary"
                      }`}
                    >

                      {purchase.status}

                    </span>

                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

    </div>

  );

}

export default MySeedPurchases;