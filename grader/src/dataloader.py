import kagglehub as kh

HOLDS_DATASET_PATH= "alirezachahardoli/object-detection-climbing-holds"

def downloadClimbingHolds():
    path = kh.dataset_download(HOLDS_DATASET_PATH)
    print("Path to dataset files:", path)
    return path

def downloadClimbingHoldsLocallyAndOrganize():
    pass