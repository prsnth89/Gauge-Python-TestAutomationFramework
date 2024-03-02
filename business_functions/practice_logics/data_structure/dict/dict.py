test_id={}
test_id['1']='prsnth'
test_id['2']='sruthi'
#print(test_id)


#add multiple dictionary
test1={'1':'prsnth','2':'sruthi'}
test2={'3':'auto','4':'shankar'}
combined_dict={}
combined_dict.update(test1)
combined_dict.update(test2)
#print(combined_dict)

# combined_dict.pop('1')
# print(combined_dict)
#combined_dict.popitem()
#combined_dict.popitem()
print(combined_dict)


for keys,values in combined_dict.items():
    print(keys,values)