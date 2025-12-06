from ultralytics import YOLO
import os

"""
    tools for training yolo models

    models to use:
    yolov8n-seg.pt (YOLO V8 segmentation fork)
    yolov11n.pt (requires labels to be converted to bounding boxes)
"""

MODEL_PATH_YOLOV8N_SEG = os.curdir.join(["grader/models/yolov8n-seg.pt"])
DATASET_YAML_PATH = "./grader/src/dataset.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
DEVICE = 0 # tbd refactor to use cpu if no gpu available
BEST_WEIGHTS_PATH = os.curdir.join(["runs/segment/train/weights/best.pt"])
LAST_WEIGHTS_PATH = os.curdir.join(["runs/segment/train/weights/last.pt"])

def train():
    model = YOLO(model=MODEL_PATH_YOLOV8N_SEG)
    model.train(data=DATASET_YAML_PATH, epochs=EPOCHS, imgsz=IMG_SIZE, batch=BATCH_SIZE, device=DEVICE)
    
def test():
    model = YOLO(model="./grader/models/yolov8n.pt")
    image = "./grader/person.jpg"
    results = model(image)
    results[0].show()
    
def testOnHolds():
    cwd = os.getcwd()
    model = YOLO(model=BEST_WEIGHTS_PATH)
    images_path = os.path.join(cwd, "grader/datasets/images/valid_images")
    for i in range(3):
        results = model(os.path.join(images_path, os.listdir(images_path)[i]))
        results[0].show()
        