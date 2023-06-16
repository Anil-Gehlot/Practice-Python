
'''

1. match():

We can use match function to check the given pattern at beginning of target string.
If the match is available then we will get Match object, otherwise we will get None.
'''

import re 
s = input('Enter pattern to check: ')
matcher = re.match(s, 'abcabdefg')
if matcher != None:
    print('Yes!!... string pattern matched at the beginning')
    print('Start index :',matcher.start())
else:
    print('Match is not availabel at the beginning.')

'''
OUTPUT:

Enter pattern to check: abca
Yes!!... string pattern matched at the beginning
Start index : 0

Enter pattern to check: bca
Match is not availabel at the beginning.

Enter pattern to check: dsgkdjvb
Match is not availabel at the beginning.
'''

#-----------------------------------------------------------------------------------------






'''
2.  fullmatch():


We can use fullmatch() function to match a pattern to all of target string. i.e complete string
should be matched according to given pattern.
If complete string matched then this function returns Match object otherwise it returns None.
'''

import re 
s = input("Enter string to check Pattern match: ")
matcher = re.fullmatch(s, 'abababa')
if matcher !=None:
    print('Full string Matched....')
else:
    print("Full string not matched.....")


'''
OUTPUT:

Enter string to check Pattern match: abababa
Full string Matched....

Enter string to check Pattern match: ababa
Full string not matched.....

Enter string to check Pattern match: ddfsd
Full string not matched.....

'''