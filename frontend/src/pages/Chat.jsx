import { useState } from "react";
import api from "../api/axios";
import Navbar from "../components/Navbar";

function Chat() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askAI = async () => {

    if (!question) return;

    setLoading(true);

    try {

      const token = localStorage.getItem("token");

      const response = await api.post(
        "/api/chat/",
        {
          question: question
        },
        {
          headers: {
            Authorization: `Bearer ${token}`
          }
        }
      );

      setAnswer(response.data.answer);

    } catch (error) {

      alert(
        error.response?.data?.detail ||
        "AI Error"
      );

    }

    setLoading(false);

  };

  return (

    <>
      <Navbar />

      <div className="container mt-5">

        <h2>🤖 FarmBuddy AI Chat</h2>

        <textarea
          className="form-control mt-3"
          rows="5"
          placeholder="Ask your farming question..."
          value={question}
          onChange={(e)=>setQuestion(e.target.value)}
        />

        <button
          className="btn btn-success mt-3"
          onClick={askAI}
        >

          {
            loading
            ?
            "Thinking..."
            :
            "Ask AI"
          }

        </button>

        {
          answer &&
          <div className="card mt-4 shadow">

            <div className="card-body">

              <h4>Answer</h4>

              <hr/>

              <p>{answer}</p>

            </div>

          </div>
        }

      </div>

    </>

  );

}

export default Chat;