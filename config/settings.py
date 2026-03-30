import json
import os
import sys

# Determinamos el directorio base (BASE_DIR)
# Si estamos ejecutando el .exe empaquetado por PyInstaller:
if getattr(sys, 'frozen', False):
    # La carpeta donde reside el .exe
    BASE_DIR = os.path.dirname(sys.executable)
    config_path = os.path.join(BASE_DIR, "config", "settings.json")
    
    # Si usamos --onefile y el config está empaquetado DENTRO del exe, el path es sys._MEIPASS
    if not os.path.exists(config_path):
        config_path = os.path.join(getattr(sys, '_MEIPASS', ''), "config", "settings.json")
else:
    # Si ejecutamos desde el código fuente Python:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(BASE_DIR, "config", "settings.json")

with open(config_path, "r", encoding="utf-8") as f:
    _config = json.load(f)

# Si la ruta en el JSON es absoluta (ej. Z:\compartida\incidencias.csv), se usa tal cual.
# Si es relativa (ej. incidencias.csv), se une al BASE_DIR.
_ruta_csv = _config["ARCHIVO_CSV"]
if os.path.isabs(_ruta_csv):
    ARCHIVO_CSV = _ruta_csv
else:
    ARCHIVO_CSV = os.path.join(BASE_DIR, _ruta_csv)

CLIENTES = _config["CLIENTES"]
USUARIOS = _config["USUARIOS"]
ESTADOS = _config["ESTADOS"]