import warnings
from log_creator import log
import cohere
import pandas as pd
from IPython.display import display

import sys
warnings.filterwarnings('ignore')

sys.path.append('../')
import config
key = config.cohere_key['key']
class Predict:
    def __init__(self):
        """Initilize class."""
        try:
            self.logger = log("predict.log").get_app_logger()
            self.api_key=key
            self.logger.info('initialized predict Object')
        except Exception:
            self.logger.exception('Failed to processor predict Object')
            sys.exit(1)
        
    def predict(self,train_df:pd.DataFrame,test:pd.DataFrame, model="xlarge"):

        test_df=test.drop(test.columns[len(test.columns)-1],axis=1)

        prompt=""
        
        for ind in train_df.index:
            prompt += "Task: Generate Analyst Average Score\n\n"
            for col in train_df.columns:
                prompt += f"{col}: {train_df.loc[ind,col]}\n\n"
            prompt += "-- --\n\n"
        
        prompt += "Task: Generate Analyst Average Score\n\n"
        for col in test_df.columns:
            ind=test_df.index[0]
            prompt += f"{col}: {test_df.loc[ind,col]}\n\n"

        prompt += f"{test.columns[len(test.columns)-1]}: "
        # prompt = "Task: Score News relevance\n\n"+prompt
        
        co = cohere.Client(f'{self.api_key}')
        response = co.generate(
        model=model,
        prompt=prompt.strip(),
        max_tokens=1,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["-- --"],
        return_likelihoods='NONE')
        print('Prediction: {}'.format(response.generations[0].text))
        return prompt