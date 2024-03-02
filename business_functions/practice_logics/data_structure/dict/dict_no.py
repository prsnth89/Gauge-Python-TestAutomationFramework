#Dictionaries are collections of key-value pairs. 
#They are unordered, mutable, and can contain elements of different data types. 
#Keys don’t allow duplicate

test_no=dict()
test_no[1]="one"
test_no.update({2:"two",3:"three"})
for key,val in test_no.items():
    print(key,val)
    if key==3:
        test_no.update({1:"one duplicate"})
        break
    elif key==2:
        print(test_no.get(key))

print(test_no)


