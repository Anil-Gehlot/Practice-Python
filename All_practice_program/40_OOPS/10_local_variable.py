'''
Sometimes to meet temporary requirements of programmer,we can declare variables inside a
method directly,such type of variables are called local variable or temporary variables.

Local variables will be created at the time of method execution and destroyed once method
completes.

Local variables of a method cannot be accessed from outside of method.
'''

# Example 1:
class Test:
    def m1(self):
        a = 100
        print(a)
    def m2(self):
        b = 200
        print(b)
t = Test()
t.m1()      # 100
t.m2()      # 200
print('-------------------------------------------------------------')


# Example 2:
# if we try to access local variable, from outside the method...it will raise NameError...

class Test1:
    def m1(self):
        a = 100
        print(a)
    def m2(self):
        b = 200
        print(a)        # #NameError: name 'a' is not defined 
        print(b)