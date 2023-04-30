from framework.locators.locator import Locator

class LoginPageObjects:    
    txtUsername = (Locator.id,"user-name")
    txtPassword = (Locator.id,"password")
    btnLogin = (Locator.id,"login-button")
    title = (Locator.xpath,"//span[@class='title']")