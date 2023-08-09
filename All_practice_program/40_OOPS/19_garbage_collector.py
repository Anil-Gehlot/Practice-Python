'''
Garbage Collection:

In old languages like C++, programmer is responsible for both creation and destruction of objects.

Usually programmer taking very much care while creating object, but neglecting
destruction of useless objects. Because of his neglectance, total memory can be filled with useless
objects which creates memory problems and total application will be down with Out of memory
error.

But in Python, We have some assistant which is always running in the background to destroy
useless objects.Because this assistant the chance of failing Python program with memory
problems is very less. This assistant is nothing but Garbage Collector.


**Hence the main objective of Garbage Collector is to destroy useless objects.

**If an object does not have any reference variable then that object eligible for Garbage Collection.
'''

'''
How to enable and disable Garbage Collector in our program

By default Gargbage collector is enabled, but we can disable based on our requirement. In this
context we can use the following functions of gc module.

1. gc.isenabled():  Returns True if GC enabled.

2. gc.disable():    To disable GC explicitly

3. gc.enable():     To enable GC explicitly
'''


# Example:

import gc
print(gc.isenabled())       # True

gc.disable()
print(gc.isenabled())       # False

gc.enable()
print(gc.isenabled())       # True


