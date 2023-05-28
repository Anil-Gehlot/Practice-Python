def square(x):
    return x**x

assert square(2)==4,'The square of 2 should be 4'
assert square(3)==9,'The square of 3 should be 9'
assert square(4)==16,'The square of 4 should be 16'

print(square(2))
print(square(3))
print(square(4))

'''
OUTPUT:
if we comment all 3 assert condition line, then output will be:
4
27
256

which is not right...
means we have done some mistake in code, so we will run it with assert condition.

Now output is :
Traceback (most recent call last):
  File "c:\Users\ anilg\OneDrive\Desktop\practice-python\All_practice_program\ 38_logging and Debugging\ 06_square_using_asseretion.py", line 5, in <module>
    assert square(3)==9,'The square of 3 should be 9'     
AssertionError: The square of 3 should be 9


while understanding assertion error improved code is below
'''



def square(x):
    return x*x

assert square(2)==4,'The square of 2 should be 4'
assert square(3)==9,'The square of 3 should be 9'
assert square(4)==16,'The square of 4 should be 16'

print(square(2))
print(square(3))
print(square(4))

'''
OUTPUT:
4
9
16
'''