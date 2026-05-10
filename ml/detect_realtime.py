"""
detect_realtime.py  —  Run from project root:
    python detect_realtime.py --camera 0
    python detect_realtime.py --camera rtsp://192.168.1.100/stream --camera-id 2
"""
import argparse, cv2, os, time, requests
from pathlib import Path
from ultralytics import YOLO
from datetime import datetime

BACKEND_URL          = os.getenv("BACKEND_URL", "http://localhost:8000")
WEIGHTS_PATH         = Path(__file__).parent / "ml" / "weights" / "best.pt"
SNAPSHOT_DIR         = Path(__file__).parent / "detections" / "snapshots"
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
CONFIDENCE_THRESHOLD = 0.50
POST_COOLDOWN_SEC    = 2.0

def run(stream_source, camera_id=1):
    model = YOLO(str(WEIGHTS_PATH))
    cap   = cv2.VideoCapture(int(stream_source) if str(stream_source).isdigit() else stream_source)
    if not cap.isOpened():
        print(f"[ERROR] Cannot open stream: {stream_source}"); return

    last_posted = {}
    print("[INFO] Detection started — press Q to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.5); continue

        results = model(frame, verbose=False)[0]

        for box in results.boxes:
            conf  = float(box.conf[0])
            label = model.names[int(box.cls[0])]
            if conf < CONFIDENCE_THRESHOLD: continue
            now = time.time()
            if now - last_posted.get(label, 0) < POST_COOLDOWN_SEC: continue

            ts            = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            snapshot_path = str(SNAPSHOT_DIR / f"{label}_{ts}.jpg")
            cv2.imwrite(snapshot_path, frame)
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            payload = {
                "camera_id": camera_id, "label": label,
                "confidence": round(conf, 4),
                "bbox_x": round(x1,1), "bbox_y": round(y1,1),
                "bbox_w": round(x2-x1,1), "bbox_h": round(y2-y1,1),
                "snapshot_path": snapshot_path,
            }
            try:
                r = requests.post(f"{BACKEND_URL}/api/detections/", json=payload, timeout=3)
                print(f"[DETECT] {label} ({conf:.0%}) -> id={r.json().get('id')}")
            except Exception as e:
                print(f"[ERROR] {e}")
            last_posted[label] = now

        cv2.imshow("Weapon Detection — Q to quit", results.plot())
        if cv2.waitKey(1) & 0xFF == ord("q"): break

    cap.release(); cv2.destroyAllWindows()

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--camera",    default="0")
    p.add_argument("--camera-id", type=int, default=1)
    args = p.parse_args()
    run(args.camera, args.camera_id)
