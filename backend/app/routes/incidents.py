from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from app.database import get_db, Incident, Camera, User, Detection
from app.routes.auth import get_current_user, require_admin

router = APIRouter()


# ── Schemas ──────────────────────────────────────────────────────────────────

class IncidentCreate(BaseModel):
    title:         str
    description:   Optional[str] = None
    severity:      str = "medium"        # low / medium / high / critical
    incident_type: Optional[str] = None
    camera_id:     Optional[int] = None
    detection_id:  Optional[int] = None
    assigned_to:   Optional[int] = None

class IncidentUpdate(BaseModel):
    title:         Optional[str] = None
    description:   Optional[str] = None
    severity:      Optional[str] = None
    status:        Optional[str] = None
    incident_type: Optional[str] = None
    assigned_to:   Optional[int] = None

class AssignedUserOut(BaseModel):
    id:       int
    username: str
    class Config:
        from_attributes = True

class CameraOut(BaseModel):
    id:   int
    name: str
    zone: Optional[str]
    class Config:
        from_attributes = True

class IncidentOut(BaseModel):
    id:            int
    incident_code: str
    title:         str
    description:   Optional[str]
    severity:      str
    status:        str
    incident_type: Optional[str]
    camera_id:     Optional[int]
    detection_id:  Optional[int]
    assigned_to:   Optional[int]
    created_at:    datetime
    updated_at:    datetime
    resolved_at:   Optional[datetime]
    camera:        Optional[CameraOut]
    assigned_user: Optional[AssignedUserOut]
    class Config:
        from_attributes = True


# ── Helpers ──────────────────────────────────────────────────────────────────

def _generate_code(db: Session) -> str:
    year  = datetime.utcnow().year
    count = db.query(Incident).filter(
        Incident.incident_code.like(f"INC-{year}-%")
    ).count()
    return f"INC-{year}-{str(count + 1).zfill(3)}"


# ── Routes ───────────────────────────────────────────────────────────────────

@router.get("/", response_model=List[IncidentOut])
def list_incidents(
    status:   Optional[str] = Query(None),
    severity: Optional[str] = Query(None),
    limit:    int            = Query(50, le=200),
    offset:   int            = Query(0),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    q = db.query(Incident).options(
        joinedload(Incident.camera),
        joinedload(Incident.assigned_user)
    )
    if status:   q = q.filter(Incident.status   == status)
    if severity: q = q.filter(Incident.severity == severity)
    return q.order_by(Incident.created_at.desc()).offset(offset).limit(limit).all()


@router.get("/stats")
def incident_stats(db: Session = Depends(get_db), _=Depends(get_current_user)):
    from sqlalchemy import func
    total      = db.query(Incident).count()
    open_count = db.query(Incident).filter(Incident.status == "open").count()
    in_progress= db.query(Incident).filter(Incident.status == "in_progress").count()
    resolved   = db.query(Incident).filter(Incident.status == "resolved").count()
    by_severity= db.query(Incident.severity, func.count(Incident.id)).group_by(Incident.severity).all()
    by_type    = db.query(Incident.incident_type, func.count(Incident.id)).group_by(Incident.incident_type).all()
    return {
        "total":       total,
        "open":        open_count,
        "in_progress": in_progress,
        "resolved":    resolved,
        "by_severity": {s: c for s, c in by_severity},
        "by_type":     {t: c for t, c in by_type if t},
    }


@router.get("/{incident_id}", response_model=IncidentOut)
def get_incident(incident_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    inc = db.query(Incident).options(
        joinedload(Incident.camera),
        joinedload(Incident.assigned_user)
    ).filter(Incident.id == incident_id).first()
    if not inc:
        raise HTTPException(404, "Incident not found")
    return inc


@router.post("/", response_model=IncidentOut)
def create_incident(
    data: IncidentCreate,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    inc = Incident(
        incident_code = _generate_code(db),
        **data.model_dump()
    )
    db.add(inc); db.commit(); db.refresh(inc)
    return db.query(Incident).options(
        joinedload(Incident.camera),
        joinedload(Incident.assigned_user)
    ).filter(Incident.id == inc.id).first()


@router.put("/{incident_id}", response_model=IncidentOut)
def update_incident(
    incident_id: int,
    data: IncidentUpdate,
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    inc = db.query(Incident).filter(Incident.id == incident_id).first()
    if not inc:
        raise HTTPException(404, "Incident not found")
    for field, value in data.model_dump(exclude_none=True).items():
        setattr(inc, field, value)
    if data.status == "resolved" and not inc.resolved_at:
        inc.resolved_at = datetime.utcnow()
    inc.updated_at = datetime.utcnow()
    db.commit(); db.refresh(inc)
    return db.query(Incident).options(
        joinedload(Incident.camera),
        joinedload(Incident.assigned_user)
    ).filter(Incident.id == inc.id).first()


@router.put("/{incident_id}/resolve")
def resolve_incident(incident_id: int, db: Session = Depends(get_db), _=Depends(get_current_user)):
    inc = db.query(Incident).filter(Incident.id == incident_id).first()
    if not inc:
        raise HTTPException(404, "Incident not found")
    inc.status      = "resolved"
    inc.resolved_at = datetime.utcnow()
    inc.updated_at  = datetime.utcnow()
    db.commit()
    return {"detail": "Incident resolved", "incident_code": inc.incident_code}


@router.delete("/{incident_id}")
def delete_incident(incident_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    inc = db.query(Incident).filter(Incident.id == incident_id).first()
    if not inc:
        raise HTTPException(404, "Incident not found")
    db.delete(inc); db.commit()
    return {"detail": "Incident deleted"}