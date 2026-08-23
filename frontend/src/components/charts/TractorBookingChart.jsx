import {

BarChart,
Bar,
XAxis,
YAxis,
Tooltip,
CartesianGrid,
ResponsiveContainer

} from "recharts";

function TractorBookingChart({ data }) {

return (

<div className="card shadow-sm border-0 rounded-4">

<div className="card-body">

<h5 className="fw-bold mb-4">

Monthly Tractor Bookings

</h5>

<ResponsiveContainer width="100%" height={320}>

<BarChart data={data}>

<CartesianGrid strokeDasharray="3 3"/>

<XAxis dataKey="month"/>

<YAxis/>

<Tooltip/>

<Bar

dataKey="bookings"

fill="#22c55e"

radius={[10,10,0,0]}

/>

</BarChart>

</ResponsiveContainer>

</div>

</div>

);

}

export default TractorBookingChart;