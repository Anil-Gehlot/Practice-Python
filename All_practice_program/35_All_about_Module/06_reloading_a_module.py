
'''
By default module will be loaded only once eventhough we are importing multiple multiple times.

for example we are importing "module1" multiple times but it is running only one time.

so suppose that we imported a module and after some time we modified that module, then what will 
happen : Will we get previous output or new output.



'''

# 1) Example 1.

import module1              # Hello !!  I'm Anil Gehlot.
import module1
import module1
import module1
import module1

"""
In the above program test module will be loaded only once eventhough we are importing 
multiple times.

The problem in this approach is after loading a module if it is updated outside then
updated version of module1 is not available to our program.

We can solve this problem by reloading module explicitly based on our requirement.

We can reload by using reload() function of imp module.
"""
##-------------------------------------------------------------------

# 2) Example 2.


import time
import module1
print("output before modifying the module......")

time.sleep(30)
import module1
print("output after modifying the module...")

'''
OUTPUT :

Hello !!  I'm Anil Gehlot.
output before modifying the module......
output after modifying the module...

In this program we imported a module and print, and then we wait for 30 second ...
In this period of time we changed something in module, But still it didn't give output
as modified....
even it is (module) running only one time.
'''
#-------------------------------------------------------------------

# 3) Example 3 : Program for module reloading.

'''
To reload the modified module, we have to use 
imp module & reload function 
'''

import time
from imp import reload

print("output before modifying the module......")
import module1
print()

print("output after modifying the module...")
time.sleep(30)
reload(module1)
print()

print("again modifying the module...")
time.sleep(30)
reload(module1)

'''
OUTPUT :

output before modifying the module......
Hello !!  I'm Anil Gehlot.

output after modifying the module...
Hello !!  I'm Anil Gehlot.Big fan of Prabhas anna.

again modifying the module...
Hello !!  I'm Anil Gehlot.Big fan of Prabhas anna.🙏🙏🙏

****Note: In the above program, everytime updated version of module1 will be available to our program.

'''
#---------------------------------------------------------------------------------------------------------

import module1
from imp import reload
reload(module1)
reload(module1)
reload(module1)

'''
OUTPUT :

Hello !!  I'm Anil Gehlot.
Hello !!  I'm Anil Gehlot.
Hello !!  I'm Anil Gehlot.
Hello !!  I'm Anil Gehlot.

** After reload the the module will be executed each time.
'''
#---------------------------------------------------------------------------------------------------------
"""
The main advantage of explicit module reloading is we can ensure that updated version is
always available to our program.

"""
