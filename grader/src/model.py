from ultralytics import YOLO
from huggingface_hub import login, upload_folder
import os
import cv2

"""
    tools for training yolo models

    models to use:
    yolov8n-seg.pt (YOLO V8 segmentation fork)
    yolov11n.pt (requires labels to be converted to bounding boxes)
"""

MODEL_PATH_DETECT_YOLO11N = os.curdir.join(["grader/models/yolo11n.pt"])
MODEL_PATH_DETECT_YOLO11S = os.curdir.join(["grader/models/yolo11s.pt"])
MODEL_PATH_POSE_YOLO11N = os.curdir.join(["grader/models/yolo11s-pose.pt"])

DATASET_YAML_PATH = "./grader/src/dataset.yaml"
EPOCHS = 50
IMG_SIZE = 640
BATCH_SIZE = 16
DEVICE = 0 # tbd refactor to use cpu if no gpu available
BEST_WEIGHTS_PATH = os.curdir.join(["runs/detect/train6/weights/best.pt"])
LAST_WEIGHTS_PATH = os.curdir.join(["runs/detect/train6/weights/last.pt"])
MODEL_UPLOAD_PATH = os.curdir.join(["runs/detect/train6"])
TEST_IMAGE_PATH = os.curdir.join(["meOnWall.jpeg"])
MODEL_TEST_HOLDS = os.curdir.join(["grader/models/test-holds.pt"])

def train():
    model = YOLO(model=MODEL_PATH_DETECT_YOLO11S)
    model.train(data=DATASET_YAML_PATH, epochs=EPOCHS, imgsz=IMG_SIZE, batch=BATCH_SIZE, device=DEVICE)
    
def testOnHolds():
    cwd = os.getcwd()
    model = YOLO(model=MODEL_TEST_HOLDS)
    images_path = os.path.join(cwd, "grader/datasets/images/valid_images")
    for i in range(3):
        results = model(os.path.join(images_path, os.listdir(images_path)[i]))
        results[0].show()
        
def testOnPerson():
    imagepath = os.curdir.join(["meOnWall.jpeg"])
    image = cv2.imread(imagepath)
    pose_model = YOLO(model=MODEL_PATH_POSE_YOLO11N)
    detect_model = YOLO(model=MODEL_TEST_HOLDS)
    pose_result = pose_model(image, verbose=False)
    detect_result = detect_model(image, verbose=False)
    
    combined = image.copy()
    combined = pose_result[0].plot(img=combined)
    combined = detect_result[0].plot(img=combined)
        
    cv2.imshow("output", combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def uploadModels():
    pose_model = YOLO(model=MODEL_PATH_POSE_YOLO11N)
    detect_model = YOLO(model="grader/models/yolo11n.pt")
    pose_export_path = pose_model.export(format='onnx')
    detect_export_path = detect_model.export(format='onnx')
    login()
    upload_folder(folder_path=os.curdir.join(["grader/models"]), repo_id="roryslange/grader", repo_type="model")