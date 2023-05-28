'''
Q.  Write a Python program to create a log file and write WARNING and higher
    level messages?


'''

import logging

logging.basicConfig(filename='log1.txt',level=logging.WARNING)

print("Implementation of loggging Module")

logging.debug("This is debug message")
logging.info("This is Info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

'''
OUTPUT: 
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
'''

# if we will not define the level by default, it will be considered as WARNING and its highe level.

logging.basicConfig(filename='log1.txt')

print("Implementation of loggging Module")

logging.debug("This is debug message")
logging.info("This is Info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

'''
OUTPUT: 
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
'''
