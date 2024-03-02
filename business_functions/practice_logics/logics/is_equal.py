a=[1,2]
b=[1,2]
print(a==b) #compare values
print(a is b) #compare memory address
print(hex(id(a))) #memory address
print(hex(id(b))) 
b=a
print(a is b)
print(hex(id(a))) #memory address
print(hex(id(b))) 