"""A lambda function in Python is a small, anonymous function defined using the lambda keyword. 
Unlike regular functions defined using the def keyword, lambda functions are used for creating 
simple functions without a name. They are particularly useful for short, throwaway functions that 
are only needed temporarily, often as arguments to higher-order functions like map(), filter(), and sorted().

eg: lambda arguments: expression
"""

add=lambda x,y:x+y
sub=lambda x,y,z:x**2-y-z
is_even=lambda x:x%2==0
sort_by_asc=lambda x:sorted(x)
sort_by_desc=lambda x:sorted(x,reverse=True)
print(sub(5,2,1))
print(is_even(3))
list1=[1,5,4,3,2]
print(sort_by_asc(list1))
print(sort_by_desc(list1))