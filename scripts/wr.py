import dvc.api
from log_creator import log
import txt

class wr:
    def dvc_get_data(self, path, version='v1'):
        data = []
        try:
            repo = "C:\Users\mikyg\OneDrive\Desktop\10 Acadamy\Week 4\Prompt-Engineering-LLMs"
            data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
            data_url = str(data_url)[6:]
            with open(data_url, 'r') as f:
                data = txt.loads(f.read())
            log.info(f"{path} with version {version} Loaded")
        except Exception as e:
            log.error(e)
        return data 