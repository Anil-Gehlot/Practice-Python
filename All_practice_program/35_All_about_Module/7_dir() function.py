
'''
Python provides inbuilt function dir() to list out all members of current module or a
specified module.

1) dir() ===>To list out all members of current module.
2) dir(moduleName)==>To list out all members of specified module.

*** Note: For every module at the time of execution Python interpreter will add some special
            properties automatically for internal use.
        Based on our requirement we can access these properties also in our program.
'''
import module
import math
a = 10
b = 20

def f1():
    print("Hello !!")

print(dir())                # # To print all members of current module
'''
OUTPUT :

['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__', 'a', 'b', 'f1']
'''


print(dir(module))
'''
OUTPUT :

['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
 '__spec__', 'add', 'div', 'product', 'sub', 'x', 'y']

'''

print(dir(math))
'''
OUTPUT :

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin',
 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 
 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 
 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 
 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter',
   'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 
   'tau', 'trunc', 'ulp']
'''
