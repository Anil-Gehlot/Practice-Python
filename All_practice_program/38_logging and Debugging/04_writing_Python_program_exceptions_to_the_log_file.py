'''
By using the following function we can write exceptions information to the log file.

**logging.exception(msg)**

'''


import logging
logging.basicConfig(filename='mylog.txt',level=0)

try:
    a = int(input('Enter first num: '))
    b = int(input('Enter second Num: '))
    print(a/b)
except ZeroDivisionError as msg:
    print("Can't divide by zero")
    logging.exception(msg)
except ValueError as msg:
    print("Please provide only integer value")
    logging.exception(msg)
logging.info('Execution completed')


'''
OUTPUT:

Enter first num: 12
Enter second Num: 2
6.0

Enter first num: 10
Enter second Num: 0
Can't divide by zero

Enter first num: ten
Please provide only integer value
'''

'''
mylog.txt:

INFO:root:Execution completed
ERROR:root:division by zero
Traceback (most recent call last):
  File "c:\Users\anilg\OneDrive\Desktop\practice-python\All_practice_program\38_logging and Debugging\04_writing_Python_program_exceptions_to_the_log_file.py", line 15, in <module>
    print(a/b)
ZeroDivisionError: division by zero
INFO:root:Execution completed
ERROR:root:invalid literal for int() with base 10: 'ten'
Traceback (most recent call last):
  File "c:\Users\anilg\OneDrive\Desktop\practice-python\All_practice_program\38_logging and Debugging\04_writing_Python_program_exceptions_to_the_log_file.py", line 13, in <module>
    a = int(input('Enter first num: '))
ValueError: invalid literal for int() with base 10: 'ten'
INFO:root:Execution completed
'''