
'''
6. sub():

sub means substitution or replacement.
In the target string every matched pattern will be replaced with provided replacement.

SYNTAX:     re.sub(regex,replacement,targetstring)
'''

import re
s1 = re.sub('[a-z]','#','a7b9c5k8z')
print(s1)
# OUTPUT:   #7#9#5#8#

s2 = re.sub('[0-9]','$','a7b9c5k8z')
print(s2)
# OUTPUT:   a$b$c$k$z

#-------------------------------------------------------------------------------------------------





'''
subn():

It is exactly same as sub except it can also returns the number of replacements.
This function returns a tuple where first element is result string and second element is number of
replacements.

SYNTAX:     (resultstring, number of replacements)
'''


import re
t = re.subn('[a-z]','#',"a7b9c5k8z")

print(t)
print("The Result String:",t[0])
print("The number of replacements:",t[1])

'''
OUTPUT:

('#7#9#5#8#', 5)
The Result String: #7#9#5#8#
The number of replacements: 5
'''