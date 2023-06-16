

'''
Character classes:

We can use character classes to search a group of characters.


1. [abc]===>Either a or b or c

2. [^abc] ===>Except a and b and c

3. [a-z]==>Any Lower case alphabet symbol

4. [A-Z]===>Any upper case alphabet symbol

5. [a-zA-Z]==>Any alphabet symbol

6. [0-9] Any digit from 0 to 9

7. [a-zA-Z0-9]==>Any alphanumeric character

8. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)

'''



# Example 1:    [abc]===>Either a or b or c

import re 

matcher = re.finditer('[abc]', 'a7b@ck92b')
for i in matcher:
    print(i.start(), '.............', i.group())
print()
'''
OUTPUT:

0 ............. a
2 ............. b
4 ............. c
8 ............. b
'''


# Example 2:     [^abc] ===>Except a and b and c
matcher = re.finditer('[^abc]', 'a7b@ck92b')
for i in matcher:
    print(i.start(), '.............', i.group())
print()

"""
OUTPUT:

1 ............. 7
3 ............. @
5 ............. k
6 ............. 9
7 ............. 2
"""


# Example 3:    [a-z]==>Any Lower case alphabet symbol

matcher = re.finditer('[a-z]', 'a7b@ck92b') 
for i in matcher:
    print(i.start(), '................', i.group())
print()

'''
OUTPUT:
0 ................ a
2 ................ b
4 ................ c
5 ................ k
8 ................ b
'''


# Example 4:    [A-Z]===>Any upper case alphabet symbol.
matcher = re.finditer('[A-Z]', 'a7b@SAck92bHDS')
for i in matcher:
    print(i.start(), '..............', i.group())
print()

'''
OUTPUT:

4 .............. S
5 .............. A
11 .............. H
12 .............. D
13 .............. S
'''

# Example 5:  [a-zA-Z]==>Any alphabet symbol.

matcher = re.finditer('[a-zA-Z]', 'a7b@SAck92bHDS')
for i in matcher:
    print(i.start(), '..............', i.group())
print()

"""
OUTPUT:

0 .............. a
2 .............. b
4 .............. S
5 .............. A
6 .............. c
7 .............. k
10 .............. b
11 .............. H
12 .............. D
13 .............. S
"""


# Example 6:    [0-9] Any digit from 0 to 9

matcher = re.finditer('[0-9]','a7b@SAck92bHDS')
for i in matcher:
    print(i.start(), '.............',i.group())
print()

"""
OUTPUT:

1 ............. 7
8 ............. 9
9 ............. 2
"""

# Example 7:    [a-zA-Z0-9]==>Any alphanumeric character
matcher = re.finditer('[a-zA-z0-9]', 'a7b@SAck92bHDS')
for i in matcher:
    print(i.start(),'............', i.group())
print()

'''
OUTPUT:

0 ............ a
1 ............ 7
2 ............ b
4 ............ S
5 ............ A
6 ............ c
7 ............ k
8 ............ 9
9 ............ 2
10 ............ b
11 ............ H
12 ............ D
13 ............ S
'''


# Example 8:   [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)
matcher = re.finditer('[^a-zA-Z0-9]', 'a7b@S_Ack9-2bHDS')
for i in matcher:
    print(i.start(), '...............', i.group())
print()
'''
OUTPUT:

3 ............... @
5 ............... _
10 ............... -
'''