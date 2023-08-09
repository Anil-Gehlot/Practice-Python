

'''

A Regular Expressions (RegEx) is a special sequence of characters that uses a search pattern to find a string or set of strings.
It can detect the presence or absence of a text by matching it with a particular pattern.

If we want to represent a group of Strings according to a particular format/pattern then we should go for Regular Expressions.
Regualr Expressions is a declarative mechanism to represent a group of Strings accroding to particular format/pattern

Eg 1: We can write a regular expression to represent all mobile numbers.
Eg 2: We can write a regular expression to represent all mail ids.

The main important application areas of Regular Expressions are : 

    1. To develop validation frameworks/validation logic
    2. To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
    3. To develop Translators like compilers, interpreters etc
    4. To develop digital circuits
    5. To develop communication protocols like TCP/IP, UDP etc.


We can develop Regular Expression Based applications by using python module: re
This module contains several inbuilt functions to use Regular Expressions very easily in our applications.






1. compile():
The compile() function is used to compile a pattern into a regular expression object.    
The pattern argument can be either a string or a regular expression object.

SYNTAX :    pattern = re.compile("ab")



2. finditer():
The finditer() function returns an iterator yielding MatchObject instances over all non-overlapping matches
Returns an Iterator object which yields Match object for every Match

SYNTAX :   matcher = pattern.finditer("abaababa")

    On Match object we can call the following methods.

    1. start() ==>>  Returns start index of the match
    2. end() ==>>  Returns end+1 index of the match
    3. group() ==>>  Returns the matched string
'''




# Example 1:
import re

count = 0
pattern = re.compile('ab')
matcher = pattern.finditer("abaababa")


for i in matcher:
    count = count + 1
    print("match is available at starting index: ",i.start())
    print("match is available till ending index:",i.end()-1)        # because it returns "end index +1"
    print('matched string is: ',i.group())
    print()
print('The number of Occurences: ',count)

"""
OUTPUT:

match is available at starting index:  0
match is available till ending index: 1
matched string is:  ab

match is available at starting index:  3
match is available till ending index: 4
matched string is:  ab

match is available at starting index:  5
match is available till ending index: 6
matched string is:  ab

The number of Occurences:  3
"""




# Example 2: we can also find mathced pattern without compile() function , directly with finditer() function.


import re 

matcher = re.finditer('ad','assfsddaadsadfdasasad')
count1 = 0
for m in matcher:
    count1 = count1 + 1
    print("match is available at starting index: ",m.start())
    print("match is available till ending index:",m.end()-1)        # because it returns "end index +1"
    print('matched string is: ',m.group())
    print()
print('The number of Occurences: ',count)

'''
OUTPUT:

match is available at starting index:  8
match is available till ending index: 9
matched string is:  ad

match is available at starting index:  11
match is available till ending index: 12
matched string is:  ad

match is available at starting index:  19
match is available till ending index: 20
matched string is:  ad

The number of Occurences:  3
'''
