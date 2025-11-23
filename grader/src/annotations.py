from ultralytics import YOLO
from ultralytics.data.utils import visualize_image_annotations
from .dataloader import downloadClimbingHolds
import os
import cv2
import numpy as np

def annotate1():
    path = downloadClimbingHolds()
    
    datapath = os.path.join(path, "CV/train")
    imagespath = os.path.join(datapath, "images")
    labelspath = os.path.join(datapath, "labels")
    
    image = os.listdir(imagespath)[0]
    image_file_path = os.path.join(imagespath, image)
    label_file_path = os.path.join(labelspath, image.replace(".jpg", ".txt"))
        
    visualize(image_file_path, label_file_path)
    
def load_yolo_segmentation(label_path):
    polygons = []
    with open(label_path, "r") as f:
        for line in f:
            values = line.strip().split()
            class_id = int(values[0])
            coords = list(map(float, values[1:]))

            xs = coords[0::2]
            ys = coords[1::2]

            polygons.append((class_id, xs, ys))
    return polygons

def visualize(image_path, label_path):
    img = cv2.imread(image_path)
    h, w = img.shape[:2]

    polygons = load_yolo_segmentation(label_path)

    for class_id, xs, ys in polygons:
        # Convert normalized → absolute pixel coordinates
        pts = np.array([[int(x * w), int(y * h)] for x, y in zip(xs, ys)])

        # Draw polygon
        cv2.polylines(img, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

    cv2.imshow("Segmentation Visualization", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
    
    