
from getgauge.python import data_store as data
from business_functions.page_objects.login_page_objects import LoginPageObjects
from framework.interface.iweb import IWeb


class LoginPage:
    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def wait_time(self,seconds):
        self.iWeb.wait_time(seconds)

    def login(self, user_name, password):
        self.iWeb.find(LoginPageObjects.txtUsername).type(user_name)
        self.iWeb.find(LoginPageObjects.txtPassword).type(password)
        self.iWeb.find(LoginPageObjects.btnLogin).click()