'''
We can use comparison operators for List objects.

Whenever we are using comparison operators(==,!=) for List objects then the following
should be considered....
    1. The number of elements should be same in list.
    2. The order of elements should be same in list.
    3. The content of elements (case sensitive) should be in same case.
'''

x = ["Dog","Cat","Rat"]
y = ["Dog","Cat","Rat"]
z = ["DOG","CAT","RAT"]

print(x==y)     # True
print(y==z)     # False
print(x!=z)     # True


'''
Note: When ever we are using relatational operators(<,<=,>,>=) between List objects,
        only first element comparison will be performed.
'''
print()
a = ["Dog","Cat","Rat"]
b = ["Rat","Cat","Dog"] 

print(a > b)        # False
print(a >=b)        #False
print(a < b)        # True
print(a <=b)        # True