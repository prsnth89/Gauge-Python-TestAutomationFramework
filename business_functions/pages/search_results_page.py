
from getgauge.python import data_store as data
from business_functions.page_objects.search_results_page_objects import SearchResultsPageObjects
from framework.interface.iweb import IWeb


class SearchResultsPage:
    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def wait_time(self,seconds):
        self.iWeb.wait_time(seconds)
    
    def verify_search_results_page(self):
        self.iWeb.wait_for(SearchResultsPageObjects.star_craft_2,20)

    def click_star_carft2(self):
        self.iWeb.find(SearchResultsPageObjects.star_craft_2).click()

    def scroll_down(self):
        self.iWeb.scroll_down()