from getgauge.python import data_store as data
from framework.interface.iweb import IWeb

class HomePage:
    iWeb: IWeb
    def __init__(self) -> None:
        self.iWeb=data.scenario.iweb

    def verify_home_page_loaded(self,text_to_verify):
        self.iWeb.verify_title(text_to_verify)

