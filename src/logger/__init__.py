import logging
from logging.handlers import RotatingFileHandler
import os 
from from_root import from_root 
from datetime import datetime 



LOG_DIR = "logs"
LOG_FILE = F"{datetime.now().strftime('%m_%d_%t_%H_%M_%S')}.log"
MAX_LLOG_SIZE = 5*1024*1024 
BACKUP_COUNT = 5 


log_dir_path =  os.path.join(form_root() , LOG_DIR) 
os.makedirs(log_dir_path , exist_ok = True) 
log_file_path = os.path.join(log_dir_path , LOG_FILE)


def condigure_logger():
    "configure logger with rotating file handler"
    logger= logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("[%(asctime)s]- %(name)s - %(levelname)s -%(message)s")
