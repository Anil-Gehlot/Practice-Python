'''

It is an encapsulation mechanism to group related modules into a single unit

package is nothing but folder or directory which represents collection of Python modules.

Any folder or directory contains __init__.py file,is considered as a Python package.This file
can be empty.("in python 2", Not applicable in python 3)

A package can contains sub packages also.




The main advantages of package statement are :

1. We can resolve naming conflicts
2. We can identify our components uniquely
3. It improves modularity of the application



modules = A collection of variables, functions and classes is known as module.

package = A collection of modules is known as package.

library = A collection of packages is known as library.

'''


from package1.module1 import *
from package1.module2 import *
from package1.subpack.moduleA import *

f1()        # hii it is module1 from pack1
f2()        # hii it is module2 from pack1
f3()        # hii this is module A from subpackage

