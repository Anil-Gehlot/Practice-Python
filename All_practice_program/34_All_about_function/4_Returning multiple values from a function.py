'''
In other languages like C,C++ and Java, function can return atmost one value.

BUT in Python, a function can return any number of values in the form of 'tuple'.
'''

# Eg 1 : 
def calculator(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    return add, sub, mul, div           # return can take n number of arguments in tuple form.
t = calculator(8, 4)
print(type(t))      # <class 'tuple'>
print(t)            # (12, 4, 32, 2.0)

# Eg 2 :
def sum_sub(num3,num4):
    sum = num3 + num4
    sub = num3 - num4
    return sum, sub
x , y = sum_sub(45,78)

print('The addition of both numbers is : ',x)
print('The substraction of both numbers is ',y)

'''
Outoput :
        The addition of both numbers is :  123
        The substraction of both numbers is  -33
'''