'''
Logging is the process of creating a log file.
Such as ... log book of library in collage etc.

Definition: It is highly recommended to store complete application flow and exceptions information
            to a file. This process is called logging.

The main advantages of logging are:

1. we can use log files while performing debugging.
2. To keep record of the flow of application.
3. We can provide statistics like number of requests per day etc.

To implement logging, Python provides one inbuilt **module logging**
'''


"""
logging levels:
                Depending on type of information, logging data is divided according to the following 6
                levels in Python.

1. CRITICAL (50): Represent a very serious problem that needs high attention.
2. ERROR  (40)  : Represent a serious error.
3. WARNING (30) : Represent a warning message, some cautions needed. It is alert to the programmer.
4. INFO  (20)   : Represent a message with some important information.
5. DEBUG  (10)  : Represent a message with debugging information.
6. NOTSET  (0)  : Represent that the level is not set.

By default while executing Python program only *WARNING and higher level* messages will
be displayed.
"""

"""
How to implement logging:

To perform logging, first we required to create a file to store messages and we have to
specify which level messages we have to store.

We can do this by using 'basicConfig()' function of logging module.

logging.basicConfig(filename='log.txt',level=logging.WARNING)

The above line will create a file log.txt and we can store either WARNING level or higher
level messages to that file.

After creating log file, we can write messages to that file by using the following methods.

1. logging.debug(message)
2. logging,debug(message)
3. logging.warning(message)
4. logging.error(message)
5. logging.critical(message)

** Note: Always remember that Levels will be written in UPPERCASE & methods will be written 
        in lowercase.

        
This log files will be saved in current working directory.





















"""