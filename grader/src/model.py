from ultralytics import YOLO

def train():
    model = YOLO(model="./grader/models/yolo11s.pt")
    model.train(data='./grader/src/dataset.yaml', epochs=50, imgsz=640, batch=16, device=0)
    
def test():
    model = YOLO(model="./grader/models/yolov8n.pt")
    image = "./grader/person.jpg"
    results = model(image)
    results[0].show()
    