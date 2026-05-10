from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from app.database import init_db
from app.routes import auth, detections, cameras, alerts, incidents, recordings, analytics, users

app = FastAPI(
    title="Behavioural Anomaly Detection API",
    description="FYP – University of Lahore | AI Surveillance Command Center",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve saved detection snapshots as static files
os.makedirs("detections", exist_ok=True)
app.mount("/snapshots", StaticFiles(directory="detections"), name="snapshots")

# ── Routers ───────────────────────────────────────────────────────────────────
app.include_router(auth.router,        prefix="/api/auth",        tags=["Auth"])
app.include_router(cameras.router,     prefix="/api/cameras",     tags=["Cameras"])
app.include_router(detections.router,  prefix="/api/detections",  tags=["Detections"])
app.include_router(alerts.router,      prefix="/api/alerts",      tags=["Alerts"])
app.include_router(incidents.router,   prefix="/api/incidents",   tags=["Incidents"])
app.include_router(recordings.router,  prefix="/api/recordings",  tags=["Recordings"])
app.include_router(analytics.router,   prefix="/api/analytics",   tags=["Analytics"])
app.include_router(users.router,       prefix="/api/users",       tags=["Users"])


@app.on_event("startup")
async def startup():
    init_db()

@app.get("/")
def root():
    return {
        "status":  "running",
        "project": "Behavioural Anomaly Detection",
        "docs":    "/docs",
    }