from collections import Counter

def duplicate(list_no):
    dupl=Counter(list_no)
    return dupl

nos=[1,1,2,4,3,2]
duplicate_item=duplicate(nos)
print(duplicate_item)
print(dict(duplicate_item))