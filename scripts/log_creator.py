import os
import logging
# A Function to create and save logs in the required format

def log(path, file):
    
    # check if the file exists
    log_file = os.path.join(path, file)

    if not os.path.isfile(log_file):
        open(log_file, 'w+').close()

    console_logging_format = "%(levelname)s %(message)s"
    file_logging_format = "%(asctime)s : %(levelname)s: %(name)s: %(module)s: %(funcName)s: %(message)s"

    # Configuring the logger
    logging.basicConfig(level=logging.INFO, format=console_logging_format)
    logger = logging.getLogger()

    
