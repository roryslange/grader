import kagglehub as kh

def downloadClimbingHolds():
    path = kh.dataset_download("alirezachahardoli/object-detection-climbing-holds")
    print("Path to dataset files:", path)
    return path

def downloadClimbingHoldsLocally():
    pass