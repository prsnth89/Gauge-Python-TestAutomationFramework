
from getgauge.python import data_store as data
from business_functions.page_objects.star_craft_2_page_objects import StarCraft2PageObjects
from framework.interface.iweb import IWeb
import os


class StartCraft2Page:
    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def wait_time(self,seconds):
        self.iWeb.wait_time(seconds)

    def wait_for_star_carft2_results_page(self):
        self.iWeb.wait_for(StarCraft2PageObjects.star_craft_2_heading,20)

    def click_first_video(self):
        self.iWeb.find(StarCraft2PageObjects.first_video_link).click()

    