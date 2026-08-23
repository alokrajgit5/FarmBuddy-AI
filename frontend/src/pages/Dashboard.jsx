import { useEffect, useState } from "react";
import api from "../api/axios";

import DashboardLayout from "../layouts/DashboardLayout";

import "../styles/dashboard.css";

import HeroSection from "../components/HeroSection";
import DashboardStats from "../components/DashboardStats";
import DashboardAnalytics from "../components/DashboardAnalytics";
import WeatherCard from "../components/WeatherCard";
import MonthlyBookingChart from "../components/MonthlyBookingChart";
import RecentActivity from "../components/RecentActivity";
import CropHealthCard from "../components/CropHealthCard";
import IncomeExpenseChart from "../components/IncomeExpenseChart";

import {
  FaChartLine,
  FaRobot,
} from "react-icons/fa";


function Dashboard() {

  const [dashboard, setDashboard] = useState(null);
  const [loading, setLoading] = useState(true);


  useEffect(() => {

    fetchDashboard();

  }, []);


  const fetchDashboard = async () => {

    try {

      const token = localStorage.getItem("token");

      if (!token) {

        console.error("JWT token not found.");

        setDashboard(null);

        return;

      }


      const response = await api.get(
        "/api/dashboard/",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );


      console.log(
        "Dashboard API Response:",
        response.data
      );


      setDashboard(response.data);


    } catch (error) {

      console.error(
        "Dashboard API Error:",
        error
      );


      alert(
        error.response?.data?.detail ||
        "Failed to load dashboard."
      );


      setDashboard(null);


    } finally {

      setLoading(false);

    }

  };


  /* =========================================
     Loading
  ========================================= */

  if (loading) {

    return (

      <div className="container text-center py-5">

        <div
          className="spinner-border text-success"
          role="status"
        />

        <h4 className="mt-3 text-success">
          Loading Dashboard...
        </h4>

      </div>

    );

  }


  /* =========================================
     Failed
  ========================================= */

  if (!dashboard) {

    return (

      <div className="container text-center py-5">

        <h3 className="text-danger">
          Failed to load dashboard.
        </h3>

        <button
          className="btn btn-success mt-3"
          onClick={() => {
            setLoading(true);
            fetchDashboard();
          }}
        >
          Retry
        </button>

      </div>

    );

  }


  /* =========================================
     Safe Dashboard Data
  ========================================= */

  const incomeExpenseData =
    dashboard.income_expense_chart || [];


  const recentActivities =
    dashboard.recent_activities || [];


  const weather =
    dashboard.weather || {};


  const aiTip =
    dashboard.ai_tip || "No AI recommendation available.";


  const marketPrice =
    dashboard.market_price || "Coming Soon";


  /* =========================================
     Render Dashboard
  ========================================= */

  return (

    <DashboardLayout dashboard={dashboard}>

      <div className="container-fluid px-4 py-4 dashboard-page">


        {/* =====================================
            Hero
        ===================================== */}

        <HeroSection
          dashboard={dashboard}
        />


        {/* =====================================
            Dashboard Stats
        ===================================== */}

        <DashboardStats
          dashboard={dashboard}
        />


        {/* =====================================
            Analytics
        ===================================== */}

        <DashboardAnalytics
          dashboard={dashboard}
        />


        {/* =====================================
            Monthly Booking Chart
        ===================================== */}

        <MonthlyBookingChart
          dashboard={dashboard}
        />


        {/* =====================================
            Charts Row
        ===================================== */}

        <div className="row">


          {/* Income / Expense */}

          <div className="col-lg-6 mb-4">

            <IncomeExpenseChart
              data={incomeExpenseData}
            />

          </div>


          {/* Crop Health */}

          <div className="col-lg-6 mb-4">

            <CropHealthCard
              dashboard={dashboard}
            />

          </div>


        </div>


        {/* =====================================
            Weather + Market
        ===================================== */}

        <div className="row">


          {/* Weather */}

          <div className="col-lg-6 mb-4">

            <WeatherCard
              weather={weather}
            />

          </div>


          {/* Market Price */}

          <div className="col-lg-6 mb-4">

            <div className="card premium-card h-100">

              <div className="card-body">

                <h4 className="fw-bold">

                  <FaChartLine
                    className="me-2 text-success"
                  />

                  Market Price

                </h4>


                <hr />


                <h2 className="text-success">

                  {marketPrice}

                </h2>

              </div>

            </div>

          </div>


        </div>


        {/* =====================================
            Recent Activities
        ===================================== */}

        <RecentActivity
          activities={recentActivities}
        />


        {/* =====================================
            AI Recommendation
        ===================================== */}

        <div className="card premium-card mb-5">

          <div className="card-body">

            <h3 className="fw-bold">

              <FaRobot
                className="me-2 text-primary"
              />

              Today's AI Recommendation

            </h3>


            <hr />


            <p
              className="fs-5"
              style={{
                lineHeight: "1.8",
              }}
            >

              {aiTip}

            </p>

          </div>

        </div>


      </div>

    </DashboardLayout>

  );

}


export default Dashboard;