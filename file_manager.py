import os

def check_disk_space():
    return {"free_gb": 50, "total_gb": 256}

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
