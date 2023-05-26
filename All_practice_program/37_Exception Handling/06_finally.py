'''
finally block is used to Resource Deallocating Code or
Resource Releasing code or cleanup code.

1.  It is not recommended to maintain clean up code(Resource Deallocating Code or
Resource Releasing code) inside try block because there is no guarentee for the execution
of every statement inside try block always.

2. It is not recommended to maintain clean up code inside except block, because if there
is no exception then except block won't be executed. 

3. Hence we required some place to maintain clean up code which should be executed
always irrespective of whether exception raised or not raised and whether exception
handled or not handled. Such type of best place is nothing but finally block.

Hence the main purpose of finally block is to maintain clean up code

SYNTAX :

try:
    Risky Code
exept: 
    Handling Code
finally:
    Cleanup Code

**The speciality of finally block is it will be executed always whether exception raised or not
raised and whether exception handled or not handled.
'''

# Case 1 : If there is no exeption.

try:
    print('try')
except:
    print('exept')
finally:
    print('finally')

# Output:
#   try
#   finally
print("------------------------------------------------")

# Case 2 : If there is an exeption raised but handled.

try:
    print(10/0)
except ZeroDivisionError:
    print('exept')
finally:
    print('finally')

# Output:
#   exept
#   finally
print("------------------------------------------------")


# Case 3 : If there is an exception raised but not handled.

# try:
#     print(10/0)
# except ValueError:
#     print('exept')
# finally:
#     print('finally')

#  Output:
#   finally
#   ZeroDivisionError: division by zero(Abnormal Termination)
print("------------------------------------------------")

'''
*** Note: There is only one situation where finally block won't be executed i.e. whenever we statrted execution and system shutdowm . 

Whenever we are using os._exit(0) function then Python Virtual Machine itself will be
shutdown.In this particular case finally won't be executed.
'''

import os
try:
    print('try')
    os._exit(0)
except NameError:
    print('exept')
finally:
    print('finally')

# Output:
#   try

#   Note:  os._exit(0)
#    where 0 represents status code and it indicates normal termination


print("------------------------------------------------")



