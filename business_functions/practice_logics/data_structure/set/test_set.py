test_set=set()  #Sets are unordered collections of unique elements. 
                #They do not allow duplicate values, and they support mathematical 
                #Set operations like union, intersection, and difference.

duplicate=[1,1,3,4,3,77]
test_set.add(5)
test_set.update(duplicate) 
print(test_set)

for items,duplicate_item in zip(test_set,duplicate): #iteration by zipping two lists
    print("set----",items,end=" ")
    print("duplicate item----",duplicate_item)

#if list1 have 5 items, list2 have 3 items then zip(list1,list2) and it will iterate n print all items from list1 and list2
#if zip(list2,list1) then it will iterate list2 first [3 items will be iterated] and also in list1 [only 3 items iterated]

for duplicate_item,items in zip(duplicate,test_set): 
    print("duplicate item----",duplicate_item)       
    print("set----",items,end=" ")