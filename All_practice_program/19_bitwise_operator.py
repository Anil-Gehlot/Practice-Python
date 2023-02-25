"""
Bitwise operators are used to compare (binary) numbers:
This operator is only applicable on int and bool datatype.


Bitwise Operator :
    1. & (bitwise AND)          : if both bits are 1 then only 1 , otherwise 0.
    2. | (bitwise OR)           : if atleast one bit is 1 then 1 , otherwise 0.
    3. ^ (XOR : exclusive or)   : if both bits are different then 1 , otherwise 0.
    4. ~ (NOT)                  : Inverts all the bits.
    
    5. << (bitwise left shift)  : Right hand side vacant cells will be filled with 0's.
    6. >> (bitwise right shift) : Left hand side vacant cells will be filled with sign bit.
    """
"""Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
8 = 0000000000001000
9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""


a = 6    # 0000000000000110 (binary)
b = 3    # 0000000000000011 (binary)

print(a & b )  # 2 = 0000000000000010

print(a | b)   # 7 = 0000000000000111

print(a ^ b)   # 5 = 0000000000000101

print(~a)       # -7 
print(~b)       # -4
print(~4)       # -5 
print(~True)    # -2

print(True<<2)  # 4
print(10<<2)    # 40

print(True>>2)  # 0
print(10>>2)    #2

