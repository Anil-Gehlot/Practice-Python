

'''

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. 
These methods are called overloaded methods and this is called method overloading. 

If 2 methods having same name but different type of arguments then those methods are said to
be overloaded methods.

But in Python Method overloading is not possible.
If we are trying to declare multiple methods with same name and different number of arguments
then Python will always consider only last method.
'''

# Example:
class Test:
    def m1(self):
        print('No-argument Method')

    
    def m1(self,a):
        print('One-argument Method')

    
    def m1(self,b,c):
        print('Two-argument Method')

t = Test()

# t.m1()              # TypeError: Test.m1() missing 1 required positional argument: 'b'
# t.m1(10)              # TypeError: Test.m1() missing 1 required positional argument: 'c'

t.m1(3, 5)              # Two-argument Method

print('----------------------------------------------------------------------------------------------------------------')


'''
How we can handle overloaded method requirements in Python:

Most of the times, if method with variable number of arguments required then we can handle
with default arguments or with variable number of argument methods
'''

# Example 1 :

class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The Sum:',total)

t=Test()
t.sum(10,20)                # The Sum: 30
t.sum(10,20,30)             # The Sum: 60
t.sum(10)                   # The Sum: 10
t.sum()                     # The Sum: 0
print('----------------------------------------------------------------------------------------------------------------')



class Test1:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!= None and c!= None:
            print('The Sum of 3 Numbers:',a+b+c)
        elif a!=None and b!= None:
            print('The Sum of 2 Numbers:',a+b)
        else:
            print('Please provide 2 or 3 arguments') 

t1 = Test1()

t1.sum(10,20)               # The Sum of 2 Numbers: 30
t1.sum(10,20,30)            # The Sum of 3 Numbers: 60
t1.sum(10)                  # Please provide 2 or 3 arguments