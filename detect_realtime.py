import cv2
import os
import time
import pandas as pd
from datetime import datetime
from ultralytics import YOLO

# ---------------- CONFIG ---------------- #

# Model setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "weights", "best.pt")

if not os.path.exists(model_path):
    print(f"❌ Error: Model file not found at {model_path}")
    print("👉 Please ensure 'best.pt' is in the 'weights' folder.")
    exit()

print(f"✅ Loading model from: {model_path}...")
model = YOLO(model_path)

# Alert settings
ALERT_COOLDOWN = 5  # seconds
last_alert_time = 0

# Create folders for detections
output_dir = os.path.join(BASE_DIR, "detections")
os.makedirs(output_dir, exist_ok=True)

# CSV Log setup
log_path = os.path.join(output_dir, "detection_log.csv")
if not os.path.exists(log_path):
    df = pd.DataFrame(columns=['timestamp', 'datetime', 'class', 'confidence', 'image_path'])
    df.to_csv(log_path, index=False)

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting Camera... Press 'q' to exit.")

# FPS variables
prev_time = 0

# ---------------- MAIN LOOP ---------------- #

while True:
    success, frame = cap.read()
    if not success:
        break

    # ---- FPS CALCULATION ---- #
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    # ---- MODEL INFERENCE ---- #
    results = model(frame, conf=0.5, verbose=False)

    detected = False

    for r in results:
        for box in r.boxes:
            detected = True

            # Get class + confidence
            class_id = int(box.cls[0])
            label = model.names[class_id]
            confidence = float(box.conf[0])

            # ---- ALERT & LOGGING SYSTEM ---- #
            if current_time - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = current_time
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

                print(f"[ALERT] {label} detected ({confidence:.2f}) at {dt_string}")

                # Save image
                img_name = f"{label}_{int(current_time)}.jpg"
                img_path = os.path.join(output_dir, img_name)
                cv2.imwrite(img_path, frame)

                # Append to CSV
                new_entry = {
                    'timestamp': current_time,
                    'datetime': dt_string,
                    'class': label,
                    'confidence': round(confidence, 4),
                    'image_path': img_name
                }
                
                # Using pandas to append to CSV
                log_df = pd.read_csv(log_path)
                log_df = pd.concat([log_df, pd.DataFrame([new_entry])], ignore_index=True)
                log_df.to_csv(log_path, index=False)
                
                print(f"Logged to: {log_path}")

    # ---- DRAW DETECTIONS ---- #
    annotated_frame = results[0].plot()

    # ---- SHOW FPS ---- #
    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ---- DISPLAY ---- #
    cv2.imshow("FYP Weapon Detection System", annotated_frame)

    # Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
