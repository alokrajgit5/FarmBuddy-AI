import React, { useEffect, useMemo, useState } from "react";

import { getAllTractors } from "../api/tractorApi";
import { createBooking } from "../api/tractorBookingApi";

import TractorCard from "../components/TractorCard";
import BookingModal from "../components/BookingModal";

function Tractor() {
  const [tractors, setTractors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("");

  const [showModal, setShowModal] = useState(false);
  const [selectedTractor, setSelectedTractor] = useState(null);

  const loadTractors = async () => {
    try {
      setLoading(true);

      const data = await getAllTractors();

      setTractors(data);

      setError("");
    } catch (err) {
      console.error(err);
      setError("Failed to load tractors.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTractors();
  }, []);

  const filteredTractors = useMemo(() => {
    let list = [...tractors];

    if (search.trim() !== "") {
      list = list.filter(
        (tractor) =>
          tractor.tractor_name
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||
          tractor.brand
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||
          tractor.location
            ?.toLowerCase()
            .includes(search.toLowerCase())
      );
    }

    if (sort === "low") {
      list.sort(
        (a, b) => a.price_per_day - b.price_per_day
      );
    }

    if (sort === "high") {
      list.sort(
        (a, b) => b.price_per_day - a.price_per_day
      );
    }

    return list;
  }, [tractors, search, sort]);

  const handleBook = (tractor) => {
    setSelectedTractor(tractor);
    setShowModal(true);
  };

  const confirmBooking = async (bookingData) => {
    try {
      await createBooking(bookingData);

      alert("✅ Tractor booked successfully.");

      setShowModal(false);
      setSelectedTractor(null);

    } catch (err) {
      console.error(err);

      alert("❌ Booking failed.");
    }
  };

  if (loading) {
    return (
      <div className="container mt-5 text-center">
        <div
          className="spinner-border text-success"
          role="status"
        ></div>

        <h5 className="mt-3">
          Loading Tractors...
        </h5>
      </div>
    );
  }

  return (
    <>
      <div className="container mt-4">

        <div className="d-flex justify-content-between align-items-center mb-4">

          <h2 className="fw-bold">
            🚜 Tractor Marketplace
          </h2>

        </div>

        <div className="row mb-4">

          <div className="col-md-8 mb-3">

            <input
              type="text"
              className="form-control"
              placeholder="Search by tractor, brand or location..."
              value={search}
              onChange={(e) =>
                setSearch(e.target.value)
              }
            />

          </div>

          <div className="col-md-4">

            <select
              className="form-select"
              value={sort}
              onChange={(e) =>
                setSort(e.target.value)
              }
            >
              <option value="">
                Sort By Price
              </option>

              <option value="low">
                Low → High
              </option>

              <option value="high">
                High → Low
              </option>

            </select>

          </div>

        </div>

        {error && (
          <div className="alert alert-danger">
            {error}
          </div>
        )}

        {filteredTractors.length === 0 ? (

          <div className="alert alert-warning">

            No tractors found.

          </div>

        ) : (

          <div className="row">

            {filteredTractors.map((tractor) => (

              <div
                className="col-lg-4 col-md-6 mb-4"
                key={tractor.id}
              >

                <TractorCard
                  tractor={tractor}
                  onBook={handleBook}
                />

              </div>

            ))}

          </div>

        )}

      </div>

      <BookingModal
        show={showModal}
        tractor={selectedTractor}
        onClose={() => {
          setShowModal(false);
          setSelectedTractor(null);
        }}
        onConfirm={confirmBooking}
      />
    </>
  );
}

export default Tractor;