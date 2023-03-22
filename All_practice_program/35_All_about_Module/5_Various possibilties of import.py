
'''
Following are the various possibilties of import.

1) import modulname

2) import module1, module2, module3,......

3) import modulename as abcd

4) import module1 as m1,module2 as m2,module3 as m3

5) from module import membername

6) from module import member1,member2,memebr3

7) from module import memeber1 as x

8) from module import *



'''

"""
we can"t alias a module name while we wre importing particular members 
of that module, Beacuse there is no need of module name so why we are aliasing module name.
"""
from module as m import add         # SyntaxError: invalid syntax



'''
in the following example we are just aliasing random module and b is not defined.
'''
import module,random as m,r             # ModuleNotFoundError: No module named 'r'