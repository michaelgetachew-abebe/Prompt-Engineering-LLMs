import logging
import os



class log:
    
    def __init__(self, file_name: str, level=logging.INFO):
        path = "../logs"
        isExist = os.path.exists(path)

        if not isExist: 
            os.makedirs(path)
