'''
Various properties of File Object:

Once we opend a file and we got file object,we can get various details related to that file
by using its properties.


name      : Name of opened file
mode      : Mode in which the file is opened
closed    : Returns boolean value indicates that file is closed or not
readable(): Retruns boolean value indicates that whether file is readable or not
writable(): Returns boolean value indicates that whether file is writable or not
'''

f=open('abc.txt','w')

print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('Is File readable: ',f.readable())
print("Is File writabel: ",f.writable())
print('Is file is Closed: ',f.closed)
f.close()
print('Is file is Closed: ',f.closed)

'''
OUTPUT:

File Name:  abc.txt
File Mode:  w
Is File readable:  False  
Is File writabel:  True   
Is file is Closed:  False 
Is file is Closed:  True 
'''