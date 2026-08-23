import {
  ResponsiveContainer,
  LineChart,
  Line,
  CartesianGrid,
  Tooltip,
  Legend,
  XAxis,
  YAxis
} from "recharts";

function IncomeExpenseChart({ data }) {

  return (

    <div className="card shadow-sm border-0 rounded-4">

      <div className="card-body">

        <h5 className="fw-bold mb-4">

          Income vs Expense

        </h5>

        <ResponsiveContainer
          width="100%"
          height={320}
        >

          <LineChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Legend />

            <Line

              type="monotone"

              dataKey="income"

              stroke="#16a34a"

              strokeWidth={3}

            />

            <Line

              type="monotone"

              dataKey="expense"

              stroke="#ef4444"

              strokeWidth={3}

            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </div>

  );

}

export default IncomeExpenseChart;