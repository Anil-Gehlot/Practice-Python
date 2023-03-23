
'''
This module defines several functions to generate random numbers.

We can use these functions while developing games,in cryptography and to generate
random numbers on fly for authentication.

The random module has a set of methods, which are used to generate random numbers.
'''

# 1) random() function.
# This function always generate some float value between 0 and 1 (0 & 1 are eclusive).

from random import *

for i in range(6):
    print(random())
'''
OUTPUT :

0.5630762549058403
0.32918921109420674
0.9430491432239361
0.6027437835678825
0.6255783898166387
0.31161829039917366

***random function takes no argument, if provided then Typeerror will be raised.

print(random(3))                 # TypeError: Random.random() takes no arguments (1 given)
'''
#----------------------------------------------------------------------------------------------

# 2) randint() function.     : It takes only 2 positional arguments.
# To generate random integer between two given numbers(both given number are imclusive)

from random import *

for i in range(6):
    print(randint(1,8))

"""
OUTPUT :
9
1
9
7
9
7
"""
#----------------------------------------------------------------------------------------------

# 3) uniform() function :
# This function returns random float values between 2 given numbers(both given numbers are exclusive)

from random import *

for i in range(7):
    print(uniform(2,6))

"""
OUTPUT :
5.200726440095821
5.971134574371382
2.818440123468554
5.0601821352946965
4.843955469551872
3.455333063931907
4.988184773110514
"""
#----------------------------------------------------------------------------------------------

# 4) randrange(start,stop,step)
"""
The randrange() method returns a randomly selected element from the specified range.

start argument is optional and default value is 0.
stop is required argument which shows ending positin.
step argument is optional and default value is 1.

randrange(10)    -->generates a number from 0 to 9
randrange(1,11)  -->generates a number from 1 to 10
randrange(1,11,2)-->generates a number from 1,3,5,7,9
"""

from random import *

for i in range(8):
    print(randrange(3,9))
'''
4
3
6
6
3
7
8
8
'''
print()
for i in range(8):
    print(randrange(9))
'''
3
2
6
6
0
1
2
5
'''
print()
for i in range(5):
    print(randrange(1,11,2))
'''
5
3
7
1
9
'''
#----------------------------------------------------------------------------------------------

# 5) choice() function.
'''
The choice() method returns a randomly selected element from the specified sequence.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
'''
import random

x = "WELCOME"

print(random.choice(x))         # L
print(random.choice(x))         # O
print(random.choice(x))         # M

list1 = [1,2,3,"anil","manish"]
print(random.choice(list1))         # anil
print(random.choice(list1))         # 2
print(random.choice(list1))         # manish
#----------------------------------------------------------------------------------------------

# 6) sample() function. 
"""
The sample() method returns a list with a randomly selection of a specified number of items from a sequnce.
"""

import random 

list1 = [1,2,3,"anil","manish"]

print(random.sample(list1,k=2))         # [3, 'manish']
print(random.sample(list1,k=3))         # ['manish', 2, 1]
print(random.sample(list1,k=4))         # [2, 1, 'manish', 'anil']

#----------------------------------------------------------------------------------------------
