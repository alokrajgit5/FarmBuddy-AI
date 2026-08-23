import { useState } from "react";
import { useNavigate } from "react-router-dom";

import api from "../api/axios";

function Register() {

  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
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

      await api.post(
        "/api/users/register",
        formData
      );

      alert("Registration Successful");

      navigate("/login");

    } catch (error) {

      alert(

        error.response?.data?.detail ||

        "Registration Failed"

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
          width: "380px",
          padding: "30px",
          border: "1px solid #ddd",
          borderRadius: "10px",
          boxShadow: "0 0 10px #ccc"
        }}
      >

        <h2>FarmBuddy Register</h2>

        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={formData.full_name}
          onChange={handleChange}
          required
          style={{
            width: "100%",
            padding: "10px",
            marginTop: "15px"
          }}
        />

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

            "Creating Account..."

            :

            "Register"

          }

        </button>

      </form>

    </div>

  );

}

export default Register;