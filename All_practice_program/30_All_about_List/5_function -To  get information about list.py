
# len() function : returns the number of elements present in the list.
l1 = [1,2,2,2,2,3,3,3,'3','3','anil','harsh',5+9j,True,False]
print(len(l1))            # 15

#  count(): It returns the number of occurrences of specified item in the list.
print(l1.count(3))        # 3
print(l1.count('3'))      # 2
print(l1.count(2))        # 4
print(l1.count(5))        # 0

# index() function: returns the index of first occurrence of the specified item.
#  If the specified element not present in the list then we will get ValueError.
print(l1.index(3))        # 5
print(l1.index('3'))      # 8
print(l1.index(2))        # 1
# print(l1.index(5))        # ValueError: 5 is not in list




