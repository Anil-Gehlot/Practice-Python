'''
Python contains the following methods to check starting and ending part of the string.

1. str.startswith(substring)
2. str.endswith(substring)

'''

str='learning Python is very easy'
print(str.startswith('learning'))       # True
print(str.endswith('learning'))         # False
print(str.endswith('easy'))             # True
print(str.startswith('l'))              # True
print(str.startswith('b'))              # False
print(str.endswith('b'))                # False
print(str.endswith('y'))                # False



