'''
We can apply the following mathematical operators for Strings.

1. + operator for concatenation
2. * operator for repetition 

1. To use + operator for Strings, compulsory both arguments should be str type.
2. To use * operator for Strings, compulsory one argument should be str and other argument should be int.

'''


a = 'anil'
b = 'gehlot'
c = 2

print(a+b)            # anilgehlot
# print( a + c)        # TypeError: can only concatenate str (not "int") to str.

print(a*2)            # anilanil
# print(a*b)            # TypeError: can't multiply sequence by non-int of type 'str'
