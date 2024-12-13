from shared.persistence import load_data 
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data/searches.json"

def get_all_searches():
    return load_data(DATA_FILE)