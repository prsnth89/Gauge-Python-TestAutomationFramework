
from getgauge.python import data_store as data
from business_functions.page_objects.search_page_objects import SearchPageObjects
from framework.interface.iweb import IWeb


class SearchPage:

    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def wait_time(self,seconds):
        self.iWeb.wait_time(seconds)

    def click_accept_cookies(self):
        self.iWeb.wait_for(SearchPageObjects.accept_cookies,20)
        self.iWeb.find(SearchPageObjects.accept_cookies).click()

    def click_browse(self):
        self.iWeb.find(SearchPageObjects.click_browse).click()
        self.iWeb.wait_for(SearchPageObjects.search,10)

    def type_search_text_and_enter(self,text_to_search):
        self.iWeb.find(SearchPageObjects.search).type(text_to_search)
        self.iWeb.find(SearchPageObjects.search).enter_by_keyboard()