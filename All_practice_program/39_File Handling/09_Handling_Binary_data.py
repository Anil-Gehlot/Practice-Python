'''
Handling Binary Data:

It is very common requirement to read or write binary data like images,video files,audio
files etc.
'''
# Q. Program to read image file and write to a new image file?

f1=open('prabhas.png','rb')
f2=open('newp.jpg','wb')
byte = f1.read()
# print(byte)
f2.write(byte)
f1.close()
f2.close()


'''
**Note: 
    Same as we can perform operation for other binary files 
    like audio, video, etc.
'''