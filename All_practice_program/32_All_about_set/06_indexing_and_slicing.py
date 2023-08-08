
'''
set objects doesn't support slicing and indexing because set elements
are not ordered.
'''

s1 = {12,321,423,45,35,34}

print(s1[0])            # TypeError: 'set' object is not subscriptable
print(s1[1:5])            # TypeError: 'set' object is not subscriptable
