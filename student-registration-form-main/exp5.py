# Medical Symptom Checker
# Experiment 5 - AI Agent with Reasoning

# Knowledge Base
rules = [
    {
        "symptoms": ["fever", "cough", "body_pain"],
        "disease": "Flu"
    },
    {
        "symptoms": ["cough", "sore_throat", "runny_nose"],
        "disease": "Common Cold"
    },
    {
        "symptoms": ["fever", "breathing_difficulty"],
        "disease": "Pneumonia"
    },
    {
        "symptoms": ["stomach_pain", "vomiting", "diarrhea"],
        "disease": "Food Poisoning"
    }
]

# Get patient symptoms
patient = {}

patient["fever"] = input("Do you have fever? (yes/no): ").lower() == "yes"
patient["cough"] = input("Do you have cough? (yes/no): ").lower() == "yes"
patient["body_pain"] = input("Do you have body pain? (yes/no): ").lower() == "yes"
patient["sore_throat"] = input("Do you have sore throat? (yes/no): ").lower() == "yes"
patient["runny_nose"] = input("Do you have runny nose? (yes/no): ").lower() == "yes"
patient["breathing_difficulty"] = input("Do you have breathing difficulty? (yes/no): ").lower() == "yes"
patient["stomach_pain"] = input("Do you have stomach pain? (yes/no): ").lower() == "yes"
patient["vomiting"] = input("Do you have vomiting? (yes/no): ").lower() == "yes"
patient["diarrhea"] = input("Do you have diarrhea? (yes/no): ").lower() == "yes"

# Reasoning
possible_illnesses = []

print("\nReasoning Process:")

for rule in rules:

    matched = True

    for symptom in rule["symptoms"]:
        if not patient.get(symptom, False):
            matched = False
            break

    if matched:
        possible_illnesses.append(rule["disease"])

        print(
            " + ".join(rule["symptoms"]),
            "->",
            rule["disease"],
            "(Rule Matched)"
        )

# Display result
print("\nPossible illnesses:")

if possible_illnesses:
    for illness in possible_illnesses:
        print("-", illness)
else:
    print("No matching illness found.")

print("\nNote: This is an educational rule-based system, not a medical diagnosis.")