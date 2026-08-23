import React, { useEffect, useState } from "react";

import { getMyLaborBookings } from "../api/laborBookingApi";

function MyLaborBookings() {

  const [bookings, setBookings] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const loadBookings = async () => {

    try {

      setLoading(true);

      const data = await getMyLaborBookings();

      setBookings(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Failed to load labor bookings.");

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    loadBookings();

  }, []);

  if (loading) {

    return (

      <div className="container mt-5 text-center">

        <div
          className="spinner-border text-success"
          role="status"
        ></div>

        <h5 className="mt-3">

          Loading Labor Bookings...

        </h5>

      </div>

    );

  }

  return (

    <div className="container mt-4">

      <h2 className="fw-bold mb-4">

        👷 My Labor Bookings

      </h2>

      {error && (

        <div className="alert alert-danger">

          {error}

        </div>

      )}

      {bookings.length === 0 ? (

        <div className="alert alert-warning">

          No labor bookings found.

        </div>

      ) : (

        <div className="table-responsive">

          <table className="table table-bordered table-hover">

            <thead className="table-success">

              <tr>

                <th>ID</th>

                <th>Labor</th>

                <th>Start Date</th>

                <th>Days</th>

                <th>Total Amount</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              {bookings.map((booking) => (

                <tr key={booking.id}>

                  <td>{booking.id}</td>

                  <td>

                    {booking.labor_name ||
                      booking.labor?.full_name ||
                      booking.labor_id}

                  </td>

                  <td>{booking.start_date}</td>

                  <td>{booking.number_of_days}</td>

                  <td>

                    ₹{booking.total_amount}

                  </td>

                  <td>

                    <span
                      className={`badge ${
                        booking.status === "Approved"

                          ? "bg-success"

                          : booking.status === "Pending"

                          ? "bg-warning text-dark"

                          : booking.status === "Cancelled"

                          ? "bg-danger"

                          : "bg-secondary"
                      }`}
                    >

                      {booking.status}

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

export default MyLaborBookings;