import "./DashboardAnalytics.css";

import {
  FaCalendarCheck,
  FaRupeeSign,
  FaWallet,
  FaLeaf,
  FaRobot
} from "react-icons/fa";

function DashboardAnalytics({ dashboard }) {

  const analytics = [

    {
      title: "Bookings This Month",
      value: dashboard.bookings_this_month,
      icon: <FaCalendarCheck />,
      color: "analytics-green"
    },

    {
      title: "Income",
      value: `₹${dashboard.income}`,
      icon: <FaRupeeSign />,
      color: "analytics-blue"
    },

    {
      title: "Expenses",
      value: `₹${dashboard.expenses}`,
      icon: <FaWallet />,
      color: "analytics-orange"
    },

    {
      title: "Crop Health",
      value: `${dashboard.crop_health}%`,
      icon: <FaLeaf />,
      color: "analytics-olive"
    },

    {
      title: "AI Score",
      value: `${dashboard.ai_score}%`,
      icon: <FaRobot />,
      color: "analytics-purple"
    }

  ];

  return (

    <div className="row mt-4">

      {analytics.map((item, index) => (

        <div
          className="col-lg col-md-6 mb-4"
          key={index}
        >

          <div className={`analytics-card ${item.color}`}>

            <div className="analytics-icon">

              {item.icon}

            </div>

            <div>

              <h6>{item.title}</h6>

              <h3>{item.value}</h3>

            </div>

          </div>

        </div>

      ))}

    </div>

  );

}

export default DashboardAnalytics;