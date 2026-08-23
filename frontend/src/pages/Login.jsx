import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/axios";

function Login() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });

  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {

    setFormData({

      ...formData,

      [e.target.name]: e.target.value

    });

  };

  const handleSubmit = async (e) => {

    e.preventDefault();

    setLoading(true);

    try {

      const response = await api.post(
    "/api/users/login",
    formData
);

console.log("Login Response:", response.data);

localStorage.setItem(
    "token",
    response.data.access_token
);

      alert("Login Successful");

      navigate("/");

    } catch (error) {

      alert(

        error.response?.data?.detail ||

        "Login Failed"

      );

    }

    setLoading(false);

  };

  return (

    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        height: "90vh"
      }}
    >

      <form
        onSubmit={handleSubmit}
        style={{
          width: "350px",
          padding: "30px",
          border: "1px solid #ddd",
          borderRadius: "10px",
          boxShadow: "0 0 10px #ccc"
        }}
      >

        <h2>FarmBuddy Login</h2>

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "15px"
          }}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "15px"
          }}
        />

        <button
          type="submit"
          disabled={loading}
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "20px",
            background: "#2E7D32",
            color: "white",
            border: "none",
            cursor: "pointer"
          }}
        >

          {

            loading

            ?

            "Logging in..."

            :

            "Login"

          }

        </button>

      </form>

    </div>

  );

}

export default Login;