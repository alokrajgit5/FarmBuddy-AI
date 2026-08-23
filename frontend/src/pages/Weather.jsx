import { useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

function Weather() {

  const [city, setCity] = useState("");

  const [weather, setWeather] = useState(null);

  const searchWeather = async () => {

    try {

      const response = await api.get(`/api/weather/${city}`);

      setWeather(response.data);

    } catch (error) {

      alert("City not found");

    }

  };

  return (

    <>
      <Navbar />

      <div className="container mt-5">

        <div className="card shadow">

          <div className="card-header bg-primary text-white">

            <h3>🌦 Live Weather</h3>

          </div>

          <div className="card-body">

            <div className="input-group">

              <input
                className="form-control"
                placeholder="Enter City Name"
                value={city}
                onChange={(e) => setCity(e.target.value)}
              />

              <button
                className="btn btn-success"
                onClick={searchWeather}
              >
                Search
              </button>

            </div>

            {weather && (

              <div className="mt-4">

                <h3>📍 {weather.city}</h3>

                <hr />

                <h5>🌡 Temperature : {weather.temperature} °C</h5>

                <h5>💧 Humidity : {weather.humidity}%</h5>

                <h5>☁ Weather : {weather.weather}</h5>

                <h5>📝 Description : {weather.description}</h5>

                <h5>💨 Wind Speed : {weather.wind_speed} m/s</h5>

              </div>

            )}

          </div>

        </div>

      </div>

    </>

  );

}

export default Weather;