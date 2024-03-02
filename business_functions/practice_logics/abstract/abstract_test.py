from abc import ABC, abstractmethod

#define interface
class AMobile(ABC):
    
    @abstractmethod
    def call_option():
        return NotImplementedError
    
    @abstractmethod
    def operating_sys():
        return NotImplementedError
    
    def average_price(self):
        print("average price of an mobile is 30000")

class Samsung(AMobile):
    
    def call_option(self):
        print("Calling from samsung mobile")

    def operating_sys(self):
        print("Samsung runs in android OS")

class Test:
    test=Samsung()
    test.call_option()
    test.operating_sys()
    test.average_price()