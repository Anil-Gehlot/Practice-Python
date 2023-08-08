'''
We can change case of a string by using the following 4 methods.

1. upper()===>To convert all characters to upper case.
2. lower() ===>To convert all characters to lower case.
3. swapcase()===>converts all lower case characters to upper case and all upper case characters to
lower case.
4. title() ===>To convert all character to title case. i.e first character in every word should be upper
case and all remaining characters should be in lower case.
5. capitalize() ==>Only first character will be converted to upper case and all remaining characters
can be converted to lower case
'''

str ='learning Python is VERY Easy .'

print(str.upper())      # LEARNING PYTHON IS VERY EASY .
print()
print(str.lower())      # learning python is very easy .
print()
print(str.swapcase())   # LEARNING pYTHON IS very eASY .
print()
print(str.title())      # Learning Python Is Very Easy .
print()
print(str.capitalize())     # Learning python is very easy .
print()
