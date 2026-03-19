import cv2
from ultralytics import YOLO

# --- CONFIGURATION ---
# Load YOUR trained model. 
# CHECK THE PATH: If yours is in 'train2', change 'train' to 'train2' below.
model_path = r'runs\detect\train\weights\best.pt' 

# Load the model
print(f"Loading model from: {model_path}...")
model = YOLO(model_path)

# Initialize Webcam (0 is usually the default laptop camera)
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting Camera... Press 'q' to exit.")

while True:
    # 1. Read a frame from the camera
    success, frame = cap.read()
    if not success:
        break

    # 2. Run the AI on the frame
    # conf=0.5 means "Only show me if you are 50% sure it's a gun"
    results = model(frame, conf=0.5)

    # 3. Draw the detections on the frame
    annotated_frame = results[0].plot()

    # 4. Show the result in a window
    cv2.imshow("FYP Weapon Detection System", annotated_frame)

    # 5. Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()