from ultralytics import YOLO
import os

"""
    tools for training yolo models

    models to use:
    yolov8n-seg.pt (YOLO V8 segmentation fork)
    yolov11n.pt (requires labels to be converted to bounding boxes)
"""

def train():
    model = YOLO(model="./grader/models/yolo11s.pt")
    model.train(data='./grader/src/dataset.yaml', epochs=50, imgsz=640, batch=16, device=0)
    
def test():
    model = YOLO(model="./grader/models/yolov8n.pt")
    image = "./grader/person.jpg"
    results = model(image)
    results[0].show()
    
def testOnHolds():
    cwd = os.getcwd()
    model = YOLO(model="yolov8n-seg.pt")
    images_path = os.path.join(cwd, "grader/datasets/images/valid_images")
    for i in range(3):
        results = model(os.path.join(images_path, os.listdir(images_path)[i]))
        results[0].show()
        