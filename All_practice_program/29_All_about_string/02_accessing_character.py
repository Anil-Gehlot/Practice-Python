'''
How to access characters of a String: We can access characters of a string by using the following ways.

1. By using index
2. By using slice operator

1. By using index :

Python supports both +ve and -ve index.
+ve index means left to right(Forward direction)
-ve index means right to left(Backward direction)
'''

a = 'anil prabhas'
print(a[0])         # a         
print(a[5])         # p
print(a[-1])        # s
# print(a[91])        # IndexError: string index out of range.
# print(a[-23])       # IndexError: string index out of range
'''Note: If we are trying to access characters of a string with out of range index then we will get
error saying : IndexError'''

'''
Q. Write a program to accept some string from the keyboard and display its characters by
index wise(both positive and nEgative index)
'''

str = input("Enter string : ")
a = 0
l = len(str)
for i in str:
    print(f'The character present at positive index {a} and at negative index {-l} is : {i}')
    a = a + 1
    l = l - 1


"""
2. Accessing characters by using slice operator:
Syntax: s[bEgin:end:step]

begin: jaha se start karna he.
end:  jaha pe khatam karna he. 
step: incremented value
Note: If we are not specifying bEgin index then it will consider from bEginning of the string.
If we are not specifying end index then it will consider up to end of the string
The default value for step is 1. step value can be either +ve or –ve.

if +ve then it should be forward direction(left to right) and we have to consider bEgin to end-1
if -ve then it should be backward direction(right to left) and we have to consider bEgin to end+1

***Note:
In the backward direction if end value is -1 then result is always empty.
In the forward direction if end value is 0 then result is always empty. 
"""

s = "Learning Python is very very easy!!!"

print(s[1 :7 ])         # earnin : because default stepper is one.
print(s[1:25:2])        # erigPto svr
print(s[:8])            # Learning : from starting to specified end value.
print(s[8:])            #  Python is very very easy!!!
print(s[:])             # Learning Python is very very easy!!!
print(s[::])            # Learning Python is very very easy!!!
print(s[::-1])          # !!!ysae yrev yrev si nohtyP gninraeL
