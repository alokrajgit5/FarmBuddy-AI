import {

  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid

} from "recharts";

function MonthlyBookingChart({ dashboard }) {

  return (

    <div className="card shadow-lg border-0 rounded-4 mt-4">

      <div className="card-body">

        <h4 className="fw-bold mb-4">

          📈 Monthly Bookings

        </h4>

        <ResponsiveContainer
          width="100%"
          height={350}
        >

          <BarChart
            data={dashboard.monthly_booking_graph}
          >

            <CartesianGrid
              strokeDasharray="3 3"
            />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="count"
              radius={[10,10,0,0]}
              fill="#4CAF50"
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>

  );

}

export default MonthlyBookingChart;