from abc import ABC, abstractmethod

#define interface
class IMobile(ABC):
    
    @abstractmethod
    def call_option():
        return NotImplementedError
    
    @abstractmethod
    def operating_sys():
        return NotImplementedError
    
class Samsung(IMobile):

    def call_option(self):
        print("Calling from samsung mobile")

    def operating_sys(self):
        print("Samsung runs in android OS")

class Test:
    test=Samsung()
    test.call_option()
    test.operating_sys()