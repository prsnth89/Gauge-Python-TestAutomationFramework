set1={1,2,3}
set2={3,4,5,6}
combined_set=set()
combined_set=set1.union(set2)
print(combined_set)


diff=combined_set.difference(set1)  #removes the set1 elements ie)1,2,3 removed
print(diff)

combined_set=set(combined_set)
combined_set.discard(4) #remove the element without any error, if element is not found then no error will be thrown
print(combined_set)
combined_set.discard(4) #element not available
print(combined_set) 

combined_set.remove(5) #element remove
print(combined_set)

