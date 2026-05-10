from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.database import get_db, Detection, Alert
from app.routes.auth import get_current_user

router = APIRouter()

class DetectionCreate(BaseModel):
    camera_id: int
    label: str
    confidence: float
    bbox_x: Optional[float] = None
    bbox_y: Optional[float] = None
    bbox_w: Optional[float] = None
    bbox_h: Optional[float] = None
    snapshot_path: Optional[str] = None

class DetectionOut(BaseModel):
    id: int
    camera_id: int
    label: str
    confidence: float
    snapshot_path: Optional[str]
    detected_at: datetime
    class Config:
        from_attributes = True

@router.get("/", response_model=List[DetectionOut])
def list_detections(
    camera_id: Optional[int] = Query(None),
    label:     Optional[str] = Query(None),
    limit:     int           = Query(50, le=500),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    q = db.query(Detection)
    if camera_id: q = q.filter(Detection.camera_id == camera_id)
    if label:     q = q.filter(Detection.label == label)
    return q.order_by(Detection.detected_at.desc()).limit(limit).all()

@router.post("/", response_model=DetectionOut)
def log_detection(data: DetectionCreate, db: Session = Depends(get_db)):
    detection = Detection(**data.model_dump())
    db.add(detection); db.flush()
    if data.confidence >= 0.60:
        alert = Alert(
            detection_id=detection.id,
            message=f"{data.label} detected with {data.confidence:.0%} confidence on camera {data.camera_id}",
            severity="high" if data.confidence >= 0.80 else "medium",
        )
        db.add(alert)
    db.commit(); db.refresh(detection)
    return detection

@router.get("/stats")
def detection_stats(db: Session = Depends(get_db), _=Depends(get_current_user)):
    from sqlalchemy import func
    total    = db.query(Detection).count()
    by_label = db.query(Detection.label, func.count(Detection.id)).group_by(Detection.label).all()
    return {"total": total, "by_label": [{"label": l, "count": c} for l, c in by_label]}
