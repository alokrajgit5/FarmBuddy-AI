import React, { useEffect, useMemo, useState } from "react";

import { getAllLabors } from "../api/laborApi";
import { hireLabor } from "../api/laborBookingApi";

import LaborCard from "../components/LaborCard";
import LaborHireModal from "../components/LaborHireModal";

function Labor() {

  const [labors, setLabors] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("");

  const [showModal, setShowModal] = useState(false);
  const [selectedLabor, setSelectedLabor] = useState(null);

  const loadLabors = async () => {

    try {

      setLoading(true);

      const data = await getAllLabors();

      setLabors(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Failed to load labor list.");

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    loadLabors();

  }, []);

  const filteredLabors = useMemo(() => {

    let list = [...labors];

    if (search.trim() !== "") {

      list = list.filter(

        (labor) =>

          labor.full_name
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||

          labor.skill
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||

          labor.location
            ?.toLowerCase()
            .includes(search.toLowerCase())

      );

    }

    if (sort === "low") {

      list.sort(

        (a, b) =>

          a.daily_wage - b.daily_wage

      );

    }

    if (sort === "high") {

      list.sort(

        (a, b) =>

          b.daily_wage - a.daily_wage

      );

    }

    return list;

  }, [labors, search, sort]);

  const handleHire = (labor) => {

    setSelectedLabor(labor);

    setShowModal(true);

  };

  const confirmHire = async (hireData) => {

    try {

      await hireLabor(hireData);

      alert("✅ Labor hired successfully.");

      setShowModal(false);

      setSelectedLabor(null);

    } catch (err) {

      console.error(err);

      alert("❌ Hiring failed.");

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

          Loading Labors...

        </h5>

      </div>

    );

  }

  return (

    <>

      <div className="container mt-4">

        <div className="d-flex justify-content-between align-items-center mb-4">

          <h2 className="fw-bold">

            👷 Labor Marketplace

          </h2>

        </div>

        <div className="row mb-4">

          <div className="col-md-8 mb-3">

            <input

              type="text"

              className="form-control"

              placeholder="Search by name, skill or location..."

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
                Sort By Daily Wage
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

        {filteredLabors.length === 0 ? (

          <div className="alert alert-warning">

            No labor found.

          </div>

        ) : (

          <div className="row">

            {filteredLabors.map((labor) => (

              <div
                className="col-lg-4 col-md-6 mb-4"
                key={labor.id}
              >

                <LaborCard

                  labor={labor}

                  onHire={handleHire}

                />

              </div>

            ))}

          </div>

        )}

      </div>

      <LaborHireModal

        show={showModal}

        labor={selectedLabor}

        onClose={() => {

          setShowModal(false);

          setSelectedLabor(null);

        }}

        onConfirm={confirmHire}

      />

    </>

  );

}

export default Labor;