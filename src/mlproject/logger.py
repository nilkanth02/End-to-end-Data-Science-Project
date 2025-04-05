# This file is the one-time setup for our logger.py file 

import logging 
import os 
from datetime import datetime

# Set the name for the log file 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Set the path for the file 
log_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# Created a folder 
os.makedirs(log_path, exist_ok=True)

# Writing the complete path of the log file 
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# There is the format of setting up the login, there is this function of 'basiconfig' where we have to maintain the path and the file n'all
logging.basicConfig(
    filename=LOG_FILE_PATH, 
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 

)