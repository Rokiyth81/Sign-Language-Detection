from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")
    model.train(
        data=r"C:\Users\Hp\OneDrive\Desktop\dataset\data.yaml",
        epochs=50,
        imgsz=640,
        device=0
    )

if __name__ == "__main__":
    main()

