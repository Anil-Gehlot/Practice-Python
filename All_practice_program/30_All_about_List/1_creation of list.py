'''
If we want to represent a group of individual objects as a single entity where insertion
order preserved and duplicates are allowed, then we should go for List.

Lists are used to store multiple element in a single variable.
We can create 'List' using Square brackets[].

In List :
       1) insertion order preserved.
       2) duplicate objects are allowed
       3) heterogeneous objects are allowed.
       4) List is dynamic because based on our requirement we can increase the size and decrease the size.     
       5) In List the elements will be placed within square brackets and with comma seperator.
       6)  List objects are mutable.i.e we can change the content.
       
       Python supports both positive and negative indexes. +ve index means from left to right
        where as negative index means right to left
        
        Example of list :  [10,"A","B",20, 30, 10] 
        '''

# Creation of list :

# 1st Way :
list1 = [ 1,2,3,3,2,'a',3+5j]
print(type(list1))          # <class 'list'>

# 2nd way :
list2 = []          # creation of empty list.
print(type(list2))          # <class 'list'>

#3rd way : by user input.
list3 = eval(input("Enter list : "))            # [1,2,3,'r']
print(list3)
print(type(list3))      # <class 'list'>

# 4th way :with list() function.
list4 = list(range(0,10))
print(list4)            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(list4))      # <class 'list'>

# 5th way : with split() function.
str = 'Hello I am anil Gehlot !!'
l = str.split()
print(type(l))           # <class 'list'>
print(l)                # ['Hello', 'I', 'am', 'anil', 'Gehlot', '!!']

# 5th way : with sorte() function in shorted way.
str = 'Hello I am anil Gehlot !!'
s = sorted(str)
print(type(s))      # <class 'list'>
print(s)            # [' ', ' ', ' ', ' ', ' ', '!', '!', 'G', 'H', 'I', 'a', 'a', 'e', 'e', 'h', 'i', 'l', 'l', 'l', 'l', 'm', 'n', 'o', 'o', 't']

'''
    *****Nested List*****
    Sometimes we can take list inside another list,such type of lists are called nested lists.
    
    Ex. ==>> [10,20,[30,40],45,68,['a','x']]
'''