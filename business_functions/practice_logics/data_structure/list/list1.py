"""Key Characteristics of Lists in Python:
Ordered: The elements in a list have a specific order, and this order will not change unless explicitly modified.
Mutable: Lists can be changed in place (elements can be added, removed, or modified).
Heterogeneous: Lists can contain elements of different data types (e.g., integers, strings, other lists).
Dynamic: The size of a list can change dynamically, meaning you can add or remove elements as needed."""

a=[10]*5
print(a) #create 10 for 5 times

b=["a",1,2,"b",3.4]
print(b) #list are ordered, mutable-changable, can hold any data types

c=list(range(1,11))
print(c) #list can have numbers 1 to 10

duplicates=[1,1,3,4,5] #list contain duplicats
print(duplicates)

duplicates.insert(3,6) #insert in a specify index
print(duplicates)

duplicates.append(77) #update in last index
print(duplicates)


