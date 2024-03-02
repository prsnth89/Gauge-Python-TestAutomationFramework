nos=[1,1,2,3,4,2,2,5]

def find_duplicate(list_item):
    store_unique_val=set()
    duplicates=[]

    for item in list_item:
        if item in store_unique_val:
            duplicates.append(item)
        else:
            store_unique_val.add(item)
    print("Duplicates--->",duplicates)
    print("unique value---",store_unique_val)

def no_of_duplicate(list_item):
    count={}
    duplicates=[]
    for item in list_item:
        if item in count:
            count[item]+=1

            if count[item]==2:
                duplicates.append(item)
        else:
            count[item]=1

    
    

find_duplicate(nos)

