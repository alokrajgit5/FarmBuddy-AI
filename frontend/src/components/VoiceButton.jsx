import { useState } from "react";
import { FaMicrophone } from "react-icons/fa";
import { startListening } from "../utils/speech";

function VoiceButton({ onText }) {

  const [listening, setListening] = useState(false);

  const handleVoice = () => {

    setListening(true);

    startListening((text) => {

      onText(text);

      setListening(false);

    });

  };

  return (

    <button
      className={`btn ${
        listening ? "btn-danger" : "btn-success"
      }`}
      onClick={handleVoice}
    >

      <FaMicrophone />

      {" "}

      {

        listening

          ? "Listening..."

          : "Speak"

      }

    </button>

  );

}

export default VoiceButton;