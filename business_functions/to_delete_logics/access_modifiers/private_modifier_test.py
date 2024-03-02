from private_modifiers import PrivateModifier

test=PrivateModifier()
print(test.__private_variable) #we cant call this variable n function due to private variable
print(test.__private_method())
# var,method=test.expose_private_variable_method()
# print(var,"----",method)
