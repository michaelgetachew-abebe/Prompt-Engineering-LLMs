import os
import logging
# A Function to create and save logs in the required format

def log(path, file):
    
    # check if the file exists
    log_file = os.path.join(path, file)

    if not os.path.isfile(log_file):
        open(log_file, 'w+').close()

    