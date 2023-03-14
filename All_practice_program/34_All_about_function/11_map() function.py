
'''
map() function :
                For every element present in the given sequence,apply some functionality and generate
new element with the required modification. For this requirement we should go for
map() function.

Syntax : map(function,sequence)
The function can be applied on each element of sequence and generates new sequence.
'''
# Q 1. : For every element present in the list perform double and generate new list of doubles.
# without lambda function.
def double(x):
    return x*2

list1 = [1,2,3,56,7]
result = map(double,list1)
print(result)               # <map object at 0x0000021CAB18ED10>
print(list(result))         # [2, 4, 6, 112, 14]

# with lambda function :
l1 = lambda x : x*2
list1 = [1,2,3,56,7]
ans = list(map(l1,list1))
print(ans)                   # [2, 4, 6, 112, 14]
#----------------------------------------------------------------------------------------------------------------------------------

# Q 2. To find square of given numbers.
# without lambda function.

list2 = [3,6,8,0,6]

def square(x):
    return x*x
print(list(map(square,list2)))              #[9, 36, 64, 0, 36]

# with lambda function.

print(list(map(lambda a : a*a,list2)))       # [9, 36, 64, 0, 36]
#----------------------------------------------------------------------------------------------------------------------------------


'''
*** We can apply map() function on multiple lists also.But make sure all list should have same length.

SYNTAX : Syntax: map(lambda x,y:x*y,l1,l2))
        where x is from list1 and y is from list2


'''
# without lambda function.

l5 = [25,78,90,6,5]
l6 = [2,4,54,64,5]

def mult(x,y):
    return x*y
ktm = list(map(mult,l5,l6))
print(ktm)          # [50, 312, 4860, 384, 25]



# with lamda function.
l5 = [25,78,90,6,5]
l6 = [2,4,54,64,5]

final = list(map(lambda x,y:x*y,l5,l6))
print(final)                                # [50, 312, 4860, 384, 25]

# ***if i dont take same element in both list,  the operation will be done on the basis of less element list.

l5 = [13,4,5,6,7,8,89,9]
l6 = [2,4]            

final = list(map(lambda x,y:x*y,l5,l6))
print(final)                  # [26, 16] 


'''
difference between map() & filter() :

In map: Function will be applied to all objects of iterable. 
In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression.

If the element passed in the function returns true the filter function will put the element passed into a new list. 
Where as map function will take an element pass it through a function and return the output of the function and store that to the new list.

In map() we can use as many as sequence we want , but 
In filter() we can only use one function & one seuqence only.

filter() will return the value only when the given boolean condition will be True,
whereas map() checks the condition for each value of given sequence.

**** one of the most suitable distance between them is :

filter() : if the input contain n element(e.g. 10 element) then definitely output element must be less than or equal to n(<=n,   <=10)

map() :  if the input contain n element(e.g. 10 element) then definitely output element exactly n element ...(output element==      or 10 element).

'''

