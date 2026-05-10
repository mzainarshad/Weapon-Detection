from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

from app.database import get_db, User
from app.routes.auth import get_current_user, require_admin, hash_password

router = APIRouter()


# ── Schemas ──────────────────────────────────────────────────────────────────

class UserCreate(BaseModel):
    username: str
    email:    EmailStr
    password: str
    role:     str = "viewer"   # admin / operator / analyst / viewer

class UserUpdate(BaseModel):
    email:     Optional[EmailStr] = None
    role:      Optional[str]      = None
    is_active: Optional[bool]     = None
    password:  Optional[str]      = None

class UserOut(BaseModel):
    id:         int
    username:   str
    email:      str
    role:       str
    is_active:  bool
    created_at: datetime
    last_login: Optional[datetime]
    class Config:
        from_attributes = True

class UserStats(BaseModel):
    total:          int
    active:         int
    inactive:       int
    by_role:        dict


# ── Routes ───────────────────────────────────────────────────────────────────

@router.get("/stats", response_model=UserStats)
def user_stats(db: Session = Depends(get_db), _=Depends(require_admin)):
    from sqlalchemy import func
    total    = db.query(User).count()
    active   = db.query(User).filter(User.is_active == True).count()
    by_role  = db.query(User.role, func.count(User.id)).group_by(User.role).all()
    return {
        "total":   total,
        "active":  active,
        "inactive":total - active,
        "by_role": {r: c for r, c in by_role},
    }


@router.get("/", response_model=List[UserOut])
def list_users(
    role:      Optional[str]  = Query(None),
    is_active: Optional[bool] = Query(None),
    limit:     int            = Query(50, le=200),
    offset:    int            = Query(0),
    db: Session = Depends(get_db),
    _=Depends(require_admin),
):
    q = db.query(User)
    if role      is not None: q = q.filter(User.role      == role)
    if is_active is not None: q = q.filter(User.is_active == is_active)
    return q.order_by(User.created_at.desc()).offset(offset).limit(limit).all()


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db), _=Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user


@router.post("/", response_model=UserOut)
def create_user(data: UserCreate, db: Session = Depends(get_db), _=Depends(require_admin)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email already registered")
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(400, "Username already taken")
    user = User(
        username        = data.username,
        email           = data.email,
        hashed_password = hash_password(data.password),
        role            = data.role,
    )
    db.add(user); db.commit(); db.refresh(user)
    return user


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db), _=Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    if data.email     is not None: user.email     = data.email
    if data.role      is not None: user.role      = data.role
    if data.is_active is not None: user.is_active = data.is_active
    if data.password  is not None: user.hashed_password = hash_password(data.password)
    db.commit(); db.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current=Depends(require_admin)):
    if user_id == current.id:
        raise HTTPException(400, "Cannot delete your own account")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    db.delete(user); db.commit()
    return {"detail": "User deleted"}


@router.patch("/{user_id}/toggle")
def toggle_user(user_id: int, db: Session = Depends(get_db), current=Depends(require_admin)):
    if user_id == current.id:
        raise HTTPException(400, "Cannot deactivate your own account")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    user.is_active = not user.is_active
    db.commit()
    return {"id": user.id, "is_active": user.is_active}