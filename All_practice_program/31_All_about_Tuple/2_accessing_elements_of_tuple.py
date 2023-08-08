
# we can access either by index or by slice operater.

# 1. By using index :
t1 = (12,3,4,9,5,6,7,6,5,43,345,6,654,3) 

print(t1[0])        # 12          
print(t1[3])        # 9
print(t1[4])        # 5
print(t1[6])        # 7

print(t1[-1])       # 3
print(t1[-9])       # 6
print(t1[-14])      # 12

# print(t1[66])       # IndexError: tuple index out of range


# 2. By using slice operator :
t2 = (12,3,4,9,5,6,7,6,5,43,345,6,654,3)

print(t2[2:5])      # (4,9,5)
print(t2[5:2])      # () : because we have to use -1 as a stepper for backward direction.
print(t2[5:2:-1])   # (6, 5, 9)
print(t2[6:100])    # (7, 6, 5, 43, 345, 6, 654, 3)
print(t2[::2])      # (12, 4, 5, 7, 5, 345, 654)


