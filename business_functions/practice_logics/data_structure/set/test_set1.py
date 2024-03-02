name="prasanth"
test_name=set(name)
test_name=sorted(test_name) #converts the set into list when sorted is used
test_name.append("test append")
test_name.append("test append") #list will allow the duplicate
test_name.reverse()
test_count=test_name.count("test append") #provides the count of key
test_name=set(test_name)  #converted to set once again
test_name.add("test append")
print(test_name)
print(type(test_name))
print(test_count)
