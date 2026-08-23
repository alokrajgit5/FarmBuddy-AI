import {

AreaChart,
Area,
XAxis,
YAxis,
Tooltip,
CartesianGrid,
ResponsiveContainer

} from "recharts";

function MonthlyActivityChart({ data }) {

return (

<div className="card shadow-sm border-0 rounded-4">

<div className="card-body">

<h5 className="fw-bold mb-4">

Monthly Activity

</h5>

<ResponsiveContainer width="100%" height={320}>

<AreaChart data={data}>

<CartesianGrid strokeDasharray="3 3"/>

<XAxis dataKey="month"/>

<YAxis/>

<Tooltip/>

<Area

type="monotone"

dataKey="activity"

stroke="#2563eb"

fill="#93c5fd"

/>

</AreaChart>

</ResponsiveContainer>

</div>

</div>

);

}

export default MonthlyActivityChart;