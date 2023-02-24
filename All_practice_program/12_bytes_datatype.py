"""
Bytes DataTypes : 
                This datatype are used to represent a group of byte numbers, just like an array.
                    
                Note that : 1. Every value in bytes datatype should be in range between (0-256).
                            2. bytes datatype is immutable. """


#b1 = -1,10,29,255        # ValueError: bytes must be in range(0, 256)
#b2= [10,20,566]          # ValueError: bytes must be in range(0, 256)  

b = [0,10,20,45,67,90,255]
x= bytes(b)

print(type(x))          # <class 'bytes'>
print(x)                # it will print in bytes form.

print(x[4])             # fetching value by indexing : 90
print(x[0:5])           # it will print in bytes form.

#x[0] = 123              # TypeError: 'bytes' object does not support item assignment (immutable : change nahi kiya ja sakta)

for j in x:              # we can use for loop for iterating in bytes datatypes.
    print(j) 