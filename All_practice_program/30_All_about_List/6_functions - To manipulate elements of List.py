'''
List objects are dynamic. i.e based on our requirement we can increase and decrease the
size.

append(), insert(), extend() : to increase the size of list.
remove() , pop() : to decrease the size of list.
'''
# 1. append() function: We can use append() function to add item at the end of the list.

list1 = []
list1.append('anil')
list1.append(8)
list1.append(332)
list1.append('prabhas')
list1.append('23 october')
print(list1)            # ['anil', 8, 332, 'prabhas', '23 october']

#Eg: To add all elements to list upto 100 which are divisible by 10
list2 = []
for i in range(101):
    if i%10==0:
        list2.append(i)
print(list2)        # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

''' 
2. insert() function: To insert item at specified index position.
              syntax : list.insert(index,'item')

        **If the specified index is greater than max index then element will be inserted at last position. 
        **If the specified index is smaller than min index then element will be inserted at first position.    
'''
list3 = [1,2,3,4,45,6,7,88,9,0]

list3.insert(3,'anil')
print(list3)        # [1, 2, 3, 'anil', 4, 45, 6, 7, 88, 9, 0]

list3.insert(69,'harsh')
list3.insert(-2,"bhahubali")
print(list3)            # [1, 2, 3, 'anil', 4, 45, 6, 7, 88, 9, 'bhahubali', 0, 'harsh']

list3.insert(-15,"mahendra")
print(list3)            # ['mahendra', 1, 2, 3, 'anil', 4, 45, 6, 7, 88, 9, 'bhahubali', 0, 'harsh']
"""
***Difference between append() & insert()....
            In list when we append any element in list, it will be added in last i.e. it will be last element ..
            BUT if we use insert() method , we can insert any element at particular index.
"""

# 3. extend() function : To add all element of one list into another list 
# Syntax : l1.extend(l2) ==>> all element of l2 will be added into l1.

order1 = ['vada paav', 'masala dosa','idli sambhar']
order2 = ['sandwich','pizza','chhole kulchhe']
order1.extend(order2)
print(order1)           # ['vada paav', 'masala dosa', 'idli sambhar', 'sandwich', 'pizza', 'chhole kulchhe']

order3 = ['panir tikka','potato slice']
order3.extend("laddu")
print(order3)           # ['panir tikka', 'potato slice', 'l', 'a', 'd', 'd', 'u']


# 4. remove() function: remove function is used to remove only first occurrence of specified element from the list. 
a1 = [1,2,3,4,5,64,3,2]
a1.remove(2)
print(a1)           # [1, 3, 4, 5, 64, 3, 2]
a1.remove(3)
print(a1)           # [1, 4, 5, 64, 3, 2]
# If the specified item not present in list then we will get ValueError.
# a1.remove(9)           # ValueError: list.remove(x): x not in list


# 5. pop() function : pop function removes & returns the last element of the list.

b1 = [10,20,30,40]
b2 = []
b1.pop()
print(b1)       # [10, 20, 30]
print(b1.pop())     # 30 : because it is the only function in list , which returns some element.

# If the list is empty then pop() function raises IndexError.
# b2.pop()        # IndexError: pop from empty list.

# we can also use pop() to delete element by index value.
b3 = [1,23,4,5,34,5,645,7,]
b3.pop(6)
print(b3)           # [1, 23, 4, 5, 34, 5, 7]
b3.pop(2)
print(b3)           # [1, 23, 5, 34, 5, 7]

"""
***Difference between remove() and pop()

remove(): 
1) We can use to remove special element from the List.
2) It can't return any value. 
3) If special element not available then we get VALUE ERROR.

pop():
1) We can use to remove last element from the List.
2) It returned removed element.
3) If List is empty then we get error.
"""

# 6. clear() function: We can use clear() function to remove all elements of List.
n=[10,20,30,40]
print(n)        # [10, 20, 30, 40]
n.clear()
print(n)        # []