'''
We can use else block with try-except-finally blocks.
else block will be executed if and only if there are no exceptions inside try block.


try:
    Risky Code
except:
    will be executed if exception inside try
else:
    will be executed if there is no exception inside try
finally:
    will be executed whether exception raised or not raised and handled or not handled
'''

try:
    print('try')
    print(10/0)
except:
    print('exept')
else:
    print('else')
finally:
    print('finally')

'''
If we are not commenting line-18 then else block won't be executed because there is exception
inside try block. In this case output is:

try
except
finally

If we comment line-18 then else block will be executed becausez there is no exception inside try.
In this case the output is:

try
else
finally
'''
