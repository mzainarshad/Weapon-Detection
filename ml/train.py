# Run this on Google Colab, not locally
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data   = "ml/data.yaml",
    epochs = 50,
    imgsz  = 640,
    batch  = 16,
    name   = "weapon_detection",
    project= "runs/train",
)

# After training, copy best.pt to ml/weights/best.pt
