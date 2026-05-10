from sqlalchemy import (
    create_engine, Column, Integer, String, Float,
    DateTime, Boolean, ForeignKey, Text, Enum
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
import os

# ── PostgreSQL connection ────────────────────────────────────────────────────
# Set this in your .env file:
#   DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/weapon_detection
DATABASE_URL = "postgresql://postgres:admin123@localhost:5432/weapon_detection"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# ── Models ───────────────────────────────────────────────────────────────────

class User(Base):
    __tablename__ = "users"

    id              = Column(Integer, primary_key=True, index=True)
    username        = Column(String(100), unique=True, index=True, nullable=False)
    email           = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role            = Column(String(50), default="viewer")   # admin / operator / analyst / viewer
    is_active       = Column(Boolean, default=True)
    created_at      = Column(DateTime, default=datetime.utcnow)
    last_login      = Column(DateTime, nullable=True)

    alerts      = relationship("Alert",     back_populates="user")
    incidents   = relationship("Incident",  back_populates="assigned_user")


class Camera(Base):
    __tablename__ = "cameras"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    location   = Column(String(200))
    zone       = Column(String(100))
    stream_url = Column(String(500), nullable=False)
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    detections = relationship("Detection", back_populates="camera")
    recordings = relationship("Recording", back_populates="camera")
    incidents  = relationship("Incident",  back_populates="camera")


class Detection(Base):
    __tablename__ = "detections"

    id            = Column(Integer, primary_key=True, index=True)
    camera_id     = Column(Integer, ForeignKey("cameras.id"))
    label         = Column(String(100), nullable=False)
    confidence    = Column(Float, nullable=False)
    bbox_x        = Column(Float)
    bbox_y        = Column(Float)
    bbox_w        = Column(Float)
    bbox_h        = Column(Float)
    snapshot_path = Column(String(500))
    detected_at   = Column(DateTime, default=datetime.utcnow)

    camera  = relationship("Camera",    back_populates="detections")
    alert   = relationship("Alert",     back_populates="detection", uselist=False)
    incident= relationship("Incident",  back_populates="detection", uselist=False)


class Alert(Base):
    __tablename__ = "alerts"

    id           = Column(Integer, primary_key=True, index=True)
    detection_id = Column(Integer, ForeignKey("detections.id"), nullable=True)
    user_id      = Column(Integer, ForeignKey("users.id"),      nullable=True)
    message      = Column(Text)
    severity     = Column(String(20), default="high")   # low / medium / high / critical
    is_resolved  = Column(Boolean, default=False)
    sent_at      = Column(DateTime, default=datetime.utcnow)
    resolved_at  = Column(DateTime, nullable=True)

    detection = relationship("Detection", back_populates="alert")
    user      = relationship("User",      back_populates="alerts")


class Incident(Base):
    __tablename__ = "incidents"

    id             = Column(Integer, primary_key=True, index=True)
    incident_code  = Column(String(30), unique=True, index=True)  # e.g. INC-2025-001
    detection_id   = Column(Integer, ForeignKey("detections.id"), nullable=True)
    camera_id      = Column(Integer, ForeignKey("cameras.id"),    nullable=True)
    assigned_to    = Column(Integer, ForeignKey("users.id"),      nullable=True)
    title          = Column(String(200), nullable=False)
    description    = Column(Text)
    severity       = Column(String(20), default="medium")  # low / medium / high / critical
    status         = Column(String(20), default="open")    # open / in_progress / resolved
    incident_type  = Column(String(100))                   # Unauthorized Access, etc.
    created_at     = Column(DateTime, default=datetime.utcnow)
    updated_at     = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at    = Column(DateTime, nullable=True)

    camera        = relationship("Camera",    back_populates="incidents")
    detection     = relationship("Detection", back_populates="incident")
    assigned_user = relationship("User",      back_populates="incidents")


class Recording(Base):
    __tablename__ = "recordings"

    id          = Column(Integer, primary_key=True, index=True)
    camera_id   = Column(Integer, ForeignKey("cameras.id"))
    file_path   = Column(String(500), nullable=False)
    file_size   = Column(Float)            # MB
    duration    = Column(Integer)          # seconds
    started_at  = Column(DateTime, default=datetime.utcnow)
    ended_at    = Column(DateTime, nullable=True)
    has_alert   = Column(Boolean, default=False)
    label_tags  = Column(String(500))      # comma-separated labels found in this clip

    camera = relationship("Camera", back_populates="recordings")


# ── DB helpers ───────────────────────────────────────────────────────────────

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
