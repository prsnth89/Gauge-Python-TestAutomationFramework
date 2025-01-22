from framework.locators.locator import Locator

class StarCraft2PageObjects:    
    star_craft_2_heading=(Locator.xpath,"//h1[text()='StarCraft II']")
    first_video_link=(Locator.xpath,"//main[@id='page-main-content-wrapper']//div[@role='list']/div[1]//img[@class='tw-image']")
    