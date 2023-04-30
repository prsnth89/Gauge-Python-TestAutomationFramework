from abc import abstractmethod


class IWeb:
  
    @abstractmethod
    def open_browser(self, browser_name):
        NotImplementedError
    
    @abstractmethod
    def quit_browser(self):
        NotImplementedError

    @abstractmethod
    def navigate(self, url):
        NotImplementedError
        return self
    
    @abstractmethod
    def wait_for(self, locator, time_to_wait):
        NotImplementedError
        return self
    
    @abstractmethod
    def find(self, locator):
        NotImplementedError
        return self
    
    @abstractmethod
    def click(self):
        NotImplementedError
        return self
    
    @abstractmethod
    def type(self, test_data):
        NotImplementedError
        return self
    
    @abstractmethod
    def take_screenshot(self, test_data):
        NotImplementedError

    @abstractmethod
    def verify_title(self, text_to_verify):
        NotImplementedError