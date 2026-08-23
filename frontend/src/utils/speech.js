// frontend/src/utils/speech.js

export const startListening = (onResult) => {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert("Speech Recognition is not supported in this browser.");
    return null;
  }

  const recognition = new SpeechRecognition();

  recognition.lang = "hi-IN";
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    onResult(transcript);
  };

  recognition.onerror = (event) => {
    console.log("Speech Error:", event.error);
  };

  recognition.start();

  return recognition;
};

export const speakText = (text) => {
  if (!window.speechSynthesis) {
    alert("Text-to-Speech is not supported.");
    return;
  }

  const utterance = new SpeechSynthesisUtterance(text);

  utterance.lang = "hi-IN";
  utterance.rate = 1;
  utterance.pitch = 1;

  window.speechSynthesis.speak(utterance);
};