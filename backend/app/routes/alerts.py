from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from datetime import datetime

from app.database import get_db, Alert
from app.routes.auth import get_current_user

router = APIRouter()

class AlertOut(BaseModel):
    id: int
    detection_id: int
    message: str
    severity: str
    is_resolved: bool
    sent_at: datetime
    class Config:
        from_attributes = True

@router.get("/", response_model=List[AlertOut])
def list_alerts(resolved: bool = False, db: Session = Depends(get_db), _=Depends(get_current_user)):
    return db.query(Alert).filter(Alert.is_resolved == resolved).order_by(Alert.sent_at.desc()).all()

@router.put("/{alert_id}/resolve")
def resolve_alert(alert_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    alert.is_resolved = True
    alert.resolved_at = datetime.utcnow()
    db.commit()
    return {"detail": "Alert resolved"}
