from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.database import get_db, Recording, Camera
from app.routes.auth import get_current_user, require_admin

router = APIRouter()


# ── Schemas ──────────────────────────────────────────────────────────────────

class RecordingCreate(BaseModel):
    camera_id:  int
    file_path:  str
    file_size:  Optional[float] = None   # MB
    duration:   Optional[int]   = None   # seconds
    has_alert:  bool = False
    label_tags: Optional[str]   = None   # e.g. "gun,knife"

class RecordingOut(BaseModel):
    id:         int
    camera_id:  int
    file_path:  str
    file_size:  Optional[float]
    duration:   Optional[int]
    started_at: datetime
    ended_at:   Optional[datetime]
    has_alert:  bool
    label_tags: Optional[str]
    camera:     Optional[dict]
    class Config:
        from_attributes = True

class CameraSnip(BaseModel):
    id:   int
    name: str
    zone: Optional[str]
    class Config:
        from_attributes = True

class RecordingFullOut(BaseModel):
    id:         int
    camera_id:  int
    file_path:  str
    file_size:  Optional[float]
    duration:   Optional[int]
    started_at: datetime
    ended_at:   Optional[datetime]
    has_alert:  bool
    label_tags: Optional[str]
    camera:     Optional[CameraSnip]
    class Config:
        from_attributes = True


# ── Routes ───────────────────────────────────────────────────────────────────

@router.get("/", response_model=List[RecordingFullOut])
def list_recordings(
    camera_id:  Optional[int]  = Query(None),
    has_alert:  Optional[bool] = Query(None),
    limit:      int            = Query(50, le=200),
    offset:     int            = Query(0),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    q = db.query(Recording).options(joinedload(Recording.camera))
    if camera_id is not None: q = q.filter(Recording.camera_id == camera_id)
    if has_alert is not None: q = q.filter(Recording.has_alert == has_alert)
    return q.order_by(Recording.started_at.desc()).offset(offset).limit(limit).all()


@router.get("/stats")
def recording_stats(db: Session = Depends(get_db), _=Depends(get_current_user)):
    from sqlalchemy import func
    total       = db.query(Recording).count()
    with_alerts = db.query(Recording).filter(Recording.has_alert == True).count()
    total_size  = db.query(func.sum(Recording.file_size)).scalar() or 0
    total_dur   = db.query(func.sum(Recording.duration)).scalar()  or 0
    return {
        "total":            total,
        "with_alerts":      with_alerts,
        "total_size_mb":    round(total_size, 2),
        "total_duration_s": total_dur,
    }


@router.get("/{recording_id}", response_model=RecordingFullOut)
def get_recording(recording_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    rec = db.query(Recording).options(joinedload(Recording.camera)).filter(Recording.id == recording_id).first()
    if not rec:
        raise HTTPException(404, "Recording not found")
    return rec


@router.post("/", response_model=RecordingFullOut)
def create_recording(data: RecordingCreate, db: Session = Depends(get_db)):
    """Called automatically by detect_realtime.py when a clip is saved."""
    rec = Recording(**data.model_dump())
    db.add(rec); db.commit(); db.refresh(rec)
    return db.query(Recording).options(joinedload(Recording.camera)).filter(Recording.id == rec.id).first()


@router.put("/{recording_id}/end")
def end_recording(recording_id: int, db: Session = Depends(get_db)):
    """Mark a recording as finished."""
    rec = db.query(Recording).filter(Recording.id == recording_id).first()
    if not rec:
        raise HTTPException(404, "Recording not found")
    rec.ended_at = datetime.utcnow()
    db.commit()
    return {"detail": "Recording ended", "id": rec.id}


@router.delete("/{recording_id}")
def delete_recording(recording_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    rec = db.query(Recording).filter(Recording.id == recording_id).first()
    if not rec:
        raise HTTPException(404, "Recording not found")
    db.delete(rec); db.commit()
    return {"detail": "Recording deleted"}