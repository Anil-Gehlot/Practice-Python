'''
We can use os library to get information about files in our computer.

os module has path sub module,which contains exists() function to check whether a
particular file exists or not?

SYNTAX: os.path.exists(fname)

***sys.exit(0) ===>To exit system without executing rest of the program.
'''

'''
Q. Write a program to check whether the given file exists or not. If it is
available then print its content?
'''
import os, sys

if os.path.exists('abc.txt'):
    f=open('abc.txt','r')
    print(f.read())
    f.close()
else:
    print('This file does not exist')
    sys.exit(0)


if os.path.exists('anil.txt'):
    f=open('anil.txt','r')
    print(f.read())
    f.close()
else:
    print('This file does not exist.')
    sys.exit(0)

'''
OUTPUT:

I am a good boy with good attiquetes.
This file does not exist.
'''