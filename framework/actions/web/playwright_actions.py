from framework.client_factory.browser_factory import BrowserFactory
from framework.interface.iweb import IWeb
from playwright.async_api import BrowserContext,Page, Route
from multipledispatch import dispatch
from time import time
from uuid import uuid1
import os
from framework.locators.locator import Locator

class PlayWrightActions(IWeb,BrowserFactory):

    _element:Page

    def refactor(self, locator):
        match locator[0]:
            case Locator.id:
                return "[id="+locator[1]+"]"
            case Locator.name:
                return "[name="+locator[1]+"]"
            case Locator.clss_name:
                return "[class="+locator[1]+"]"
            case _:
                return locator
    
    def open_browser(self, browser_name):
        self.open_playwright_browser(browser_name)

    def quite_browser(self):
        self.quit_playwright_browser()

    def wait_for(self, locator, time_to_wait):
        is_element_present=False
        try:
            if self._page.wait_for_selector(self.refactor(locator),timeout=int(time_to_wait)):
                is_element_present=True
        except Exception as e:
            assert False, "element not found"
        return is_element_present
    
    def navigate(self, url):
        self._page.goto(url)

    def click(self):
        self._element.click()
        return self

    def type(self,test_data):
        self._element.fill(test_data)
        return self
    
    @dispatch(tuple)
    def find(self, locator):
        self._element=self._page.locator(self.refactor(locator))
        return self
    
    @dispatch(tuple,str)
    def find(self, locator,timeout):
        if not self.wait_for(locator,int(timeout)):
            assert False, "Element not found"
        self._element=self._page.locator(self.refactor(locator))
        return self

    def wait_time(self, second):
        time.sleep(second)

    def verify_title(self, text_to_verify):
        print("title-------",self._page.url)
        assert self._page.url.__contains__(text_to_verify)

    def take_screenshot(self, path):
        image =self._page.screenshot()
        file_name=os.path.join(os.getenv("gauge_reports_dir")+path,"screenshot-{0}.png".format(uuid1().int))
        file=open(file_name,"wb")
        file.write(image)
        return os.path.basename(file_name)