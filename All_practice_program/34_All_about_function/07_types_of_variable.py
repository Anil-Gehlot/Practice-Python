
'''
Types of Variables : 

python supports 2 type of variables :
1) Global variables.
2) Local variables.

1) Global variables : The global variable which are declared outside of a function are called global variables.
                    These variable can be accessed in all functions of that modules.

2) Local variables : The variable which are declared inside a function are called local variable.
                    Local variable are availabel only for the function in which we declared it.
                    Means we can't access local variable outside to that function.

 
====>>>>   global keyword: We can use global keyword for the following 2 purposes :
                    A.  To declare a global function inside the function.
                    B.  To make global variable available to th function, so that we can perform required modification.


'''

# Example 1.
a = 10          # global variable
def f1():
    print(a)
def f2():
    print(a)

f1()            # 10
f2()            # 10

# Example 2.

def f3():
    b = 34          # local variable
    print(b)            # 34

def f4():
    print(b)            # NameError: name 'b' is not defined.

f3()
f4()


# Example 3: defining global keyword inside the function.

d =45
def f5():
    global e,d
    e = 34
    d = 67              # this d = 67 will overwrite d = 45
    print(d,e)      # 67 34

def f6():
    print(e, d)        # 34 67

f5()
f6()


# Example 4 : 
p=10
def f7():
    global p
    p=777
    print(p)            # 777
def f8():
    print(p)            # 777

f7()
f8()


# Example 5 : 
'''
if there is a golbal outside the function & local variable with same name inside the function,
 then local variable will be executed firstly : because it has higher priority.
''' 
x = 789
def f9():
    x = 111
    print(x)            # 111
def f10():
    print(x)            # 789

f9()
f10()


# Example 6 : 
# Never do this kind of mistakes 👇👇
def f0():
    y = 19
    global y
    y =78
    print(y)            # SyntaxError: name 'y' is assigned to before global declaration
f0()



#----------------------------------------------------------------------
'''
*** Note : If global variable and local variable having the same name then we can access
global variable inside a function as follows.
'''
s = 23
def f11():
    s = 789
    print('local : ',a)                     # local :  10
    print('global : ',globals()['s'])       # global :  23
f11()
