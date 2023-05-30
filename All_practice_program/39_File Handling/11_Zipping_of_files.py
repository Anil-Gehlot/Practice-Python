'''

Zipping and Unzipping Files:

It is very common requirement to zip and unzip files.
The main advantages are:

1. To improve memory utilization
2. We can reduce transport time
3. We can improve performance.

To perform zip and unzip operations, Python contains one in-bulit module --> zipfile.
This module contains a class : ZipFile
'''

# To create Zip file:

'''
We have to create ZipFile class object with name of the zip file,mode and constant
ZIP_DEFLATED. This constant represents we are creating zip file.

f = ZipFile("files.zip","w","ZIP_DEFLATED")

Once we create ZipFile object,we can add files by using write() method.
f.write(filename).
'''

# Creating a zipfile.

from zipfile import *
f = ZipFile('newzip.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('abcd.txt')
f.write('abcde.txt')
f.close()
print('newzip file is succesfully created.')