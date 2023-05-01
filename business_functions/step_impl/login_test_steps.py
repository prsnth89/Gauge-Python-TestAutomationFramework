from getgauge.python import step
from business_functions.hooks.hooks import Hooks
from getgauge.python import data_store as data
from business_functions.pages.home_page import HomePage
from business_functions.pages.login_page import LoginPage

login_page:LoginPage

@step("Login to sauce demo page")
def login_to_sauce_demo_page():
    print("login")

@step("Enter <user_name> and <password>")
def enter_user_pwd(user_name, password):
    login_page=LoginPage()
    login_page.login(user_name,password)

@step("Click Login to sauce demo page")
def click_login_to_sauce_demo_page():
    print("click login")

@step("Verify if the page got loaded successfully")
def verify_if_the_page_got_loaded_successfully():
    print("verify page ")
    home_page=HomePage()
    home_page.verify_home_page_loaded("https://www.saucedemo.com/inventory.html")