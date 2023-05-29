"""
File Handling:

As the part of programming requirement, we have to store our data permanenetly for future purpose.
For this requirement we should go for files.

Files are very common permanent storage areas to store our data. 

Types of Files:
There are 2 types of files.

1. Text Files:
Usually we can use text files to store character data.
eg: anil.txt


2. Binary files:
Usually we can use binary files to store binary data like images,video files, audio files etc...


very less value     : File concept
huge amount of data : Database concept
vary huge amount of data : Big Data
"""


'''
Opening a File:

Before performing any operation (like read or write) on the file,first we have to open that
file.For this we should use Python's inbuilt function open()

But at the time of open, we have to specify mode,which represents the purpose of
opening file....

f = open(filename, mode)

The allowed python modes are:

1. r:   ing of the file.If the specified file does not exist then we will get
        FileNotFoundError.This is default mode

2. w:   open an existing file for write operation. If the file already contains some data
        then it will be overridden. If the specified file is not already avaialble then this mode will
        create that file.

3. a:   open an existing file for append operation. It won't override existing data.If the
        specified file is not already avaialble then this mode will create a new file.

4. r+:   To read and write data into the file. The previous data in the file will not be
        deleted.The file pointer is placed at the beginning of the file.

5. w+:   To write and read data. It will override existing data.

6. a+:  To append and read data from the file.It wont override existing data.

7. x :  To open a file in exclusive creation mode for write operation. If the file already
        exists then we will get FileExistsError.

**Note: All the above modes are applicable for text files. If the above modes suffixed with
        'b' then these represents for binary files.

        Eg: rb, wb, xb, a, r+b, w+b, a+b.

'''


'''
Closing a File:

After completing our operations on the file,it is highly recommended to close the file.
For this we have to use close() function.

f.close()
'''



