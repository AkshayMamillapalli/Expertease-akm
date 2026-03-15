def diagnose(symptoms):
    rules = [
        {
            "if": ["fever", "cough", "weakness"],
            "then": "Common Cold",
            "explanation": "A mild viral infection that causes runny nose, cough, and low fever.",
            "causes": "Caused by viruses (mostly rhinoviruses) spread through air droplets or contact.",
            "precautions": ["Wash hands regularly", "Stay hydrated", "Avoid close contact with sick people"],
            "medicines": ["Paracetamol", "Antihistamines", "Cough syrup"]
        },
        {
            "if": ["fever", "headache", "nausea", "vomiting"],
            "then": "Typhoid",
            "explanation": "A bacterial infection spread through contaminated food or water, leading to high fever.",
            "causes": "Caused by Salmonella typhi bacteria, spread via unsafe water or food.",
            "precautions": ["Drink clean water", "Wash hands", "Avoid street food"],
            "medicines": ["Antibiotics (Ciprofloxacin, Azithromycin)", "Paracetamol", "ORS"]
        },
        {
            "if": ["fever", "chills", "sweating", "headache"],
            "then": "Malaria",
            "explanation": "A mosquito-borne disease causing cycles of fever, chills, and sweating.",
            "causes": "Caused by Plasmodium parasites transmitted through Anopheles mosquitoes.",
            "precautions": ["Use mosquito nets", "Apply repellents", "Avoid stagnant water"],
            "medicines": ["Chloroquine", "Artemisinin-based drugs", "Paracetamol"]
        },
        {
            "if": ["fever", "cough", "chest pain", "breathing difficulty"],
            "then": "Pneumonia",
            "explanation": "An infection that inflames the air sacs in the lungs, making breathing painful.",
            "causes": "Caused by bacteria, viruses, or fungi infecting the lungs.",
            "precautions": ["Get vaccinated", "Avoid smoking", "Maintain hygiene"],
            "medicines": ["Antibiotics (Amoxicillin)", "Cough syrup", "Pain relievers"]
        },
        {
            "if": ["fever", "rash", "runny nose", "red eyes"],
            "then": "Measles",
            "explanation": "A highly contagious viral disease with rash, fever, and cold-like symptoms.",
            "causes": "Caused by measles virus, spread by coughing and sneezing.",
            "precautions": ["Get vaccinated (MMR)", "Avoid contact with infected people", "Boost immunity"],
            "medicines": ["Vitamin A supplements", "Paracetamol", "Fluids"]
        },
        {
            "if": ["fever", "sore throat", "swollen glands"],
            "then": "Tonsillitis",
            "explanation": "Swelling of the tonsils, often causing sore throat and difficulty swallowing.",
            "causes": "Caused by viral or bacterial infections affecting the tonsils.",
            "precautions": ["Avoid sharing utensils", "Maintain oral hygiene", "Drink warm fluids"],
            "medicines": ["Antibiotics (if bacterial)", "Pain relievers", "Warm salt water gargle"]
        },
        {
            "if": ["fever", "fatigue", "muscle pain", "dry cough"],
            "then": "Influenza (Flu)",
            "explanation": "A viral infection causing sudden fever, body aches, and dry cough.",
            "causes": "Caused by influenza viruses, spread through droplets.",
            "precautions": ["Get flu vaccine", "Cover mouth while coughing", "Rest and hydrate"],
            "medicines": ["Antiviral drugs (Oseltamivir)", "Paracetamol", "Cough syrup"]
        },
        {
            "if": ["fever", "loss of taste", "loss of smell", "cough"],
            "then": "COVID-19",
            "explanation": "A viral respiratory illness causing fever, cough, and loss of smell/taste.",
            "causes": "Caused by SARS-CoV-2 virus, transmitted via droplets and surfaces.",
            "precautions": ["Wear masks", "Maintain social distance", "Get vaccinated"],
            "medicines": ["Paracetamol", "Antivirals (if prescribed)", "Vitamin C/Zinc"]
        },
        {
            "if": ["blisters", "itching", "tiredness"],
            "then": "Chickenpox",
            "explanation": "A viral infection that causes itchy blisters all over the body.",
            "causes": "Caused by varicella-zoster virus, spread via droplets.",
            "precautions": ["Isolate infected person", "Keep nails trimmed", "Avoid scratching"],
            "medicines": ["Calamine lotion", "Antihistamines", "Paracetamol"]
        },
        {
            "if": ["stomach pain", "diarrhea", "vomiting"],
            "then": "Food Poisoning",
            "explanation": "Illness caused by contaminated food, leading to stomach upset and diarrhea.",
            "causes": "Caused by bacteria, viruses, or toxins in contaminated food/water.",
            "precautions": ["Eat fresh food", "Wash vegetables properly", "Avoid street food"],
            "medicines": ["ORS", "Antibiotics (if bacterial)", "Probiotics"]
        },
        {
            "if": ["abdominal pain", "bloating", "gas"],
            "then": "Irritable Bowel Syndrome (IBS)",
            "explanation": "A digestive disorder causing stomach pain, bloating, and irregular bowel habits.",
            "causes": "Caused by abnormal gut function, stress, or diet triggers.",
            "precautions": ["Eat fiber-rich food", "Reduce stress", "Avoid trigger foods"],
            "medicines": ["Antispasmodics", "Laxatives", "Probiotics"]
        },
        {
            "if": ["burning chest pain", "acid reflux"],
            "then": "GERD (Acid Reflux)",
            "explanation": "A condition where stomach acid flows back into the food pipe causing heartburn.",
            "causes": "Caused by weakened lower esophageal sphincter, obesity, or poor diet.",
            "precautions": ["Avoid spicy foods", "Don’t lie down after eating", "Maintain healthy weight"],
            "medicines": ["Antacids", "Proton pump inhibitors (Omeprazole)", "H2 blockers"]
        },
        {
            "if": ["excessive thirst", "frequent urination", "fatigue"],
            "then": "Diabetes",
            "explanation": "A condition where blood sugar levels are too high due to lack of insulin control.",
            "causes": "Caused by low insulin production (Type 1) or insulin resistance (Type 2).",
            "precautions": ["Eat balanced diet", "Exercise regularly", "Monitor blood sugar"],
            "medicines": ["Insulin (Type 1)", "Metformin", "Sulfonylureas"]
        },
        {
            "if": ["chest pain", "shortness of breath", "sweating"],
            "then": "Heart Disease",
            "explanation": "A range of conditions affecting the heart, often linked with poor blood flow.",
            "causes": "Caused by blocked arteries, high blood pressure, or lifestyle factors.",
            "precautions": ["Avoid smoking", "Exercise regularly", "Eat low-fat diet"],
            "medicines": ["Aspirin", "Beta blockers", "Statins"]
        },
        {
            "if": ["high blood pressure", "headache", "dizziness"],
            "then": "Hypertension",
            "explanation": "A condition where blood pressure is too high, putting strain on the heart.",
            "causes": "Caused by obesity, stress, high salt intake, or genetics.",
            "precautions": ["Eat low-salt diet", "Exercise daily", "Manage stress"],
            "medicines": ["ACE inhibitors", "Diuretics", "Calcium channel blockers"]
        },
        {
            "if": ["headache", "sensitivity to light", "nausea"],
            "then": "Migraine",
            "explanation": "A severe headache often accompanied by nausea and sensitivity to light.",
            "causes": "Caused by brain activity changes, triggers include stress, food, or hormones.",
            "precautions": ["Avoid trigger foods", "Sleep regularly", "Reduce stress"],
            "medicines": ["Triptans", "NSAIDs", "Antiemetics"]
        },
        {
            "if": ["memory loss", "confusion", "difficulty speaking"],
            "then": "Stroke",
            "explanation": "A sudden interruption of blood supply to the brain, causing confusion or paralysis.",
            "causes": "Caused by blocked or burst blood vessels in the brain.",
            "precautions": ["Control blood pressure", "Avoid smoking", "Exercise regularly"],
            "medicines": ["Aspirin", "Clot-busting drugs", "Blood thinners"]
        },
        {
            "if": ["seizures", "confusion", "loss of awareness"],
            "then": "Epilepsy",
            "explanation": "A neurological disorder causing repeated seizures or sudden loss of awareness.",
            "causes": "Caused by abnormal brain activity, genetics, or head injury.",
            "precautions": ["Take medication regularly", "Avoid triggers", "Get enough sleep"],
            "medicines": ["Carbamazepine", "Valproate", "Levetiracetam"]
        },
        {
            "if": ["joint pain", "swelling", "stiffness"],
            "then": "Arthritis",
            "explanation": "A condition that causes inflammation of joints, leading to pain and stiffness.",
            "causes": "Caused by joint wear-and-tear (osteoarthritis) or immune attack (rheumatoid arthritis).",
            "precautions": ["Exercise regularly", "Maintain healthy weight", "Avoid injury"],
            "medicines": ["NSAIDs", "Corticosteroids", "DMARDs"]
        },
        {
            "if": ["fatigue", "weight gain", "hair loss"],
            "then": "Hypothyroidism",
            "explanation": "A condition where the thyroid gland does not produce enough hormones.",
            "causes": "Caused by autoimmune disease, iodine deficiency, or thyroid surgery.",
            "precautions": ["Eat iodine-rich foods", "Regular thyroid checkups", "Take medication regularly"],
            "medicines": ["Levothyroxine"]
        },
        {
            "if": ["fatigue", "shortness of breath", "pale skin"],
            "then": "Anemia",
            "explanation": "A condition where the body lacks enough healthy red blood cells.",
            "causes": "Caused by iron deficiency, chronic diseases, or blood loss.",
            "precautions": ["Eat iron-rich foods", "Avoid heavy bleeding", "Take supplements"],
            "medicines": ["Iron supplements", "Vitamin B12", "Folic acid"]
        }
    ]

    symptoms = [s.lower().strip() for s in symptoms]

    possible_diagnoses = []

    for rule in rules:
        overlap = set(rule["if"]).intersection(set(symptoms))
        if overlap:
            possible_diagnoses.append({
                "disease": rule["then"],
                "explanation": rule["explanation"],
                "causes": rule["causes"],
                "precautions": rule["precautions"],
                "medicines": rule["medicines"],
                "matched": list(overlap)
            })

    if len(possible_diagnoses) > 0:
        return possible_diagnoses
    elif len(symptoms) == 0:
        return [{"disease": "None", "explanation": "No symptoms provided. Please enter some symptoms."}]
    else:
        return [{"disease": "Unknown", "explanation": "No clear diagnosis found. Please consult a doctor."}]


if __name__ == "__main__":
    test_symptoms = ["fever", "cough"]
    results = diagnose(test_symptoms)
    for r in results:
        print(f"{r['disease']}: {r['explanation']}")
        print(f"Causes: {r['causes']}")
        print(f"Precautions: {', '.join(r['precautions'])}")
        print(f"Medicines: {', '.join(r['medicines'])}")
        print(f"Matched Symptoms: {', '.join(r['matched'])}")
        print("-" * 50)
