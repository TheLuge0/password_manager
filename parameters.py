import os 
from pathlib import  Path

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, 'data')
SYS_FILE = os.path.join(CUR_DIR, 'system')
path_data = Path(DATA_FILE)
path_system = Path(SYS_FILE)