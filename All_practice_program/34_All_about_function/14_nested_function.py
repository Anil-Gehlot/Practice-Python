
'''
We can declare a function inside another function, such type of functions are called Nested functions.

we can call any function to inside another function ,
But can't call a inner function to outside of that particular function.
'''

def outside():
    print("come outside")

    def inside():
        print("come inside")

    print("calling inside function ")
    inside()

outside()
'''
output:

come outside
calling inside function
come inside
'''

# inside()                # NameError: name 'inside' is not defined

#----------------------------------------------------------------------------------------------

# a function can also return another function.

def out():
    print("outer function started")
    def ins():
        print("inner function execution") 
    print("outer function returning inner function")
    return ins
a1=out()
a1()
a1()
a1()
'''
output: 

outer function started
outer function returning inner function
inner function execution
inner function execution
inner function execution'''


#----------------------------------------------------------------------------------------------
def outer():
    print("outer function started ")
    def inner():
        print("inner function execution ")
    print("outer function returning inner function")
    # return inner() : if i write this type then it means , we are calling inner function and ,
    # what inner function is returning , we are returning that returned value. 
    return inner



outer()         # because we did not call inner function inside the outer function
'''
output:

outer function started 
outer function returning inner function'''

f1 = outer()
print(f1())
'''
output:

outer function started
outer function returning inner function
inner function execution
None
'''
f1()                # inner function execution
f1()                # inner function execution
#----------------------------------------------------------------------------------------------

# calling a function inside another function.

def greet():
    print('Hii.. How are you ??')

def wish():
    greet()
    print("Happy birthday")

wish()
'''
OUTPUT :

Hii.. How are you ??
Happy birthday
'''
#----------------------------------------------------------------------------------------------

'''Q. What is the differenece between the following lines?
                f1 = outer
                f1 = outer()

1) In the first case for the outer() function we are providing another name f1(function aliasing).

2) But in the second case we calling outer() function,which returns inner function.For that inner
    function() we are providing another name f1

Note: We can pass function as argument to another function
Eg:              
                 filter(function,sequence)
                 map(function,sequence)
                 reduce(function,sequence)

 '''
