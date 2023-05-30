'''
We can get statistics of a file like size, last accessed time,last modified time etc by using
stat() function of os module.

SYNTAX: stats = os.stat("abc.txt")


The statistics of a file includes the following parameters:

st_mode==>Protection Bits
st_ino==>Inode number
st_dev===>device
st_nlink===>no of hard links
st_uid===>userid of owner
st_gid==>group id of owner
st_size===>size of file in bytes
st_atime==>Time of most recent access
st_mtime==>Time of Most recent modification
st_ctime==> Time of Most recent meta data change


st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st
1970 ,12:00AM.  Bcoz according to 'Epoche Time Standard' computer standard time started on this date.

By using datetime module fromtimestamp() function,we can get exact
date and time.
'''

# Q. To print all statistics of file abcde.txt:

import os

staticstics = os.stat('abcde.txt')
print(staticstics)

'''
OUTPUT:

os.stat_result(
    st_mode=33206, 
    st_ino=14918173765898993, 
    st_dev=3894807656, 
    st_nlink=1, 
    st_uid=0, 
    st_gid=0, 
    st_size=48, 
    st_atime=1685348019, 
    st_mtime=1685254922, 
    st_ctime=1685254922)
    '''

# Q. To print specified properties:

import os

from datetime import *
st = os.stat('abc.txt')
print("File size in bytes: ",st.st_size)
print("File's last accessed time: ",datetime.fromtimestamp(st.st_atime))
print("File's last modified time: ",datetime.fromtimestamp(st.st_mtime))

'''
OUTPUT:

File size in bytes:  0
File's last accessed time:  2023-05-29 21:24:10.644132    
File's last modified time:  2023-05-29 21:24:10.644132    
'''