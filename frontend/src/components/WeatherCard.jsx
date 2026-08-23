import "./WeatherCard.css";

import {

FaTemperatureHigh,

FaTint,

FaWind,

FaMapMarkerAlt,

FaCloudSun

} from "react-icons/fa";

function WeatherCard({ weather }) {

return (

<div className="weather-card">

<div className="weather-header">

<h3>

<FaCloudSun />

&nbsp;

Live Weather

</h3>

</div>

<div className="weather-main">

<h1>

{weather?.temperature ?? 0}°C

</h1>

<p>

{weather?.status}

</p>

</div>

<div className="weather-grid">

<div>

<FaTint />

<span>

Humidity

</span>

<h4>

{weather?.humidity ?? 0}%

</h4>

</div>

<div>

<FaWind />

<span>

Wind

</span>

<h4>

{weather?.wind_speed ?? 0} km/h

</h4>

</div>

<div>

<FaMapMarkerAlt />

<span>

City

</span>

<h4>

{weather?.city}

</h4>

</div>

</div>

<div className="weather-footer">

Updated

{weather?.updated_at}

</div>

</div>

);

}

export default WeatherCard;