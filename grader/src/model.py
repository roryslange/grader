from ultralytics import YOLO
from .dataloader import downloadClimbingHolds

def test():
    model = YOLO(model="yolo11n.pt")
    datapath = downloadClimbingHolds()
    