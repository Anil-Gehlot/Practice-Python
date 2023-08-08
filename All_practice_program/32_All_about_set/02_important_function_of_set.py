
# 1. add(x) : adds item x to the set.

s1 = {1,2,3,4}

s1.add(6)
print(s1)           # {1, 2, 3, 4, 6}
# s1.add(7,8)             # TypeError: set.add() takes exactly one argument (2 given)

# ***TypeError: unhashable type: 'list' :==>> This error is raised because a set can only contain immutable types.
# s1.add({1,2,3})           # TypeError: unhashable type: 'set'
# s1.add([1,2,3,4])           # TypeError: unhashable type: 'list'

s1.add((5,6,7,8,4))         # tuple is immutable , so it is added successfully.
print(s1)           # {1, 2, 3, 4, (5, 6, 7, 8, 4), 6}


'''
2. update(x,y,z) : 

update() method is used to To add multiple items to the set.
update method takes only iterable object like(list,tuple etc.)
All the element present in the iterable object will be added to set. 
You can add as many arguments as you want, just separate them with a comma.
'''

s2={10,20,30}
l=['a','b','c','d']
s2.update(l,range(5))
print(s2)        # {0, 1, 2, 3, 4, 10, 20, 'a', 'd', 'b', 'c', 30}
print()

s3={10,20,30}
# s3.update(1,3,4,5)      # TypeError: 'int' object is not iterable
# it gives TypeError : because update method takes only iterable object like(list,tuple etc.)
 
'''
Q. What is the difference between add() and update() functions in set ?

A. We can use add() to add individual item to the Set,where as we can use update() function  to add multiple items to Set.

B. add() function can take only one argument where as update() function can take any number of arguments but
     all arguments should be iterable objects.
 
     
1. s.add(10)            ==>> Valid
2. s.add(10,20,30)      # TypeError: add() takes exactly one argument (3 given)
3. s.update(10)         #  TypeError: 'int' object is not iterable
4. s.update(range(1,10,2),range(0,10,2))        ==>> Valid
'''


# 3. copy(): Returns copy of the set. It is cloned object.

s4 = {1,2,3,4}
s5 = s4.copy()

print(id(s4))           # 2133828559008
print(id(s5))           # 2133828560352


# 4. pop() : It removes and returns some random element from the set.

s6 = {7,8,9,0,6,5,9}
print(s6)           # {0, 5, 6, 7, 8, 9}
print(s6.pop())     # 0
print(s6)           # {5, 6, 7, 8, 9}


'''
 5. remove(x) : It removes specified element from the set.
          If the specified element not present in the Set then we will get KeyError. 
'''   

s7 = {24,2345,35,34,645,675,345}
s7.remove(345)
print(s7)           # {34, 35, 675, 645, 24, 2345}
# s7.remove(245)    # KeyError: 245


'''
6.  discard(x): It removes the specified element from the set.
              If the specified element not present in the set then we won't get any error.  
'''

s8 = {10,20,40}
s8.discard(20)
print(s8)           # {40, 10}
s8.discard(30)      # It will not raise any error.
print(s8)           # {40, 10}

'''
Q. What is the difference between remove() and discard() functions in Set?
ANS: removes() removes specified element from the set.If the specified element not present in the Set then we will get KeyError.
    whereas discard() removes the specified element from the set.If the specified element not present in the set then we won't get any error.


Q. Explain differences between pop(),remove() and discard() functionsin Set?
ANS : pop() removes and returns some random element from the set.
'''

# 7.clear(): To remove all elements from the Set.
s9 = {2,423,4,235,3245,34,51,2}
s9.clear()          # clear() function doesn't take any argument.
print(s9)           # set()
