try:
    print('statement 1')
    print('statement 2')
    print('statement 3')
except ZeroDivisionError:  # ZeroDivisionError or it can be any kind of error
    print('statement 4')

print('statement 5')

'''

case-1: 
    If there is no exception
    1,2,3,5  statements will be printed and Normal Termination

case-2:
    If an exception raised at stmt-2 and corresponding except block matched
    1,4,5 statements will be printed and Normal Termination  
    
case-3: 
    If an exception raised at stmt-2 and corresponding except block not matched
    1 statement will be printed only and Abnormal Termination  
    
case-4: 
    If an exception raised at stmt-4 (which is inside the exept block) 
    then it is always abnormal termination.  
  
    
Conclusions:

    1. within the try block if anywhere exception raised then rest of the try block wont be
        executed eventhough we handled that exception.

    2. If any statement which is not part of try block raises an exception then it is always
        abnormal termination.

    3. If there is no error in try block , then exept block will not be executed.
    '''