import os
import logging
from datetime import datetime

LOG_DIR = "logs"
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

os.makedirs(LOG_DIR_PATH, exist_ok=True)

LOG_FILE = f'{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log'
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
