from flask import Flask, request, jsonify
from flask_cors import CORS
import expert_system
import os


app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Medical Expert System API is running"})

@app.route("/diagnose", methods=["POST"])
def diagnose():
    try:
        data = request.get_json()
        symptoms = data.get("symptoms", [])

        diagnosis = expert_system.diagnose(symptoms)

        formatted_diagnosis = []
        for d in diagnosis:
            formatted_diagnosis.append({
                "disease": d.get("disease", ""),
                "explanation": d.get("explanation", ""),
                "causes": d.get("causes", ""),
                "precautions": d.get("precautions", []),
                "medicines": d.get("medicines", []),
                "matched": d.get("matched", [])
            })

        return jsonify({"diagnosis": formatted_diagnosis})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
