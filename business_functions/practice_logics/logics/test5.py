tuples=(33,44,55)
print(tuples)

def get_name_age():
    name="prasanth"
    age=32
    return name, age

name,age=get_name_age()
print(name,age)

#dict  with tuples to sort in reverse order
dict_name_age={102:("prasanth",33),103:("sruthi",27),101:("jisha",28)}
print(dict_name_age.get(100))
sorted_keys=sorted(dict_name_age.keys(), reverse=True)
sorted_dict={}
for key in sorted_keys:
    sorted_dict[key] =dict_name_age[key]

print(sorted_dict)


#set -to remove duplicate
keys=[22,44,11,22,44,55,33]
keys=set(keys)
print(keys)


import numpy as np
my_array = np.arange(10)
print(my_array)