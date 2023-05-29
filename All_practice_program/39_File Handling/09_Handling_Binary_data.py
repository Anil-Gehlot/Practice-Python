'''
Handling Binary Data:
It is very common requirement to read or write binary data like images,video files,audio
files etc.
'''

# Q. Program to read image file and write to a new image file?


f1=open("prabhas.png","rb")
f2=open("newpic.jpg","wb")
byte=f1.read()
f2.write(byte)
print("New Image is available with the name: newpic.jpg")