
# We can create a tuple by packing a group of variables.

a = 10
b = 20
c = 30
d = 40
t = a,b,c,d
print(t)         #(10, 20, 30, 40)
# Here a,b,c,d are packed into a tuple t. This is nothing but tuple packing.

'''
Tuple unpacking is the reverse process of tuple packing
We can unpack a tuple and assign its values to different variables.

Note: At the time of tuple unpacking the number of variables and number of values
should be same, otherwise we will get ValueError.

'''

t=(10,20,30,40)
a,b,c,d=t
print("a =",a,"b =",b,"c =",c,"d =",d)      # Output :a = 10 b = 20 c = 30 d = 40 

t=(10,20,30,40)
a,b,c=t         #ValueError: too many values to unpack (expected 3)
