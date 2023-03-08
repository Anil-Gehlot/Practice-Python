
# 1. len() function : it is used to find the length of tuple, 
#        it shows how many elements are present in the list.

t1 = (1,2,3,43,5,6)
print(len(t1))          # 6


# 2. count() funtion : To return number of occurrences of given element in the tuple.
t2 = (10,20,10,10,20)

print(t2.count(10))     # 3
print(t2.count(20))     # 2


# 3. index() function : it is used to find the index of first occurence of given element.
#                     If the specified element is not available then we will get ValueError.             

t3 = (10,20,10,10,20,30,40)

print(t3.index(10))     # 0
print(t3.index(20))     # 1
print(t3.index(40))     # 7
# print(t3.index(33))     # ValueError: tuple.index(x): x not in tuple


# 4. min() and max() functions: These functions return min and max values according to default natural sorting order.

t4 = (40,10,30,20)

print(min(t4))      # 10
print(max(t4))      # 40


# 5. sorted() function : To sort elements based on default natural sorting order and returns a sorted list.
#                       to use this function element must be homogeneous , not hetrogeneous.

t5 = (1,6,8,14,8,4,0,'s')
t6 = (1,6,8,14,8,4,0,)

# print(sorted(t5))           # TypeError: '<' not supported between instances of 'str' and 'int'
print(sorted(t6))             # [0, 1, 4, 6, 8, 8, 14]


'''
6. cmp():
It compares the elements of both tuples.
If both tuples are equal then returns 0
If the first tuple is less than second tuple then it returns -1
If the first tuple is greater than second tuple then it returns +1

Eg:
t1=(10,20,30)
t2=(40,50,60)
t3=(10,20,30)
print(cmp(t1,t2)) # -1
print(cmp(t1,t3)) # 0
print(cmp(t2,t3)) # +1

Note: cmp() function is available only in Python2 but not in Python 3
'''