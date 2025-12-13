from ultralytics import YOLO
import os

"""
    tools for training yolo models

    models to use:
    yolov8n-seg.pt (YOLO V8 segmentation fork)
    yolov11n.pt (requires labels to be converted to bounding boxes)
"""

MODEL_PATH_DETECT_YOLO11N = os.curdir.join(["grader/models/yolo11n.pt"])
MODEL_PATH_DETECT_YOLO11S = os.curdir.join(["grader/models/yolo11s.pt"])
MODEL_PATH_POSE_YOLO11N = os.curdir.join(["grader/models/yolo11l-pose.pt"])

DATASET_YAML_PATH = "./grader/src/dataset.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
DEVICE = 0 # tbd refactor to use cpu if no gpu available
BEST_WEIGHTS_PATH = os.curdir.join(["runs/detect/train6/weights/best.pt"])
LAST_WEIGHTS_PATH = os.curdir.join(["runs/detect/train6/weights/last.pt"])

def train():
    model = YOLO(model=MODEL_PATH_DETECT_YOLO11S)
    model.train(data=DATASET_YAML_PATH, epochs=EPOCHS, imgsz=IMG_SIZE, batch=BATCH_SIZE, device=DEVICE)
    
def testOnHolds():
    cwd = os.getcwd()
    model = YOLO(model=BEST_WEIGHTS_PATH)
    images_path = os.path.join(cwd, "grader/datasets/images/valid_images")
    for i in range(3):
        results = model(os.path.join(images_path, os.listdir(images_path)[i]))
        results[0].show()
        
def testOnPerson():
    cwd = os.getcwd()
    model = YOLO(model=MODEL_PATH_POSE_YOLO11N)
    results = model(os.path.join(cwd, "meOnWall.jpeg"))
    results[0].show()