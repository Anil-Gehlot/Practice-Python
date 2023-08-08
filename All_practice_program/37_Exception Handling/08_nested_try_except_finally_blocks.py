'''
We can take try-except-finally blocks inside try or except or finally blocks.i.e nesting of tryexcept-finally is possible.

try:
    ----------
    ----------
    ----------
    try:
        -------------
        --------------
        --------------
    except:
        --------------
        --------------
        --------------
        ------------
except:
    -----------
    -----------
    -----------

    General Risky code we have to take inside outer try block and too much risky code we have to take inside inner try block. 
    Inside Inner try block if an exception raised then innerexcept block is responsible to handle. If it is unable to handle
    then outer except block is responsible to handle.
'''


try:
    print("outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("outer except block")
finally:
    print("outer finally block") 


# Output :
# outer try block
# Inner try block
# Inner except block
# Inner finally block
# outer finally block
