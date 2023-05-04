class Fibonacci:

    def print_fibonacci(n):
        n1,n2=0,1
        n3=None

        for i in range(n):
            n3=n1+n2
            n1=n2
            n2=n3
            print(n3,end=" ")

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

