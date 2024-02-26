import os 
from pathlib import  Path

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, 'data')
SYS_FILE = os.path.join(CUR_DIR, 'system')
path_data = Path(DATA_FILE)
path_system = Path(SYS_FILE)

if not path_data.exists():
    path_data.mkdir()

if not path_system.exists():
    path_system.mkdir()
