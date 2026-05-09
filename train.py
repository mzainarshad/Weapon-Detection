from ultralytics import YOLO

def main():
    # 1. Load the model. 
    model = YOLO('yolov8n.pt')

    # 2. Train the model
    print("🚀 Starting training...")
    
    model.train(
        data='data.yaml', 
        epochs=10,       
        imgsz=640,       
        device='cpu',    # Default to CPU for local laptop tests
        workers=0        # Windows compatibility fix
    )

if __name__ == '__main__':
    main()