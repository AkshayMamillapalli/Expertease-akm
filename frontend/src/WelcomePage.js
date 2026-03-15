import React from "react";
import "./App.css";

function WelcomePage({ onStart }) {
  return (
    <div className="welcome-container">
      <div className="welcome-card">
        <h1>🤖 AI Medical Expert System</h1>
        <p>Get instant medical insights based on your symptoms.</p>
        <button className="start-btn" onClick={onStart}>
          🚀 Start Diagnosis
        </button>
      </div>
    </div>
  );
}

export default WelcomePage;
