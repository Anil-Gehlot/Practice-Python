
'''
^ symbol:
We can use ^ symbol to check whether the given target string starts with our provided pattern or not.

if the target string starts with given string, then it will return Match object,otherwise returns None.
'''

import re
s="Learning Python is Very Easy"
sym = re.search('^Learn', s)
sym1 = re.search("^earn",s)

if sym != None:
    print("Target String starts with Learn")
else:
    print("Target String not starts with Learn")


if sym1 != None:
    print("Target String starts with earn")
else:
    print("Target String not starts with earn")

'''
OUTPUT:

Target String starts with Learn
Target String not starts with earn
'''

#--------------------------------------------------------------------------------------------------------


'''
$ symbol:
We can use $ symbol to check whether the given target string ends with our provided pattern or not

If the target string ends with given string then it will return Match object,otherwise returns None.
'''
import re
s="Learning Python is Very Easy"
res=re.search("Easy$",s)
if res != None:
    print("Target String ends with Easy")
else:
    print("Target String Not ends with Easy") 

'''
OUTPUT:

Target String ends with Easy
'''


s="Learning Python is Very Easy"
res=re.search("easy$",s, re.IGNORECASE)
if res != None:
    print("Target String ends with Easy")
else:
    print("Target String Not ends with Easy") 

'''
OUTPUT:

output without re.IGNORECASE ==>>   Target String Not ends with Easy.
output with re.IGNORECASE ==>>      Target String ends with Easy
'''
