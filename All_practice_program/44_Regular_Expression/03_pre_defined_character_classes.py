


'''

\s :   Space character
\S :   Any character except space character
\d :   Any digit from 0 to 9
\D :   Any character except digit
\w :   Any word character [a-zA-Z0-9]
\W :   Any character except word character (Special Characters)
.  :   Any character including special characters

'''

# Example 1:  \s Space character
import re
matcher = re.finditer('\s', 'a7b k@9 z')
for i in matcher:
    print(i.start(), '...............', i.group())
print()

"""
OUTPUT:

3 ...............  
7 ...............
"""


# Example 2:  \S  Any character except space character
matcher = re.finditer('\S', 'a7b k@9 z')
for i in matcher:
    print(i.start(), '...............', i.group())
print()

'''
OUTPUT:

0 ............... a
1 ............... 7
2 ............... b
4 ............... k
5 ............... @
6 ............... 9
8 ............... z
'''



# Example 3:  \d  Any digit from 0 to 9

matcher = re.finditer('\d','a7b k@9 z')
for i in matcher:
    print(i.start(),'...................',i.group())
print()

'''
OUTPUT:

1 ................... 7
6 ................... 9
'''



# Example 4:  \D  Any character except digit

matcher = re.finditer('\D', 'a7b k@9 z')
for i in matcher:
    print(i.start(), '...............', i.group())
print()

'''
OUTPUT:

0 ............... a
2 ............... b
3 ...............
4 ............... k
5 ............... @
7 ...............
8 ............... z
'''


# Example 5:  \w  Any word character [a-zA-Z0-9]
matcher = re.finditer('\w', 'a7b k@9 z')
for i in matcher:
    print(i.start(), '.....................',i.group())
print()

'''
OUTPUT:

0 ..................... a
1 ..................... 7
2 ..................... b
4 ..................... k
6 ..................... 9
8 ..................... z
'''



# Example 6:  \W  Any character except word character (Special Characters)
matcher = re.finditer('\W', 'a7b k@9 z-')
for i in matcher:
    print(i.start(), '......................',i.group())
print()

'''
OUTPUT:

3 ......................
5 ...................... @
7 ......................
9 ...................... -
'''

# Example 7:  .   Any character including special characters
matcher = re.finditer('.', 'a7b k@9 z-')
for i in matcher:
    print(i.start(), '..........................', i.group())
print()

'''
OUTPUT:

0 .......................... a
1 .......................... 7
2 .......................... b
3 ..........................
4 .......................... k
5 .......................... @
6 .......................... 9
7 ..........................
8 .......................... z
9 .......................... -
'''
