# Behavioural Anomaly Detection System
FYP — University of Lahore | Team: Umar Farooq, Muhammad Zain, Zarnab Waheed

## Quick Start

### 1. Backend
```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy ..\\.env.example ..\\.env
uvicorn main:app --reload
```
API docs -> http://localhost:8000/docs

### 2. Frontend
```
cd frontend
npm install
npm run dev
```
App -> http://localhost:5173

### 3. Detection
```
python detect_realtime.py --camera 0 --camera-id 1
```
