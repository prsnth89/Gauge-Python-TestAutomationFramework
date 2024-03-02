#0 1 1 2 3 5 8 13 21

def fibonacci(n):
    a=0
    b=1
    c=None
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c,end=" ") 
    
fibonacci(8)