
'''
1) If we want to represent a group of unique values as a single entity then we should go for set.
2) Duplicates are not allowed in set.
3) Insertion order is not preserved.But we can sort the elements.
4) Indexing and slicing not allowed for the set.
5) Heterogeneous elements are allowed.
6) Set objects are mutable i.e once we creates set object we can perform any changes in
    that object based on our requirement.
7) We can represent set elements within curly braces and with comma seperation.
8) We can apply mathematical operations like union,intersection,difference etc on set objects.
'''

# Creation of Set objects : 

# 1st way :
s = {10, 20, 30, 40}
print(s)            # {40, 10, 20, 30}
print(type(s))      # <class 'set'>


# 2nd way : We can create set objects by using set() function.
            # Syntax : s=set(any sequence)   ==>> set() takes only one argument.
l = [243,45,3,5]
s1 = set(l)
s2 = set({12,3,4,45})
s3 = {}         # it is not an empty set, it is treated as empty dictionary.
s4 = set()      # creation of empty set. 
s6 = set(range(5))

print(s1)           # {3, 5, 243, 45}
print(type(s1))     # <class 'set'>

print(s2)           # {4, 3, 12, 45}
print(type(s2))     # <class 'set'>

print(s3)           # {}
print(type(s3))     # <class 'dict'>

print(s4)           # set()
print(type(s4))     # <class 'set'>

print(s6)           # {0, 1, 2, 3, 4}
print(type(s6))     # <class 'set'>
