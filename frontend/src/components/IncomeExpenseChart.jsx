import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";


function IncomeExpenseChart({ data = [] }) {

  /*
   * Backend format:
   *
   * [
   *   {
   *     month: "Jan",
   *     income: 0,
   *     expense: 0
   *   },
   *   ...
   * ]
   */


  const chartData = Array.isArray(data)
    ? data.map((item) => ({
        month: item?.month || "",
        income: Number(item?.income || 0),
        expense: Number(item?.expense || 0),
      }))
    : [];


  return (

    <div className="card premium-card h-100">

      <div className="card-body">

        <div className="d-flex justify-content-between align-items-center mb-3">

          <div>

            <h4 className="fw-bold mb-1">
              Income vs Expenses
            </h4>

            <p className="text-muted mb-0">
              Monthly financial overview
            </p>

          </div>

        </div>


        {chartData.length === 0 ? (

          <div
            className="d-flex justify-content-center align-items-center text-muted"
            style={{
              height: "320px",
            }}
          >

            No financial data available.

          </div>

        ) : (

          <div
            style={{
              width: "100%",
              height: "320px",
            }}
          >

            <ResponsiveContainer
              width="100%"
              height="100%"
            >

              <BarChart
                data={chartData}
                margin={{
                  top: 10,
                  right: 10,
                  left: 0,
                  bottom: 10,
                }}
              >

                <CartesianGrid
                  strokeDasharray="3 3"
                  opacity={0.2}
                />


                <XAxis
                  dataKey="month"
                />


                <YAxis
                  allowDecimals={false}
                />


                <Tooltip />


                <Legend />


                <Bar
                  dataKey="income"
                  name="Income"
                  fill="#16a34a"
                  radius={[6, 6, 0, 0]}
                />


                <Bar
                  dataKey="expense"
                  name="Expenses"
                  fill="#dc2626"
                  radius={[6, 6, 0, 0]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        )}

      </div>

    </div>

  );

}


export default IncomeExpenseChart;