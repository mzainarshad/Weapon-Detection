from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional

from app.database import get_db, Camera
from app.routes.auth import get_current_user, require_admin

router = APIRouter()

class CameraCreate(BaseModel):
    name: str
    location: Optional[str] = None
    stream_url: str

class CameraOut(BaseModel):
    id: int
    name: str
    location: Optional[str]
    stream_url: str
    is_active: bool
    class Config:
        from_attributes = True

@router.get("/", response_model=List[CameraOut])
def list_cameras(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return db.query(Camera).all()

@router.post("/", response_model=CameraOut)
def add_camera(data: CameraCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    cam = Camera(**data.model_dump())
    db.add(cam); db.commit(); db.refresh(cam)
    return cam

@router.put("/{camera_id}/toggle")
def toggle_camera(camera_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    cam = db.query(Camera).filter(Camera.id == camera_id).first()
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    cam.is_active = not cam.is_active
    db.commit()
    return {"id": cam.id, "is_active": cam.is_active}

@router.delete("/{camera_id}")
def delete_camera(camera_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    cam = db.query(Camera).filter(Camera.id == camera_id).first()
    if not cam:
        raise HTTPException(status_code=404, detail="Camera not found")
    db.delete(cam); db.commit()
    return {"detail": "Camera deleted"}
