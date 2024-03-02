person1=(1,'prsnth',32)
person2=(2,'sruthi',27)
person3=(3,'john',33)

id,name,age=person1  #just assigning variables will split values
print(id,name,age)

no_of_ppl={'person1':person1,
           'person2':person2,
           'person3':person3}


for ppl in no_of_ppl:
    print(no_of_ppl.get(ppl)[1])