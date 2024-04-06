#check documentation corresponding to logger
#any execution that is happening it should be logged
# so that things can be easily tracked

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) #even though there is a file/folder keep on appending the file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO


)


if __name__ == '__main__':
    logging.info("Logging has started")