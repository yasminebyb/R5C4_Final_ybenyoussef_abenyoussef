import json
from pathlib import Path

def load_data(path):
    with open(path, 'r') as file:
        return json.load(file)

