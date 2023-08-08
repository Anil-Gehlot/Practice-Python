a=1244           # decimal number
b=0B110011       # binary number
c=0o7532         # octal number
d=0x94beeface    # hexa-decimal number

# bin() function is used to convert any type of number into the binary number.

print(bin(a))      # decimal to binary 
print(bin(c))      # octal to binary 
print(bin(d))      # hexa-decimal to binary
print("--------------------------------")

# oct() function is used to convert any type of number into the octal number.
print(oct(a))    # decimal to octal
print(oct(b))    # binary to octal
print(oct(d))    # hexa-decimal to octal
print("--------------------------------")


# hex() function is used to convert any type of number into the hexadecimal number.
print(hex(a))   # decimal to hexa-decimal 
print(hex(b))   # binary to hexa-decimal
print(hex(c))   # octal to hexa-decimal
print("--------------------------------")


# print() function by default is used to convert any type of number into the decimal number.

print(a)     # decimal number
print(b)     # binary to decimal
print(c)     # octal to decimal
print(d)     # hexa-decimal to decimal
print("--------------------------------")

