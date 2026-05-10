from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Date, extract
from typing import Optional
from datetime import datetime, timedelta

from app.database import get_db, Detection, Alert, Incident, Camera, Recording
from app.routes.auth import get_current_user

router = APIRouter()


@router.get("/dashboard")
def dashboard_stats(db: Session = Depends(get_db), _=Depends(get_current_user)):
    """
    Top-level stat cards shown on the Dashboard page:
    Total Incidents, Active Cameras, Alerts Today, Resolved Cases
    """
    today_start = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    total_incidents  = db.query(Incident).count()
    total_cameras    = db.query(Camera).count()
    active_cameras   = db.query(Camera).filter(Camera.is_active == True).count()
    alerts_today     = db.query(Alert).filter(Alert.sent_at >= today_start).count()
    resolved_cases   = db.query(Incident).filter(Incident.status == "resolved").count()
    total_detections = db.query(Detection).count()

    # week-over-week incident change
    week_ago     = datetime.utcnow() - timedelta(days=7)
    two_weeks    = datetime.utcnow() - timedelta(days=14)
    this_week    = db.query(Incident).filter(Incident.created_at >= week_ago).count()
    last_week    = db.query(Incident).filter(
        Incident.created_at >= two_weeks,
        Incident.created_at <  week_ago
    ).count()
    pct_change   = round(((this_week - last_week) / max(last_week, 1)) * 100, 1)

    return {
        "total_incidents":   total_incidents,
        "total_cameras":     total_cameras,
        "active_cameras":    active_cameras,
        "alerts_today":      alerts_today,
        "resolved_cases":    resolved_cases,
        "total_detections":  total_detections,
        "incident_change_pct": pct_change,
        "camera_utilization": round((active_cameras / max(total_cameras, 1)) * 100, 1),
        "resolution_rate":    round((resolved_cases / max(total_incidents, 1)) * 100, 1),
    }


@router.get("/weekly-incidents")
def weekly_incidents(
    weeks: int = Query(1, ge=1, le=12),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    """
    Incidents and resolutions grouped by day for the last N weeks.
    Used by the 'Incidents This Week' bar chart and Analytics area chart.
    """
    since = datetime.utcnow() - timedelta(weeks=weeks)
    rows  = db.query(
        cast(Incident.created_at, Date).label("day"),
        func.count(Incident.id).label("incidents"),
        func.sum(func.cast(Incident.status == "resolved", Integer_type())).label("resolved"),
    ).filter(Incident.created_at >= since).group_by("day").order_by("day").all()

    return [{"day": str(r.day), "incidents": r.incidents, "resolved": r.resolved or 0} for r in rows]


@router.get("/hourly-activity")
def hourly_activity(db: Session = Depends(get_db), _=Depends(get_current_user)):
    """
    Detection counts grouped by hour-of-day (0-23).
    Used by the 'Hourly Activity Pattern' line chart.
    """
    rows = db.query(
        extract("hour", Detection.detected_at).label("hour"),
        func.count(Detection.id).label("count"),
    ).group_by("hour").order_by("hour").all()

    # Fill missing hours with 0
    hour_map = {int(r.hour): r.count for r in rows}
    return [{"hour": f"{h:02d}:00", "count": hour_map.get(h, 0)} for h in range(24)]


@router.get("/incident-distribution")
def incident_distribution(db: Session = Depends(get_db), _=Depends(get_current_user)):
    """
    Incident counts by type. Used by the 'Incident Distribution' pie chart.
    """
    rows = db.query(
        Incident.incident_type,
        func.count(Incident.id).label("count"),
    ).group_by(Incident.incident_type).all()
    return [{"type": r.incident_type or "Unknown", "count": r.count} for r in rows]


@router.get("/activity-by-zone")
def activity_by_zone(db: Session = Depends(get_db), _=Depends(get_current_user)):
    """
    Detection counts per camera zone. Used by 'Activity by Zone' bar chart.
    """
    rows = db.query(
        Camera.zone,
        func.count(Detection.id).label("count"),
    ).join(Detection, Detection.camera_id == Camera.id, isouter=True
    ).group_by(Camera.zone).all()
    return [{"zone": r.zone or "Unassigned", "count": r.count} for r in rows]


@router.get("/threat-trends")
def threat_trends(
    hours: int = Query(24, ge=1, le=168),
    db: Session = Depends(get_db),
    _=Depends(get_current_user),
):
    """
    Alert severity counts over the last N hours in 3-hour buckets.
    Used by the 'Threat Level Trends' line chart on Dashboard.
    """
    since = datetime.utcnow() - timedelta(hours=hours)
    rows  = db.query(
        (extract("hour", Alert.sent_at) / 3 * 3).label("bucket"),
        Alert.severity,
        func.count(Alert.id).label("count"),
    ).filter(Alert.sent_at >= since
    ).group_by("bucket", Alert.severity).order_by("bucket").all()

    buckets: dict = {}
    for r in rows:
        b = int(r.bucket)
        if b not in buckets:
            buckets[b] = {"hour": f"{b:02d}:00", "low": 0, "medium": 0, "high": 0, "critical": 0}
        buckets[b][r.severity] = r.count

    return list(buckets.values())


@router.get("/detection-stats")
def detection_stats(db: Session = Depends(get_db), _=Depends(get_current_user)):
    """
    Detection counts grouped by label. Used by Detection bar charts.
    """
    from sqlalchemy import func as f
    total    = db.query(Detection).count()
    by_label = db.query(Detection.label, f.count(Detection.id)).group_by(Detection.label).all()
    return {
        "total":    total,
        "by_label": [{"label": l, "count": c} for l, c in by_label],
    }


# ── SQLAlchemy helper: cast bool to int portably ─────────────────────────────
def Integer_type():
    from sqlalchemy import Integer
    return Integer