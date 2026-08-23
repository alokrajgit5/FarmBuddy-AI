import { useState } from "react";
import api from "../api/axios";

import VoiceButton from "../components/VoiceButton";
import { speakText } from "../utils/speech";

function VoiceAssistant() {

  const [question, setQuestion] = useState("");

  const [answer, setAnswer] = useState("");

  const [loading, setLoading] = useState(false);

  const askAI = async () => {

    if (!question.trim()) return;

    setLoading(true);

    try {

      const response = await api.post(
        "/api/chat/",
        {
          question: question
        }
      );

      setAnswer(response.data.answer);

    } catch (error) {

      setAnswer(
        "⚠️ AI service is temporarily unavailable."
      );

    }

    setLoading(false);

  };

  return (

    <div className="container mt-5">

      <h2 className="mb-4">
        🎤 FarmBuddy Voice Assistant
      </h2>

      <div className="mb-3">

        <textarea

          className="form-control"

          rows="4"

          placeholder="Ask anything about farming..."

          value={question}

          onChange={(e) =>
            setQuestion(e.target.value)
          }

        />

      </div>

      <div className="d-flex gap-2 mb-3">

        <VoiceButton
          onText={(text) => setQuestion(text)}
        />

        <button
          className="btn btn-primary"
          onClick={askAI}
          disabled={loading}
        >

          {

            loading

              ? "Thinking..."

              : "Ask AI"

          }

        </button>

      </div>

      {

        answer && (

          <div className="card shadow">

            <div className="card-body">

              <h5>🤖 AI Answer</h5>

              <hr />

              <p>{answer}</p>

              <button
                className="btn btn-success"
                onClick={() => speakText(answer)}
              >

                🔊 Speak Response

              </button>

            </div>

          </div>

        )

      }

    </div>

  );

}

export default VoiceAssistant;