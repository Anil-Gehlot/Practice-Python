'''
It is very easy and compact way of creating list objects from any iterable 
    objects(like list,tuple,dictionary,range etc) based on some condition.

    Syntax:
    list=[expression for item in list if condition]
'''
l1 = [i*i for i in range(10)]
print(l1)       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


l2 = [2**j for j in range(7)]
print(l2)       # [1, 2, 4, 8, 16, 32, 64]


l3 = [k for k in l1 if k%2==0]
print(l3)       # [0, 4, 16, 36, 64]


name = ['anil','Harsh','lokesh','paritosh']
letters = [x[0] for x in name]
print(letters)      # ['a', 'H', 'l', 'p']


num1 = [10,20,30,40]
num2= [30,40,50,60]
num3= [ i for i in num1 if i not in num2]
num4 = [ i for i in num1 if i in num2]
print(num3)          # [10,20] 
print(num4)          # [30, 40]


words="the quick brown fox jumps over the lazy dog".split() 
print(words)         # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
l5 = [[i.upper() , len(i)] for i in words]
print(l5)           # [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]