import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import re
import sys
import warnings
warnings.filterwarnings('ignore')
from log_creator import log



from sklearn.datasets import fetch_20newsgroups
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from cleaner import DataCleaner

warnings.filterwarnings('ignore')

sys.path.append('../')


class Processor:
    def __init__(self) -> None:
        """Initilize class."""
        try:
            self.logger = log("preprocessor.log").get_app_logger()
            self.logger.info('Successfully initialized processor Object')
            self.cleaner=DataCleaner()
        except Exception:
            self.logger.exception('Failed to processor util Object')
            sys.exit(1)
    
    def prepare_text(self,df:pd.DataFrame,columns:list=[]):
        self.logger.info("Preparing texts")
        if len(columns) == 0:
            columns = self.cleaner.get_categorical_columns(df)
        targeted_df=df[columns]
        pipeline= Pipeline(steps=[
            ('symbol_cleanner',FunctionTransformer(self.cleaner.clean_symbols, kw_args={"columns":columns},validate=False)),
            ('lower_casing',FunctionTransformer(self.cleaner.convert_to_lower_case, kw_args={"columns":columns},validate=False)),
            ('link_cleanner',FunctionTransformer(self.cleaner.clean_links, kw_args={"columns":columns},validate=False)),
            ('stemmer',FunctionTransformer(self.cleaner.stem_word, kw_args={"columns":columns},validate=False)),
            ('lemmatization',FunctionTransformer(self.cleaner.lemantize, kw_args={"columns":columns},validate=False)),
            ('trail_space_remover',FunctionTransformer(self.cleaner.trail_space_remove, kw_args={"columns":columns},validate=False)),
            ('remove_stop_word',FunctionTransformer(self.cleaner.clean_stopwords, kw_args={"columns":columns},validate=False)),
        ])

        transformed=pipeline.fit_transform(targeted_df)
        
        df[columns]=transformed
        return df
    
    def prepare_tuner(self,train_df:pd.DataFrame):

        prompt=""
        for ind in train_df.index:
            prompt += "Task: Generate Analyst Average Score\n\n"
            for col in train_df.columns:
                if train_df.loc[ind,col] != '':
                    prompt += f"{col}: {train_df.loc[ind,col]}\n\n"
            prompt += "-- --\n\n"
        try:
            with open('../data/tuner.txt', 'w', encoding="utf-8") as f:
                f.write(prompt)
            print("tuner prepared successfuly")
        except:
            print("Failed to prepare tuner")