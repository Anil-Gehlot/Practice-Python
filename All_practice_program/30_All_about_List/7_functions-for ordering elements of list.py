
# 1. reverse(): we can use reverse() to reverse the order of list.

r1 = [12,2,4,3,648,60,72,3,45,5]
r1.reverse()        # [5, 45, 3, 72, 60, 648, 3, 4, 2, 12]
print(r1)

# 2. sort() function : sort() is used to sort the function according to default natural sorting order.

# For numbers default natural sorting order is Ascending Order.
s1 = [20,5,34,57,7,976,0]
s1.sort()
print(s1)           # [0, 5, 7, 20, 34, 57, 976]

# For strings default natural sorting order is Alphabetical Order.
s2 = ['ANil','anil','bahubali','mahendra',"PRABHAS"]
s2.sort()
print(s2)           # ['ANil', 'PRABHAS', 'anil', 'bahubali', 'mahendra']

#  To use sort() function, compulsory list should contain only homogeneous elements. otherwise we will get TypeError.
s3 = [20,10,"A","B"]
# s3.sort()       # TypeError: '<' not supported between instances of 'str' and 'int' .

# To sort in reverse order : we can sort in reverse order by using 'reverse=True' argument.
a1 = [20,5,34,57,7,976,0]
s2 = ['ANil','anil','bahubali','mahendra',"PRABHAS"]
s1.sort(reverse=True)
s2.sort(reverse=True)
print(s1)       # [976, 57, 34, 20, 7, 5, 0]
print(s2)       # ['mahendra', 'bahubali', 'anil', 'PRABHAS', 'ANil']
