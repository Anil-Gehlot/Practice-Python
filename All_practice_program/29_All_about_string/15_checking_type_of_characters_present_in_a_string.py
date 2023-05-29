'''
Python contains the following methods to check type of characters present in a string.

1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
3) isdigit(): Returns True if all characters are digits only( 0 to 9)
4) islower(): Returns True if all characters are lower case alphabet symbols
5) isupper(): Returns True if all characters are upper case aplhabet symbols
6) istitle(): Returns True if string is in title case
7) isspace(): Returns True if string contains only spaces

8) iscapitalize : iscapitalize doesn't exist.****
'''

a = 'Anil2303'
b = '23anil'
num = '345'
print(a.isalnum())          # True
print(num.isalnum())        # True
print(a.isalpha())          # False
print("anIl".isalpha())     # True

print(num.isdigit())        # True
print(a.isdigit())          # False

print(b.islower())          # True
print('Anil'.islower())     # False

print(b.isupper())          # False
print("ANIL".isupper())     # True

s ='Learning python is Easy'
t = 'Learning Python Is Easy'
print(s.istitle())      # False
print(t.istitle())      # True

p = ''
q = ' '
print(p.isspace())      # False
print(q.isspace())      # True
print()


# program :

s=input("Enter any character:")
if s.isalnum():
    print("Alpha Numeric Character")
    if s.isalpha():
        print("Alphabet character")
        if s.islower():
            print("Lower case alphabet character")
        else:
            print("Upper case alphabet character")
    else:
        print("it is a digit")
elif s.isspace():
    print("It is space character")
else: 
    print("Non Space Special Character") 
