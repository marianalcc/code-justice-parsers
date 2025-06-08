"""
icc_parser.py
Extracts basic info from ICC rulings (text files).
Outputs structured JSON for further analysis.
"""

import spacy
import json

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Load the ICC case (must be plain text)
with open("sample_icc_case.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Analyze the text using spaCy
doc = nlp(text)

# Extract people, dates, and violations
people = set()
dates = set()
violations = []

for ent in doc.ents:
    if ent.label_ == "PERSON":
        people.add(ent.text)
    elif ent.label_ == "DATE":
        dates.add(ent.text)

# Example: Find lines mentioning violations
for line in text.split("\n"):
    if "violation" in line.lower() or "article" in line.lower():
        violations.append(line.strip())

# Format as dictionary
case_data = {
    "case_name": doc.ents[0].text if doc.ents else "Unknown",
    "people_involved": list(people),
    "dates": list(dates),
    "violations": violations
}

# Save as JSON
with open("parsed_icc_case.json", "w", encoding="utf-8") as out_file:
    json.dump(case_data, out_file, indent=4)

print("✅ Case parsed and saved to parsed_icc_case.json")


