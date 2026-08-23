import {

PieChart,
Pie,
Cell,
Tooltip,
Legend,
ResponsiveContainer

} from "recharts";

const COLORS = [

"#16a34a",
"#f59e0b",
"#3b82f6",
"#ef4444",
"#8b5cf6"

];

function CropDistributionChart({ data }) {

return (

<div className="card shadow-sm border-0 rounded-4">

<div className="card-body">

<h5 className="fw-bold mb-4">

Crop Distribution

</h5>

<ResponsiveContainer width="100%" height={320}>

<PieChart>

<Pie

data={data}

dataKey="value"

nameKey="name"

outerRadius={110}

label

>

{

data.map((entry,index)=>(

<Cell

key={index}

fill={COLORS[index%COLORS.length]}

/>

))

}

</Pie>

<Tooltip/>

<Legend/>

</PieChart>

</ResponsiveContainer>

</div>

</div>

);

}

export default CropDistributionChart;