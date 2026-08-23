import "./RecentActivity.css";

import {
  FaTractor,
  FaUsers,
  FaSeedling
} from "react-icons/fa";

function RecentActivity({ activities }) {

  const getIcon = (type) => {

    switch (type) {

      case "tractor":
        return <FaTractor className="activity-icon tractor" />;

      case "labor":
        return <FaUsers className="activity-icon labor" />;

      case "seed":
        return <FaSeedling className="activity-icon seed" />;

      default:
        return <FaSeedling className="activity-icon" />;

    }

  };

  return (

    <div className="activity-card">

      <h3 className="activity-title">

        Recent Activities

      </h3>

      <div className="activity-list">

        {activities?.length > 0 ? (

          activities.map((item, index) => (

            <div
              className="activity-item"
              key={index}
            >

              {getIcon(item.type)}

              <div className="activity-content">

                <h5>{item.title}</h5>

                <p>{item.description}</p>

                <span>{item.date}</span>

              </div>

            </div>

          ))

        ) : (

          <h5>No Recent Activity</h5>

        )}

      </div>

    </div>

  );

}

export default RecentActivity;