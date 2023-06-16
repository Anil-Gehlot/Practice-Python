
'''
search():

We can use search() function to search the given pattern in the target string.
If the match is available then it returns the Match object which represents first occurrence of the
match.
If the match is not available then it returns None.
'''

import re
s = input("Enter pattern to check: ")
matcher = re.search(s, 'abaaaba')
if matcher != None:
    print('Match is availabel')
    print("First occurrence of matched index: ",matcher.start())
else:
    print('Match is not availabel.')

'''
OUTPUT:

Enter pattern to check: aab
Match is availabel
First occurrence of matched index:  3

Enter pattern to check: abba
Match is not availabel.

Enter pattern to check: ddf
Match is not availabel.

Enter pattern to check: aba
Match is availabel
First occurrence of matched index:  0
'''

#---------------------------------------------------------------------------------------------------


'''
findall():

To find all occurrences of the match.
This function returns a list object which contains all occurrences.
'''

import re
l1 = re.findall('[0-9]',"a7b9c5kz")
print(l1)
#   ['7', '9', '5']

l2 = re.findall('[a-zA-z]', 'dSdcS32@#@DSDWsffds')
print(l2)
#   ['d', 'S', 'd', 'c', 'S', 'D', 'S', 'D', 'W', 's', 'f', 'f', 'd', 's']

#---------------------------------------------------------------------------------------------------


'''
5. finditer():

Returns the iterator yielding a match object for each match.
On each match object we can call start(), end() and group() functions.
'''

import re
itr=re.finditer("[a-z]","a7b9c5k8z")
for m in itr:
    print(m.start(),"...",m.end(),"...",m.group()) 

'''
OUTPUT:

0 ... 1 ... a
2 ... 3 ... b
4 ... 5 ... c
6 ... 7 ... k
8 ... 9 ... z
'''

# Note: To know more about finditer(), refer program no. 01, 02, 03 and 04.