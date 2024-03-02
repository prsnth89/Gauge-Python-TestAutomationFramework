class TestOverloading:
    #def add(a,b):
    #    return a+b
    
    #def add(a,b,c):   
    #    return a+b+c
    
    #above two concept not allowed instead use below

    def add(*args):
        if len(args)==0:
            return 0
        elif len(args)==1:
            return 1
        else:
            if all(isinstance(arg, str) for arg in args): #check if all arg are string
                return  ''.join(args)
            else:
                return sum(args)

    
print(TestOverloading.add(2,3))
print(TestOverloading.add(2,3,4))
print(TestOverloading.add("prsnth","gopal"))
