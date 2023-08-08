
# We can use + and * operators for List objects.

# 1. Concatenation operator(+): We can use + to concatenate 2 lists into a single list.

l1 = [1,2,3,4,5,6,6]
l2 = ['a','b','c','d','e']
l3 = l1 + l2
print(l3)       # [1, 2, 3, 4, 5, 6, 6, 'a', 'b', 'c', 'd', 'e']

# Note: To use + operator compulsory both arguments should be list objects,otherwise we will get TypeError.

# l4 = l1 + 40        # TypeError: can only concatenate list (not "int") to list
# l5 = l1 +'anil'     # TypeError: can only concatenate list (not "str") to list.
l6 = l1 +[40]
print(l6)             # [1, 2, 3, 4, 5, 6, 6, 40]


# 2. Repetition Operator(*): We can use repetition operator * to repeat elements of list specified number of times.

r1 = [2,4,6,8,9,7,5,3]
r2 = r1*2
print(r2)           # [2, 4, 6, 8, 9, 7, 5, 3, 2, 4, 6, 8, 9, 7, 5, 3]
# print(r1*r2)        # TypeError: can't multiply sequence by non-int of type 'list'
