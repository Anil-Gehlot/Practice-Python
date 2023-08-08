"""
len() in-built function: We can use len() function to find the number of characters present in the string.

"""
a = 'anil'
b = 'Hello, I am ANIL !!!'
print(len(a))           # 4
print(len(b))           # 20
print()

'''
Q. Write a program to access each character of string in forward and backward direction
by using while loop?
'''

b = 'Hello, I am ANIL !!!'
i = 0
l = len(b)

print(" IN forward direction : ")
while i<=l-1:
    print(f"At the index {i} : {b[i]} ")
    i =i+1
print()
print(" IN backward direction : ")

i = -1
while i>=-len(b):
    print(f'At the index {i} : {b[i]}')
    i = i-1


'''Alternative ways: to solve the above question...'''
# first way
for j in b:
    print(j,end=" " )  # forward direction
print()

# second way
print(b[::])            # forward direction

# third way 
print(b[::-1])          # Backward direction
