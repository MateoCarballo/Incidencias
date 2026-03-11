import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "config", "settings.json"), "r") as f:
    _config = json.load(f)

ARCHIVO_CSV = os.path.join(BASE_DIR, _config["ARCHIVO_CSV"])