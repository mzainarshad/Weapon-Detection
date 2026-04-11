import cv2
import os
import time
from ultralytics import YOLO

# ---------------- CONFIG ---------------- #

# Fix model path (portable)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "runs", "detect", "train", "weights", "best.pt")

print(f"Loading model from: {model_path}...")
model = YOLO(model_path)

# Alert settings
ALERT_COOLDOWN = 5  # seconds
last_alert_time = 0

# Create folder to save detections
output_dir = os.path.join(BASE_DIR, "detections")
os.makedirs(output_dir, exist_ok=True)

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
    results = model(frame, conf=0.5)

    detected = False

    for r in results:
        for box in r.boxes:
            detected = True

            # Get class + confidence
            class_id = int(box.cls[0])
            label = model.names[class_id]
            confidence = float(box.conf[0])

            # ---- ALERT SYSTEM ---- #
            current_time = time.time()
            if current_time - last_alert_time > ALERT_COOLDOWN:
                last_alert_time = current_time

                print(f"[ALERT] {label} detected ({confidence:.2f})")

                # Save image
                filename = f"{label}_{int(current_time)}.jpg"
                filepath = os.path.join(output_dir, filename)
                cv2.imwrite(filepath, frame)

                print(f"Saved: {filepath}")

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