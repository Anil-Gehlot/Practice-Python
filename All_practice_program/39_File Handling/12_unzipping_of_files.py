'''
To perform unzip operation:

We have to create ZipFile object as follows:

f = ZipFile("files.zip","r",ZIP_STORED)

ZIP_STORED represents unzip operation. This is default value and hence we are not
required to specify.

Once we created ZipFile object for unzip operation,we can get all file names present in
that zip file by using namelist() method.

names = f.namelist()
'''

from zipfile import *
f = ZipFile('newzip.zip','r',ZIP_STORED)
names=f.namelist()
for i in names:
    print('File Name is :',i)
    print('File content is: ')
    f1=open(i,'r')
    print(f1.read())
    print()
