import React, { useEffect, useMemo, useState } from "react";

import { getAllSeeds } from "../api/seedApi";
import { buySeed } from "../api/seedPurchaseApi";

import SeedCard from "../components/SeedCard";
import SeedBuyModal from "../components/SeedBuyModal";

function SeedMarketplace() {

  const [seeds, setSeeds] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [search, setSearch] = useState("");
  const [sort, setSort] = useState("");

  const [showModal, setShowModal] = useState(false);
  const [selectedSeed, setSelectedSeed] = useState(null);

  const loadSeeds = async () => {

    try {

      setLoading(true);

      const data = await getAllSeeds();

      setSeeds(data);

      setError("");

    } catch (err) {

      console.error(err);

      setError("Failed to load seeds.");

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    loadSeeds();

  }, []);

  const filteredSeeds = useMemo(() => {

    let list = [...seeds];

    if (search.trim() !== "") {

      list = list.filter(

        (seed) =>

          seed.seed_name
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||

          seed.brand
            ?.toLowerCase()
            .includes(search.toLowerCase()) ||

          seed.category
            ?.toLowerCase()
            .includes(search.toLowerCase())

      );

    }

    if (sort === "low") {

      list.sort(

        (a, b) =>

          a.price - b.price

      );

    }

    if (sort === "high") {

      list.sort(

        (a, b) =>

          b.price - a.price

      );

    }

    return list;

  }, [seeds, search, sort]);

  const handleBuy = (seed) => {

    setSelectedSeed(seed);

    setShowModal(true);

  };

  const confirmPurchase = async (purchaseData) => {

    try {

      await buySeed(purchaseData);

      alert("✅ Seed purchased successfully.");

      setShowModal(false);

      setSelectedSeed(null);

      loadSeeds();

    } catch (err) {

      console.error(err);

      alert("❌ Purchase failed.");

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

          Loading Seeds...

        </h5>

      </div>

    );

  }

  return (

    <>

      <div className="container mt-4">

        <div className="d-flex justify-content-between align-items-center mb-4">

          <h2 className="fw-bold">

            🌱 Seed Marketplace

          </h2>

        </div>

        <div className="row mb-4">

          <div className="col-md-8 mb-3">

            <input

              type="text"

              className="form-control"

              placeholder="Search by seed name, brand or category..."

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

        {filteredSeeds.length === 0 ? (

          <div className="alert alert-warning">

            No seeds found.

          </div>

        ) : (

          <div className="row">

            {filteredSeeds.map((seed) => (

              <div
                className="col-lg-4 col-md-6 mb-4"
                key={seed.id}
              >

                <SeedCard

                  seed={seed}

                  onBuy={handleBuy}

                />

              </div>

            ))}

          </div>

        )}

      </div>

      <SeedBuyModal

        show={showModal}

        seed={selectedSeed}

        onClose={() => {

          setShowModal(false);

          setSelectedSeed(null);

        }}

        onConfirm={confirmPurchase}

      />

    </>

  );

}

export default SeedMarketplace;