import "./DashboardStats.css";

import {
  FaTractor,
  FaUsers,
  FaShoppingBasket,
  FaMoneyBillWave,
  FaClipboardList
} from "react-icons/fa";

function DashboardStats({ dashboard }) {

  const stats = [
    {
      title: "Total Bookings",
      value: dashboard.total_bookings || 0,
      icon: <FaClipboardList />,
      color: "green-card"
    },
    {
      title: "Tractor Bookings",
      value: dashboard.tractor_bookings || 0,
      icon: <FaTractor />,
      color: "brown-card"
    },
    {
      title: "Labor Bookings",
      value: dashboard.labor_bookings || 0,
      icon: <FaUsers />,
      color: "blue-card"
    },
    {
      title: "Seed Purchases",
      value: dashboard.seed_purchases || 0,
      icon: <FaShoppingBasket />,
      color: "orange-card"
    },
    {
      title: "Total Spending",
      value: `₹${dashboard.total_spending || 0}`,
      icon: <FaMoneyBillWave />,
      color: "purple-card"
    }
  ];

  return (

    <div className="row g-4 dashboard-stats-row">

      {stats.map((item, index) => (

        <div
          className="col-xl col-lg-4 col-md-6"
          key={index}
        >

          <div className={`stats-card ${item.color}`}>

            <div className="stats-top">

              <div className="stats-icon">

                {item.icon}

              </div>

            </div>

            <div className="stats-title">

              {item.title}

            </div>

            <div className="stats-value">

              {item.value}

            </div>

            <div className="stats-growth">

              ▲ +12% this month

            </div>
           <div className="stats-sparkline">

              <span></span>
              <span></span>
              <span></span>
              <span></span>
              <span></span>

            </div>

          </div>

        </div>

      ))}

    </div>

  );

}

export default DashboardStats;