'''
1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple object,
    we cannot perform any changes in that object.
    Hence Tuple is Read Only version of List.

2. If our data is fixed and never changes then we should go for Tuple.
3. Insertion Order is preserved
4. Duplicates are allowed
5. Heterogeneous objects are allowed.
6. We can preserve insertion order and we can differentiate duplicate objects by using index. 
    Hence index will play very important role in Tuple also.
    
7. Tuple support both +ve and -ve index. +ve index means forward direction(from left to right)
     and -ve index means backward direction(from right to left)
    
8. We can represent Tuple elements within Parenthesis and with comma seperator.
    Parenethesis are optional but recommended to use.    
'''

# Types of Tuple creation :

# 1. creating empty tuple followed by paranthesis.
t1 = ()
print(type(t1))         # <class 'tuple'>
print(t1)               # ()


# 2. Tuple with only one element.
'''Note: We have to take special care about single valued tuple.compulsary the value
should ends with comma,otherwise it is not treated as tuple.'''

t2 = (10)
t3 = (10,)

print(t2)           # 10
print(t3)           # (10,)
print(type(t2))     # <class 'int'>
print(type(t3))     # <class 'tuple'>


# 3.  creation of multi values tuples without paranthesis (parenthesis are optional).
t4 = 10,2,4,45,57

print(t4)           # (10, 2, 4, 45, 57)
print(type(t4))     # <class 'tuple'>


# 4. By using tuple() fnction : The tuple function can only take one argument.
list1 =[1,4,6,7]

t5 = tuple('s')
t6 = tuple(list1)
t7 = tuple(range(1,10))
print(t5)           # ('s',)
print(type(t5))     # <class 'tuple'>

print(t6)           # (1, 4, 6, 7)
print(type(t6))     # <class 'tuple'>

print(t7)           # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(type(t7))     # <class 'tuple'>
