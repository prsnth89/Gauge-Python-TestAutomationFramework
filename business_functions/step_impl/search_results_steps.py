from getgauge.python import step
from business_functions.hooks.hooks import Hooks
from getgauge.python import data_store as data
from business_functions.pages.search_page import *
from business_functions.pages.search_results_page import *
from business_functions.pages.star_craft2_page import *
from business_functions.pages.video_page import *
from framework.interface.iweb import IWeb

@step("Click browse button")
def click_browse_button():
    global searchPage
    searchPage=SearchPage()
    searchPage.click_accept_cookies()
    searchPage.click_browse()

@step("Search <search_text> and enter")
def search_and_enter(search_text):
    searchPage.type_search_text_and_enter(search_text)


@step("Verify search results page got loaded successfully")
def verify_search_results_page_got_loaded_successfully():
    global search_results_page
    search_results_page=SearchResultsPage()
    search_results_page.verify_search_results_page()

@step("Scroll down <no_of_times> times")
def scroll_down_times(no_of_times):
    print(no_of_times)
    for i in range(int(no_of_times)):
        search_results_page.scroll_down()

@step("Click starcraft2")
def click_starcraft2():
    search_results_page.click_star_carft2()


@step("Take screenshot of the page")
def take_screenshot_of_the_page():
    video_page=VideoPage()
    video_page.take_screenshot_of_page()

@step("Click first streamer")
def click_first_streamer():
    global startCraft2Page
    startCraft2Page=StartCraft2Page()
    startCraft2Page.wait_for_star_carft2_results_page()
    startCraft2Page.click_first_video()

@step("Verify if the first steamer result page got loaded successfully")
def verify_if_the_first_steamer_result_page_got_loaded_successfully():
    global video_page
    video_page=VideoPage()
    video_page.verify_video_results_page_got_loaded_successfully()
