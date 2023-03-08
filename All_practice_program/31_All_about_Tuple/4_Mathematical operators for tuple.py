
# we can apply Concatenation Operator(+) and multiplication operator (*) for tuple.

# 1. Concatenation Operator(+) :

t1 = (1,2,3,4)
t2 = (5,6,7,8)
t3 = t1+t2 
# t4 = t1 + 30            # TypeError: can only concatenate tuple (not "int") to tuple
t5 = t1 + (30,)

print(t3)           # (1, 2, 3, 4, 5, 6, 7, 8)
print(t5)           # (1, 2, 3, 4, 30)


# 2. Multiplication operator or repetition operator(*):

t6 = (10,20,30)
t7 = (1,3,5,6)

print(t6*3)         # (10, 20, 30, 10, 20, 30, 10, 20, 30)
# print(t6*t7)        # TypeError: can't multiply sequence by non-int of type 'tuple'
print(t7*2)         # (1, 3, 5, 6, 1, 3, 5, 6)
