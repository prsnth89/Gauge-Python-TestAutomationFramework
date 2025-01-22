from framework.locators.locator import Locator

class SearchPageObjects:    
    click_browse = (Locator.xpath,"//div[text()='Browse']")
    search=(Locator.xpath,"//input[@type='search']")
    accept_cookies=(Locator.xpath,"//div[text()='Accept']")
    