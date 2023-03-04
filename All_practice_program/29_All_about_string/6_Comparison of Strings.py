'''
We can use comparison operators (<,<=,>,>=) and equality operators(==,!=) for strings.
Comparison will be performed based on alphabetical order.'''

# program :
s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
if s1==s2:
    print("Both strings are equal")
elif s1>s2 :
    print("First string is greater.")
else:
    print("second string is greater.")

