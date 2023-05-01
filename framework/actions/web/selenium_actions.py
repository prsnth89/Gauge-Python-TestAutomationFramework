
from framework.locators.locator import Locator
from framework.client_factory.browser_factory import BrowserFactory
from framework.interface.iweb import IWeb
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from time import time
import os

class SeleniumActions(IWeb, BrowserFactory):
    _element: WebElement=None

    def open_browser(self, browser_name):
        BrowserFactory.open_selenium_browser(self,browser_name)

    def quit_browser(self):
        BrowserFactory.quit_selenium_browser()

    def wait_for(self, locator, time_to_wait):
        is_element_present=False
        try:
            self._element=WebDriverWait(self._driver,int(time_to_wait)).until(EC.presence_of_element_located(locator))
            if self._element.is_displayed():
                 is_element_present=True
        except Exception as e:
            assert False, "element not found"
        return is_element_present
    
    def navigate(self, url):
        self._driver.get(url)

    def find(self, locator):
        locator_id=locator[0]
        locator_value=locator[1]
        self._element=self._driver.find_element(locator_id,locator_value)
        if self._element==None:
            assert False, "element not found"
        return self

    def click(self):
        self._element.click()

    def type(self, test_data):
        self._element.clear()
        self._element.send_keys(test_data)
        return self

    def wait_time(self, seconds):
        time.sleep(seconds)
        return self
    
    def verify_title(self, text_to_verify):
        print("title----",self._driver.title)
        assert self._driver.current_url.strip().__contains__(text_to_verify), "failed to verify title"
   
    def take_screenshot(self, path):
        image =self._driver.get_screenshot_as_png()
        file_name=os.path.join(os.getenv("gauge_reports_dir")+path,"screenshot-{0}.png".format(uuid1().int))
        file=open(file_name,"wb")
        file.write(image)
        return os.path.basename(file_name)
