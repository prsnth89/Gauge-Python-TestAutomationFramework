#1*2*3*4*5=120

def fact(n):
    fact_calc=1
    for i in range(1,n+1):
       print(i)
       fact_calc =fact_calc*i  
    print(fact_calc)

fact(5)