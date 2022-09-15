import logging
import os



class log:
    
    def __init__(self, file_name: str, level=logging.INFO):
    
        path = "../logs"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)

        if not isExist:
        # Create a new directory because it does not exist 
            os.makedirs(path)

        logger = logging.getLogger(__name__)

        # set log level
        logger.setLevel(level)

        # define file handler and set formatter

        file_handler = logging.FileHandler(f'../logs/{file_name}')
        formatter = logging.Formatter(
            '%(asctime)s : %(levelname)s : %(name)s : %(message)s', '%m-%d-%Y %H:%M:%S')

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        self.logger = logger

    def get_app_logger(self) -> logging.Logger:
        return self.logger