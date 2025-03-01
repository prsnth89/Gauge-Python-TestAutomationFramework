from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from playwright.async_api import Page,async_playwright
from playwright.sync_api import Page,sync_playwright
from framework.interface.iweb import IWeb
import gc


class BrowserFactory:
    _driver: webdriver=None
    _page : Page=None
    _context=None
    _browser=None
    _playwright=None
    tabs=dict({})


    def open_selenium_browser(self,browser_type='chrome'):
        if browser_type=='chrome':
            _driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        elif browser_type=='edge':
            _driver=webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self._driver=_driver
        self._driver.maximize_window
        self._driver.delete_all_cookies
        self.tabs.update({'default':self._driver.current_window_handle})

    def open_mob_selenium_browser(self,browser_type='chrome'):
        _driver=None
        if browser_type=='chrome':
            mobile_emulation = self._get_mobile_emulation("iphonex")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            _driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        elif browser_type=='edge':
            mobile_emulation = self._get_mobile_emulation("nexus")
            options = webdriver.EdgeOptions()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            _driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
        self._driver=_driver
        self._driver.maximize_window
        self._driver.delete_all_cookies
        self.tabs.update({'default':self._driver.current_window_handle})

    def _get_mobile_emulation(self, device_name):
        devices = {
            'iphonex': {"deviceName": "iPhone X"},
            'nexus': {"deviceName": "Nexus 5"}
        }
        return devices.get(device_name)
    
    def quit_mob_selenium_browser(self):
        self._driver.quit()
        gc.collect()

    def quit_selenium_browser(self):
        self._driver.quit()
        gc.collect()

    def start_playwright_engine(self):
        self._playwright=sync_playwright().start()
        return self._playwright
    
    def open_playwright_browser(self, browser_name='chrome'):
        self._playwright=self.start_playwright_engine()
        if browser_name=='chrome':
            browser=self._playwright.chromium.launch(headless=False, slow_mo=50)
        # if self.video=='yes':
        #     context=browser.new_context()
        #     page=browser.new_page(record_video_dir="./reports/video")
        # else:
            context=browser.new_context()
            page=browser.new_page()

        def check(response):
            if(response.status==400):
                assert False, "network error----url----"+response.url

        page.on('response',check)
        self._page=page
        self._context=context
        self._browser=browser
        self.tabs.update({'default':page})
        #self._page_set_viewport_size({'width':get_monitors()[0].width, 'height':get_monitors()[0].height})

    def quit_playwright_browser(self):
        self._context.close()
        self._browser.close()
        self.stop_playwright_engine()
        gc.collect()

    def stop_playwright_engine(self):
        self._playwright.stop()
    
