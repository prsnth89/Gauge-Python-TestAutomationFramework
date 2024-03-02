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