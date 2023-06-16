

'''
split():

If we want to split the given target string according to a particular pattern then we should go for split() function.
This function returns list of all tokens.

By default space is not applicable as usual.
'''

import re
l1 = re.split(',', 'i, am, learning, python')

print(l1)           # ['i', ' am', ' learning', ' python']


# By default '.' is reserved to search for each character of given string.
# For spliting with '.' , we should use '\.'

l2 = re.split('\.', 'www.google.com')
print(l2)           # ['www', 'google', 'com']

