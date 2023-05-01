
from getgauge.python import data_store as data
from business_functions.page_objects.login_page_objects import LoginPageObjects
from framework.interface.iweb import IWeb


class LoginPage:
    iWeb: IWeb
    def __init__(self):
        self.iWeb=data.scenario.iweb

    def login(self, user_name, password):
        self.iWeb.find(LoginPageObjects.txtUsername).type(user_name)
        self.iWeb.find(LoginPageObjects.txtPassword).type(password)
        self.iWeb.find(LoginPageObjects.btnLogin).click()

