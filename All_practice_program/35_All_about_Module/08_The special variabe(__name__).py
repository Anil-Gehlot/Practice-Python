
'''
For every Python program , a special variable __name__ will be added internally.
This variable stores information regarding whether the program is executed as an
individual program or as a module.

If the program executed as an individual program then the value of this variable is
__main__

If the program executed as a module from some other program then the value of this
variable is the name of module where it is defined.

Hence by using this __name__ variable we can identify whether the program executed
directly or as a module.
'''

x = 8 
y = 345

def f():
    if __name__ == '__main__':
        print("The program is executed without importing any module.")
    else:
        print("The program is executed with any imported module.")

f()             # The program is executed without importing any module.
