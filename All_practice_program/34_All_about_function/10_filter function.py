
'''
filter() function: 

            The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

            We can use filter() function to filter values from the given sequence based on some condition.

            The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
            
Syntax : filter(function,sequence(iterable))

where function argument is responsible to perform conditional check
sequence can be list or tuple or string.
            
            
            '''

# filter function can only take atmost 2 arguments , nothing much nothing more.

l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(filter(lambda x,y:x*y,l1,l2))                   # TypeError: filter expected 2 arguments, got 3
print(l3) 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Q 1. Without lambda function.
ages = [34,6,78,5,2,2,3,4,36,2,3,22]

def func(x):
    if x > 18:
        return True
    else:
        return False
print(filter(func,ages))                # <filter object at 0x0000020A4864FBB0>

final = list(filter(func,ages))
print(final)                            # [34, 78, 36, 22]

# Q 1. With lambda function.

ages = [34,6,78,5,2,2,3,4,36,2,3,22]

result = filter(lambda a : a>18,ages)
print(list(final))                      # [34, 78, 36, 22]
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Q 2. find vowels.
# with out lambda function.
vowel = ['a','e','i','o','u']

list1 = [12,3,'a','f','h',5,'g','f','u']
def func2(x):
    if x in vowel:
        return True
    else:
        return False

ans = list(filter(func2,list1))
print(ans)                          # ['a', 'u']

# with lambda function.
b = lambda x : x in vowel

answer = list(filter(b,list1))
print(answer)                       # ['a', 'u']
#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Q. Program to filter only even numbers from the list by using filter() function ?
# without lambda function.

l=[0,5,10,15,20,25,30]

def even(x):
    if x%2==0:
        return True
    else:
        return False
    
a1 = list(filter(even,l))
print(a1)                       # [0, 10, 20, 30]


# with lambda function.
l2=[0,5,10,15,20,25,30]
a2 = lambda z : z%2==0
final1 = list(filter(a2,l2))
print(final1)                   # [0, 10, 20, 30]