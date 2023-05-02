from getgauge.python import step
from business_functions.hooks.hooks import Hooks
from getgauge.python import data_store as data
from business_functions.pages.home_page import HomePage
from business_functions.pages.login_page import LoginPage
from framework.interface.iweb import IWeb

login_page:LoginPage=None

@step("Login to sauce demo page")
def login_to_sauce_demo_page():
    pass

@step("Enter <user_name> and <password>")
def enter_user_pwd(user_name, password):
    global login_page
    login_page=LoginPage()
    login_page.login(user_name,password)

@step("Click Login to sauce demo page")
def click_login_to_sauce_demo_page():
    pass

@step("Verify if the page got loaded successfully")
def verify_if_the_page_got_loaded_successfully():
    home_page=HomePage()
    home_page.wait_time(3)
    home_page.verify_home_page_loaded("https://www.saucedemo.com/inventory.html")

@step("URL of the current page")
def url_of_the_current_browser():
    print("------current url-------")

@step("Print the current test")
def print_the_current_test():
    print("-----------current test execution--------------")
