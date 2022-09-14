import dvc.api
from log_creator import log
import txt

class wr:
    def data_getter(self, path, version):
        data = []
        repo = ""
        url = str(dvc.api.get_url)