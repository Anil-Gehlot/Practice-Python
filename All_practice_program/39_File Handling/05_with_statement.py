'''
The with statement can be used while opening a file. 
We can use this to group file operation statments within a block. 

The advantages of with statements is, it will take care closing of file, 
after completing all operation automatically, even in the case of exception also,
and we are not required to close explicitly.


'''

with open('new.txt','a') as f:
    f.write('Hello, I am learning Python.... \n')
    f.write('I am going to alomost finish it......')
    print("is file closed: ",f.closed)
print("is file closed: ",f.closed)

'''
OUTPUT:

is file closed:  False
is file closed:  True
'''