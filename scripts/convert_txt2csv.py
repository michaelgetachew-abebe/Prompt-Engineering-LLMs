import pandas as pd
from log_creator import log

def converter(filename:str):
    df = pd.read_csv(filename, encoding = 'ANSI')
    df.to_csv(filename, encoding = 'utf-8', index = False)