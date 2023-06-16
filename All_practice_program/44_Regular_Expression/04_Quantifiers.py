

'''

We can use quantifiers to specify the number of occurrences to match.

a    :  Exactly one 'a'
a+   :  Atleast one 'a'
a*   :  Any number of a's including zero number
a?   :  Atmost one 'a' ie either zero number or one number
a{m} :  Exactly m number of a's
a{m,n} :     Minimum m number of a's and Maximum n number of a's

^x :   It will check whether target string starts with x or not
x$ :   It will check whether target string ends with x or not
'''


# Example 1:  Exactly one 'a'
import re
matcher = re.finditer('a', 'aabbababassb')
for i in matcher:
    print(i.start(), '................', i.group())
print()

'''
OUTPUT:

0 ................ a
1 ................ a
4 ................ a
6 ................ a
8 ................ a
'''


# Example 2:  Atleast one 'a'
matcher = re.finditer('a+', 'aabbabaabaaab')
for i in matcher:
    print(i.start(), '................', i.group())
print()
'''
OUTPUT:

0 ................ aa
4 ................ a
6 ................ aa
9 ................ aaa
'''


# Example 3:  Any number of a's including zero number.
matcher = re.finditer('a*', 'aabbabaabaaab')
for i in matcher:
    print(i.start(), '................', i.group())
print()

'''
OUTPUT:

0 ................ aa
2 ................
3 ................
4 ................ a
5 ................
6 ................ aa
8 ................
9 ................ aaa
12 ................
13 ................
'''


# Example 4:  Atmost one 'a' ie either zero number or one number

matcher = re.finditer('a?', 'aabbabaabaaab')
for i in matcher:
    print(i.start(), '................', i.group())
print()

'''
OUTPUT:

0 ................ a
1 ................ a
2 ................
3 ................
4 ................ a
5 ................
6 ................ a
7 ................ a
8 ................
9 ................ a
10 ................ a
11 ................ a
12 ................
13 ................
'''


# Example 5:   Exactly m number of a's
matcher = re.finditer('a{2}', 'aabbabaabaaab')
for i in matcher:
    print(i.start(), '................', i.group())
print()

'''
OUTPUT:

0 ................ aa
6 ................ aa
9 ................ aa
'''


# Example 6:  Minimum m number of a's and Maximum n number of a's
matcher = re.finditer('a{2,3}', 'aabbabaabaaab')
for i in matcher:
    print(i.start(), '................', i.group())
print('--')
'''
OUTPUT:

0 ................ aa
6 ................ aa
9 ................ aaa
'''

