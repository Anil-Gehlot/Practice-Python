
'''

If try with multiple except blocks available then the order of these except blocks is
important .Python interpreter will always consider from top to bottom until matched
except block identified.

'''



try:
    x=int(input("Enter First Number: ")) 
    y=int(input("Enter Second Number: "))
    print(x/y) 
except ZeroDivisionError :
    print("Can't Divide with Zero")
except ValueError: 
    print("please provide int value only") 