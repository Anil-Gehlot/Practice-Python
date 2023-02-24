"""
Bytearray DataTypes : 
                This datatype are also used to represent a group of byte numbers, just like an array.
                    
                Note that : 1. Every value in bytes datatype should be in range between (0-256).
                            2. bytearray datatype is mutable. """


#b1 = -1,10,29,255        # ValueError: bytes must be in range(0, 256)
#b2= [10,20,566]          # ValueError: bytes must be in range(0, 256)  

b = [0,10,20,45,67,90,255]
x= bytearray(b)

print(type(x))          # <class 'bytearray'>
print(x)                # it will print in bytearray form.

print(x[4])             # fetching value by indexing : 90
print(x[0:5])           # it will print in bytearray form.

#x[0] = 345              # ValueError: byte must be in range(0, 256)
x[0] = 123              # changing the 0th element value.

for j in x:              # we can use for loop for iterating in bytearray datatypes.
    print(j) 