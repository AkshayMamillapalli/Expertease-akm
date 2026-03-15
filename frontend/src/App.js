import React, { useState } from "react";
import "./App.css";

function App() {
  const [page, setPage] = useState("home");
  const [symptoms, setSymptoms] = useState([]);
  const [inputSymptom, setInputSymptom] = useState("");
  const [result, setResult] = useState(null);
  const [selectedDisease, setSelectedDisease] = useState(null);

  const suggestedSymptoms = [
    "fever", "cough", "headache", "weakness", "nausea", "vomiting",
    "chills", "sweating", "chest pain", "breathing difficulty", "rash",
    "runny nose", "red eyes", "sore throat", "swollen glands", "fatigue",
    "muscle pain", "dry cough", "loss of taste", "loss of smell",
    "blisters", "itching", "tiredness", "stomach pain", "diarrhea",
    "abdominal pain", "bloating", "gas", "acid reflux", "excessive thirst",
    "frequent urination", "dizziness", "memory loss", "confusion",
    "difficulty speaking", "seizures", "joint pain", "swelling", "stiffness",
    "weight gain", "hair loss", "pale skin"
  ];

  const handleAddSymptom = () => {
    if (inputSymptom.trim() !== "" && !symptoms.includes(inputSymptom.toLowerCase())) {
      setSymptoms([...symptoms, inputSymptom.toLowerCase()]);
      setInputSymptom("");
    }
  };

  const handleSuggestionClick = (symptom) => {
    if (!symptoms.includes(symptom)) {
      setSymptoms([...symptoms, symptom]);
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("https://expertease-backend.onrender.com/diagnose", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptoms }),
      });

      const data = await response.json();
      setResult(data.diagnosis);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  if (page === "home") {
    return (
      <div className="home-container">
        <h1>Welcome to the Medical Expert System</h1>
        <p>Your AI-based health assistant for basic disease predictions.</p>
        <button className="start-btn" onClick={() => setPage("diagnose")}>
          🚀 Start Diagnosis
        </button>
      </div>
    );
  }

  if (page === "details" && selectedDisease) {
    return (
      <div className="details-container">
        <button className="back-btn" onClick={() => setPage("diagnose")}>⬅ Back</button>
        <h2>{selectedDisease.disease}</h2>
        <p><b>Explanation:</b> {selectedDisease.explanation}</p>
        <p><b>Causes:</b> {selectedDisease.causes}</p>
        <p><b>Precautions:</b></p>
        <ul>
          {selectedDisease.precautions.map((p, i) => <li key={i}>{p}</li>)}
        </ul>
        <p><b>Medicines:</b></p>
        <ul>
          {selectedDisease.medicines.map((m, i) => <li key={i}>{m}</li>)}
        </ul>
        <em>Matched symptoms: {selectedDisease.matched.join(", ")}</em>
      </div>
    );
  }

  return (
    <div className="container">
      <h1>Medical Expert System</h1>
      <p>Select symptoms from suggestions or add your own:</p>

      <div className="input-box">
        <input
          type="text"
          value={inputSymptom}
          onChange={(e) => setInputSymptom(e.target.value)}
          placeholder="Enter a symptom..."
        />
        <button onClick={handleAddSymptom}>Add Symptom</button>
      </div>
      <br></br>
      <div className="selected-symptoms">
        <strong>Selected Symptoms:</strong> {symptoms.join(", ") || "None"}
      </div>

      <div className="suggestions">
        {suggestedSymptoms.map((symptom, index) => (
          <button
            key={index}
            className="suggestion-btn"
            onClick={() => handleSuggestionClick(symptom)}
          >
            {symptom}
          </button>
        ))}
      </div>

      <button className="diagnose-btn" onClick={handleSubmit}>Diagnose</button>

      {result && result.length > 0 && (
        <div className="results">
          <h2>Possible Diagnoses:</h2>
          {result.map((item, index) => (
            <div
              key={index}
              className="diagnosis-card clickable"
              onClick={() => {
                setSelectedDisease(item);
                setPage("details");
              }}
            >
              <strong>{item.disease}</strong>
              <p>{item.explanation}</p>
              <small>Click for more details ➡</small>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
