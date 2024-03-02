class DecoratorLogic:
    def login(self):
        print("Login into application")

    def pre_post_condition(self,func):
        def wrapper():
            print("Enter username/password")
            func()
            print("Verify Login Successful")
        return wrapper


class TestDecorator:
    test=DecoratorLogic()
    dec_logic=test.pre_post_condition(test.login)
    dec_logic()   #Enter username/password
                  #Login into application
                  #Verify Login Successful