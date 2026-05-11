import json
from pathlib import Path

def load_data(json_path):
    if json_path.exists():
        with open(json_path, "r") as f:
            data = json.load(f)
        return data
    else:
        return []