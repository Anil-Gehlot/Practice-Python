
"""
Example of function :
            def func(a,b):
                c = a+b
                return c
            func(5,10)

In the above function a&b are formal parameter,
whereas 5 & 10 are actual argument or parameter.


Types of arguments :

1) positional argument.
2) keyword argument.
3) default argument.
4) variable length argument.


1. positional arguments: These are the arguments passed to function in correct positional order.

            The number of arguments and position of arguments must be matched. If we change the
                order then result may be changed.

            If we change the number of arguments then we will get error.

"""
# Example of positional argument :

def func(name,marks):
    print(f'Hii {name} you achieved {marks}% marks.')

func('anil',93)         # Hii anil you achieved 93% marks.
func(93,'anil')         # Hii 93 you achieved anil% marks. : changing the order of parameter, result will be changed.
# func('anil')                 # TypeError: func() missing 1 required positional argument: 'marks'
# func('anil',93,'good')       # TypeError: func() takes 2 positional arguments but 3 were given



'''
2. keyword arguments: We can pass argument values by keyword i.e by parameter name.
                        Here the order of arguments is not important but number of arguments must be matched.

Note:    We can use both positional and keyword arguments simultaneously. But first we have to
          take positional arguments and then keyword arguments,otherwise we will get syntaxerror.                  

***** If we are giving many type of argument while calling a function, If is necessary to give first priority 
        to all positional argument.
'''
# Example of keyword argument :
def func1(name,msg):
    print(f"Hii {name} : {msg}")

func1(name='anil',msg='How are you ?')            # Hii anil : How are you ?
func1(msg='How are you ?',name='anil')            # Hii anil : How are you ?
func1('anil',msg='How are you ?')                 # Hii anil : How are you ?
# func1(name='anil','Hii anil : How are you ?')   # SyntaxError: positional argument follows keyword argument.



'''
3. Default Arguments: Sometimes we can provide default values for our positional arguments.
                    If we are not passing any name then only default value will be considered.
                    After default arguments we should not take non default arguments.
                    ***Default argument will be declared at the end of all arguments.
'''
# Ex. 1 :
def wish(name,msg="It is your b'day today"):
    print(f'Hello {name} : {msg}')

# wish()              # TypeError: wish() missing 1 required positional argument: 'name'
wish('manoj','what are you doing ?')                            # Hello manoj : what are you doing ?
wish(name='manish',msg='where are you currently working ?')     # Hello manish : where are you currently working ?
wish('anil')                # Hello anil : It is your b'day today

'''
 Ex. 2 :
def wish1(msg='great job!!!',name):
    pass
wish(name='anil')           # SyntaxError: non-default argument follows default argument
'''



'''
4. Variable length arguments : Sometimes we can pass variable number of arguments to our function,such type of
                                arguments are called variable length arguments.

We can declare a variable length argument with * symbol.                               
Ex :      def f1(*n):                             
                                
We can call this function by passing any number of arguments including zero number.
Internally all these values represented in the form of *tuple*.                              
''' 
# Ex 1.
def sum(*n):
    total = 0
    # print(type(n))              # <class 'tuple'>
    for i in n:
        total =total+i
    print('The sum of given numbers is : ',total)
sum()                 # The sum of given numbers is :  0
sum(12,34,46)         # The sum of given numbers is :  92
sum(10,306,50,29)     # The sum of given numbers is :  395


# Ex. 2
# We can mix variable length arguments with positional arguments.
def f2(n1,*s):
    print("positional argumemnt : ",n1)
    print("variable length argument : ",s)

# f2()        # TypeError: f2() missing 1 required positional argument: 'n1'
f2(2,3,4,5,6)     # first argument is treated as positional and rest are treated as var args(variable length arguments)
'''
output : 
positional argumemnt :  2
variable length argument :  (3, 4, 5, 6)
'''


# Ex 3.
'''
Note: After variable length argument,if we are taking any other arguments then we
should provide values as keyword arguments.'''

def f3(*s,n2):
    print("positional argumemnt : ",n2)
    print("variable length argument : ",s)

# f3(1,2,3,4,35,4)            # TypeError: f3() missing 1 required keyword-only argument: 'n2'
f3(43,423,4,n2='anil')        # keyword argument always comes after posotional argument.
'''
Output : 
positional argumemnt :  anil
variable length argument :  (43, 423, 4)'''

#-----------------------------------------------------------------------------------------------------------

'''
NOTE : We can declare key word variable length arguments also.
        For this we have to use **.

   We can call this function by passing any number of keyword arguments. Internally these
keyword arguments will be stored inside a dictionary.     
'''

def f5(**kwargs):
    print(type(kwargs))
    print(kwargs)

    for k,v in kwargs.items():
        print(f'{k} : {v}')

f5(name='anil',course='MCA',Rank=102)
'''
OUTPUT :
<class 'dict'>
{'name': 'anil', 'course': 'MCA', 'Rank': 102}
name : anil
course : MCA
Rank : 102
'''
#-----------------------------------------------------------------------------------------------------------
'''


some practice questions :

def f(arg1,arg2,arg3=4,arg4=8):
        print(arg1,arg2,arg3,arg4)

1. f(3,2)                ==> 3 2 4 8

2. f(10,20,30,40)        ===>10 20 30 40

3. f(25,50,arg4=100)     ==>25 50 4 100

4. f(arg4=2,arg1=3,arg2=4)===>3 4 4 2

5. f()===>Invalid
         TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'

 6. f(arg3=10,arg4=20,30,40) ==>Invalid
        SyntaxError: positional argument follows keyword argument
        [After keyword arguments we should not take positional arguments]

 7. f(4,5,arg2=6)==>Invalid
        TypeError: f() got multiple values for argument 'arg2'

 8. f(4,5,arg3=5,arg5=6)==>Invalid
        TypeError: f() got an unexpected keyword argument 'arg5'
 '''