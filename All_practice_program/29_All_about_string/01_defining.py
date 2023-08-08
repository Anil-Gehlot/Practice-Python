"""
The most commonly used object in any project and in any programming language is String only.
Hence we should aware complete information about String data type.


Q. What is String?
Any sequence of characters within either single quotes or double quotes is considered as a String.

Note: In most of other languges like C, C++,Java, a single character with in single quotes is treated
as char data type value. But in Python we are not having char data type.Hence it is treated as
String only.

Eg:
>>> ch='a'
>>> type(ch)
<class 'str'>
"""

# defining string :
a = 'anil'
b = "prabhas"

"""
How to define multi-line String literals:  We can define multi-line String literals by using triple single or double quotes.
"""
# defining multiline string :
c = """anil 
is a good 
boy."""

"""
We can also use triple quotes to use single quotes or double quotes as symbol inside String literal.

Eg:
s   =   'This is ' single quote symbol'  ==>invalid
s   =   'This is \' single quote symbol' ==>valid
s   =   "This is ' single quote symbol" ====>valid
s   =   'This is " double quotes symbol' ==>valid
s   =   'The "Python Notes" by 'durga' is very helpful' ==>invalid
s   =   "The "Python Notes" by 'durga' is very helpful" ==>invalid
s   =   'The \"Python Notes\" by \'durga\' is very helpful' ==>valid
s   =   '''The "Python Notes" by 'durga' is very helpful''' ==>valid
"""
