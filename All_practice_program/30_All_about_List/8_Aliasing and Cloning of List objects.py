
# The process of giving another reference variable to the existing list is called aliasing.
x = [10,20,30,40,50]
y = x
print(id(x))        # 2128840370752
print(id(y))        # 2128840370752
# hence both x and y refers to the object [10,20,30,40,50]

"""
The problem in this approach is by using one reference variable if we are changing
content,then those changes will be reflected to the other reference variable.
"""
# For eg.
x = [10,20,30,40,50]
y = x
y.append(56)
print(x)        # [10, 20, 30, 40, 50, 56]
print(y)        # [10, 20, 30, 40, 50, 56]

'''
To overcome this problem we should go for cloning.
The process of creating exactly duplicate independent object is called cloning.
We can implement cloning by using slice operator or by using copy() function
'''

# By using slice operator.
a = [10,20,30,40] 
b = a[::]

print(id(a))        # 2533606260480
print(id(b))        # 2533606260544

b.append(345)
print(a)        # [10, 20, 30, 40]
print(b)        # [10, 20, 30, 40, 345]

# By using copy() function :
c = ['a','b','c','d']
d = c.copy()

print(id(c))        # 2020302006400
print(id(d))        # 2020302261760

d.append('anil')
print(c)        # ['a', 'b', 'c', 'd']
print(d)        # ['a', 'b', 'c', 'd', 'anil']

