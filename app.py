from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load mappings from JSON file
def load_mappings():
    try:
        with open('mappings.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

@app.route('/map_disease', methods=['POST'])
def map_disease():
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data or 'disease' not in data:
            return jsonify({
                "error": "Invalid request. Please provide 'disease' field in JSON."
            }), 400
        
        disease_name = data['disease'].strip()
        
        if not disease_name:
            return jsonify({
                "error": "Disease name cannot be empty."
            }), 400
        
        # Load mappings
        mappings = load_mappings()
        
        # Look for the disease (case-insensitive)
        disease_mapping = None
        for key, value in mappings.items():
            if key.lower() == disease_name.lower():
                disease_mapping = value
                break
        
        if not disease_mapping:
            return jsonify({
                "error": f"Disease '{disease_name}' not found in mappings.",
                "available_diseases": list(mappings.keys())
            }), 404
        
        # Create FHIR-compliant response
        fhir_response = {
            "resourceType": "Condition",
            "id": f"condition-{disease_name.lower().replace(' ', '-')}",
            "meta": {
                "versionId": "1",
                "lastUpdated": "2024-01-01T00:00:00Z",
                "source": "AYUSH-Disease-Mapping-System"
            },
            "status": "active",
            "category": [
                {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/condition-category",
                            "code": "encounter-diagnosis",
                            "display": "Encounter Diagnosis"
                        }
                    ]
                }
            ],
            "code": {
                "coding": [
                    {
                        "system": "http://namaste.gov.in/ayush-terminology",
                        "code": disease_mapping.get("namaste_code", ""),
                        "display": disease_name
                    }
                ]
            },
            "subject": {
                "reference": "Patient/example-patient"
            },
            "extension": [
                {
                    "url": "http://namaste.gov.in/ayush-mapping",
                    "valueCodeableConcept": {
                        "coding": [
                            {
                                "system": "http://namaste.gov.in/ayush-codes",
                                "code": disease_mapping.get("namaste_code", ""),
                                "display": disease_mapping.get("namaste_description", "")
                            }
                        ]
                    }
                }
            ]
        }
        
        # Add ICD mapping if available
        if disease_mapping.get("icd_code"):
            fhir_response["code"]["coding"].append({
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": disease_mapping["icd_code"],
                "display": disease_mapping.get("icd_description", "")
            })
        
        return jsonify(fhir_response), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Internal server error: {str(e)}"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "message": "AYUSH Disease Mapping API is running"
    }), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "AYUSH Disease Mapping API",
        "endpoints": {
            "/map_disease": "POST - Map AYUSH disease to FHIR format",
            "/health": "GET - Health check"
        }
    }), 200

if __name__ == '__main__':
    print("Starting AYUSH Disease Mapping API...")
    print("API will be available at: http://127.0.0.1:5000")
    print("Endpoints:")
    print("  POST /map_disease - Map disease to FHIR format")
    print("  GET /health - Health check")
    app.run(debug=True, host='127.0.0.1', port=5000)
