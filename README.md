# Sign-Language-Detection
# YOLOv8 Sign Language Detection

This project detects and recognizes **sign language gestures** using **YOLOv8**.  
It includes **training**, **evaluation**, and **webcam-based real-time detection**.

⚙️ Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   ->pip install ultralytics
   ->pip install opencv-python
   ->pip install torch torchvision torchaudio

📦 Dataset
The dataset is too large to include in GitHub.
Download it manually and place it in the project folder.
data.yaml -> defines class names and paths to train, validation, and test images/labels.

🚀 Training the Model
Run the training script: "Yolo model.py",
Trained weights will be saved automatically.

🎥 Running Real-Time Detection
Run the webcam detection script: "web cam.py",
Ensure the trained weights (best.pt) are available.
The script will detect gestures in real time using your webcam.

📊 Results
Confusion matrix and sample predictions are generated during training.
Visual results include: "results.png","confusion_matrix.png".
Base model yolov8n.pt is included.

📖 References
YOLOv8 Documentation,
Ultralytics GitHub
