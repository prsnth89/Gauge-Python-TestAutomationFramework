
from getgauge.python import data_store as data
from business_functions.page_objects.video_page_objects import VideoResultsPageObjects
from framework.interface.iweb import IWeb
import os

class VideoPage:
    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def wait_time(self,seconds):
        self.iWeb.wait_time(seconds)
    
    def verify_video_results_page_got_loaded_successfully(self):
        self.iWeb.wait_for(VideoResultsPageObjects.video_result_overlay,20)

    def take_screenshot_of_page(self):
        screenshot_location=os.getcwd()
        print(screenshot_location)
        self.iWeb.take_screenshot(screenshot_location)
