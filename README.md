# AYUSH Disease Mapping System

Simple Flask backend + HTML frontend for mapping AYUSH diseases to FHIR format with NAMASTE and ICD codes.

## 📁 Project Structure
```
AYUSH API/
├── app.py              # Flask API server
├── mappings.json       # Disease mappings data  
├── requirements.txt    # Python dependencies
├── index.html          # Web interface
└── README.md          # This file
```

## 🚀 How to Run

### Step 1: Install Flask
```bash
pip install -r requirements.txt
```

### Step 2: Start Backend Server
```bash
python app.py
```
✅ Server runs at: `http://127.0.0.1:5000`

### Step 3: Open Frontend
Double-click `index.html` to open in your browser

### Step 4: Test the System
1. Input disease name (e.g., "Amavata")
2. Click "Map Disease to FHIR"
3. View FHIR JSON result

## Available Diseases to Test
- Amavata
- Sandhigata Vata
- Madhumeha
- Pandu
- Yakrit Roga
- Jwara
- Kasa
- Swasa

## 🔗 API Endpoint
- **POST** `/map_disease`
- **Input**: `{"disease": "Amavata"}`
- **Output**: FHIR JSON with NAMASTE + ICD mapping

That's it! 
