class PrivateModifier:
    def __init__(self) -> None:
        self.__private_variable="This is private variable"

    def __private_method(self):
        return "This is private method"
    
    def expose_private_variable_method(self):
        return self.__private_variable,self.__private_method()