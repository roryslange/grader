from ultralytics import YOLO

def train():
    model = YOLO(model="yolov8n.pt")
    model.train(data='./grader/src/dataset.yaml', epochs=50, imgsz=640, batch=16, device='cpu')
    
    