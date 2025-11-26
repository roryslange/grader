from ultralytics import YOLO
from PIL import ImageGrab

def train():
    model = YOLO(model="yolov5s.pt")
    model.train(data='./grader/src/dataset.yaml', epochs=50, imgsz=640, batch=16, device='cpu')
    
def test():
    model = YOLO(model="yolov8n.pt")
    image = "./grader/person.jpg"
    results = model(image)
    results[0].show()
    