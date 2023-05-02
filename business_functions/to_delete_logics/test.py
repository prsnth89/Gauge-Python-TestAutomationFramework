class Fibonacci:

    def print_fibonacci(n):
        a,b=0,1

        for i in range(n):
            print(a,end=" ")
            a,b=b, a+b

#Fibonacci.print_fibonacci(10)

class Factorial:

    def print_factorial(n):
        fact=None
        if n==0 or n==1:
            return 1
        else:
            fact=n*Factorial.print_factorial(n-1)
            print(fact)
            return fact
fact=Factorial.print_factorial(5)
#print(fact)

class ReverseString:

    def reverse(string_reverse):
        return string_reverse[::-1]
#print(ReverseString.reverse('Prasanth'))


name='sruthi'
print(name[::-1])

