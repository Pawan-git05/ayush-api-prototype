# 🌿 AYUSH Disease Mapping System

A simple Flask backend + HTML frontend for mapping AYUSH diseases to FHIR format with NAMASTE and ICD codes.

## 📁 Project Structure
```
AYUSH API/
├── app.py              # Flask API server (backend)
├── mappings.json       # Disease mappings data  
├── requirements.txt    # Python dependencies
├── index.html          # Web interface (frontend)
├── .gitignore         # Git ignore file
└── README.md          # Instructions
```

## 🚀 How to Run (Follow This Order!)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start Backend Server FIRST 
```bash
python app.py
```
✅ **Backend runs at**: `http://127.0.0.1:5000`  
⚠️ **Important**: Keep this terminal running!

### Step 3: Open Frontend (Choose One Method)

#### Option A: Using VS Code Live Server (Recommended)
1. Install "Live Server" extension in VS Code
2. Right-click on `index.html` in VS Code
3. Select "Open with Live Server"
4. ✅ Frontend opens at: `http://127.0.0.1:5500` (or similar)

#### Option B: Direct File Access
- Double-click `index.html` to open in your browser
- Opens as: `file:///path/to/index.html`

📝 **Note**: Live Server is recommended as it provides a proper HTTP server environment, while direct file access may have CORS limitations in some browsers.

### Step 4: Test the Complete System
1. ✅ Verify "API is online and ready" shows green at the top
2. Enter disease name (e.g., "Amavata") in the input box
3. Click "Map Disease to FHIR" button
4. View the beautiful FHIR JSON result below!

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
