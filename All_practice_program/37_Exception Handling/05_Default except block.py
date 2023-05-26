'''
We can use default except block to handle any type of exceptions.
In default except block generally we can print normal error messages.
'''


try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError:
    print("Can't Divide with Zero")
except :                            # default exeption block
    print("Default Except:Plz provide valid input only")


'''
***Note: If try with multiple except blocks available then default except block should be
last,otherwise we will get SyntaxError.
'''

print('--------------------------------------------------------------------')

try:
    print(10/0)
except:
    print('default Exeption')
except ZeroDivisionError:
    print('Zero Division Error')

# Output : SyntaxError: default 'except:' must be last.