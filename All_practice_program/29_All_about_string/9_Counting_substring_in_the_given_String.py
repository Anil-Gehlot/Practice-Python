'''
We can find the number of occurrences of substring present in the given string by using count()
method.
1. s.count(substring) ==> It will search through out the string.
2. s.count(substring, bEgin, end) ===> It will search from bEgin index to end-1 index.
'''

a = "abcabcabcabcadda"
print(a.count('a'))     # 6
print(a.count('ab'))        #4
print(a.count('d'))     # 2
print(a.count('a',3,7))     # 2

"""
if we give invalid begin index, it will give output as 0.
if begin index is right but ending index is out of range it will give the correct answer"""
print(a.count('a',35,44))     # 0
print(a.count('a',3,44))     # 5
