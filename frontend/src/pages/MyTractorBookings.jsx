import React, { useEffect, useState } from "react";

import { getMyBookings } from "../api/tractorBookingApi";

function MyTractorBookings() {

  const [bookings, setBookings] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const loadBookings = async () => {

    try {

      setLoading(true);

      const data = await getMyBookings();

      setBookings(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Failed to load bookings.");

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

          Loading Bookings...

        </h5>

      </div>

    );

  }

  return (

    <div className="container mt-4">

      <h2 className="fw-bold mb-4">

        🚜 My Tractor Bookings

      </h2>

      {error && (

        <div className="alert alert-danger">

          {error}

        </div>

      )}

      {bookings.length === 0 ? (

        <div className="alert alert-warning">

          No bookings found.

        </div>

      ) : (

        <div className="table-responsive">

          <table className="table table-bordered table-hover">

            <thead className="table-success">

              <tr>

                <th>ID</th>

                <th>Tractor</th>

                <th>Start Date</th>

                <th>End Date</th>

                <th>Total Amount</th>

                <th>Status</th>

              </tr>

            </thead>

            <tbody>

              {bookings.map((booking) => (

                <tr key={booking.id}>

                  <td>{booking.id}</td>

                  <td>

                    {booking.tractor_name ||
                      booking.tractor?.tractor_name ||
                      booking.tractor_id}

                  </td>

                  <td>{booking.start_date}</td>

                  <td>{booking.end_date}</td>

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

export default MyTractorBookings;