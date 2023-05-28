'''
Note:
In the above program only WARNING and higher level messages will be written to log file.
If we set level as DEBUG then all messages will be written to log file.
'''
import logging
logging.basicConfig(filename='log2.txt',level=logging.DEBUG)

print("Implementation of loggging Module")

logging.debug("This is debug message")
logging.info("This is Info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

'''
OUTPUT:
DEBUG:root:This is debug message
INFO:root:This is Info message
WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message


Note: We can format log messages to include date and time, ip address of the client etc
at advanced level.
'''