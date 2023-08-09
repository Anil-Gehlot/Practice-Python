
'''

Constructor overloading is not possible in Python.
If we define multiple constructors then the last constructor will be considered.
'''



# In the below program only Two-Arg Constructor is available.

class Test:
    def __init__(self):
        print('No-Arg Constructor.')
    
    def __init__(self, a):
        print('One-Arg constructor.')

    def __init__(self, a, b):
        print('Two-Arg constructor.')

# t = Test()              # TypeError: Test.__init__() missing 2 required positional arguments: 'a' and 'b'
# t = Test(10)            # TypeError: Test.__init__() missing 1 required positional argument: 'b'
t = Test(10, 20)          # Two-Arg constructor.



'''

Based on our requirement we can declare constructor with default arguments and variable
number of arguments.

Constructor with Default Arguments:
'''

# Example 1:

class Test1:
    def __init__(self, a = None, b = None, c = None):
        print('Constructor with 0, 1, 2 or 3 number of arguments.')

t1 = Test1()
t1 = Test1(10)
t1 = Test1(10,20)
t1 = Test1(10,20,30)

'''
OUTPUT:

Constructor with 0, 1, 2 or 3 number of arguments.
Constructor with 0, 1, 2 or 3 number of arguments.
Constructor with 0, 1, 2 or 3 number of arguments.
Constructor with 0, 1, 2 or 3 number of arguments.
'''







# Example 2: Constructor with Variable Number of Arguments:

class Test2:
    def __init__(self, *args):
        print('Constructor with variable number of arguments.')


t2 = Test2()
t2 = Test2(10)
t2 = Test2(10,20)
t2 = Test2(10,20,30)
t2 = Test2(324,23,423,4,234,23,423,4)


'''
OUTPUT:

Constructor with variable number of arguments.
Constructor with variable number of arguments.
Constructor with variable number of arguments.
Constructor with variable number of arguments.
Constructor with variable number of arguments.
'''
