from ultralytics import YOLO

def main():
    # 1. Load the model. 
    # We use 'yolov8n.pt' (nano) because it is the fastest to train on laptops.
    model = YOLO('yolov8n.pt')

    # 2. Train the model
    print("Starting CPU training (Optimized for Windows)...")
    
    model.train(
        data='data.yaml', 
        epochs=10,       # Reduced to 10 for faster testing on CPU
        imgsz=640,       # Standard image size
        device='cpu',    # Force CPU usage
        workers=0        # CRITICAL FIX: Prevents crashing on Windows
    )

if __name__ == '__main__':
    main()