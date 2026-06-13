# Dictionary App

A dictionary web app that returns definitions, phonetics, parts of speech,
and example sentences for any English word.

## Tech Stack
- Python
- FastAPI (backend API server)
- Streamlit (frontend UI)
- Free Dictionary API (dictionaryapi.dev)

## Features
- Search any English word
- Displays phonetic pronunciation
- Shows all meanings grouped by part of speech
- Example sentences for each definition
- Error handling for unknown words

## How to Run

### 1. Start the FastAPI backend
```bash
pip install fastapi uvicorn httpx
uvicorn main:app --reload
```

### 2. Start the Streamlit frontend
```bash
pip install streamlit requests
streamlit run app.py
```

### 3. Open your browser
