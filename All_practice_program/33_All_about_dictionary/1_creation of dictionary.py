'''
If we want to represent a group of objects as key-value pairs then we should go for Dictionary.
Syntax :  dict={key:value, key:value}

We can use List,Tuple and Set to represent a group of individual objects as a single entity within dictionary.
Eg:        name -> roll no.
        address -> mobile no.

Duplicates keys are not allowed but values can be duplicated.
Hetrogeneous objects are allowed for both keys and values.
insertion order is not preserved.
Dictionaries are mutable.
Dictionaries are dynamic.
Indexing and Slicing concept not applicable on dictionaries.

Note: In C++ and Java Dictionaries are known as "Map" where as in Perl and Ruby it is known as "Hash"
'''

# Creation of dictionary :

# If we know data in advance then we can create dictionary as follows
d1 = {'anil':'MCA',"manoj":'b.com','manish':'BCA'}
print(d1)               # {'anil': 'MCA', 'manoj': 'b.com', 'manish': 'BCA'}

# we are creating empty dictionary. We can add entries into dictionary.
d2 = {}             # empty dictionary
d3 = dict()         # empty dictionary

d2[100] = 'hundred'
d2[200] = 'Two hundred'
d2[300] = 'Three hundred'
d3["A"] = 'a'
d3["B"] = 'b'
d3["C"] = 'c'

print(d2)       # {100: 'hundred', 200: 'Two hundred', 300: 'Three hundred'}
print(d3)       # {'A': 'a', 'B': 'b', 'C': 'c'}
