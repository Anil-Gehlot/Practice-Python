'''

How to delete static variables of a class:

We can delete static variables from anywhere by using the following syntax::
del classname.variablename::

But inside classmethod we can also use cls variable
del cls.variablename

'''

# Example 1:

class Test:
    a = 10 

    @classmethod
    def m1(cls):
        del cls.a
Test.m1()
print(Test.__dict__)
"""
OUTPUT: 
{'__module__': '__main__', 'm1': <classmethod(<function Test.m1 at 0x000001D53F285360>)>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
"""
print("-------------------------------------------------------------------------")

class Next:
    p = 1
    def __init__(self):
        del Next.p
        Next.q = 2
    def m1(self):
        del Next.q
        Next.r = 3
    @classmethod
    def m2(cls):
        del Next.r
        cls.s = 4
    @staticmethod
    def m3():
        del Next.s
        Next.t = 5
    
print(Next.__dict__)        # {'__module__': '__main__', 'p': 1, '__init__': <function Next.__init__ at 0x00000184941F52D0>, 'm1': <function Next.m1 at 0x00000184941F53F0>, 'm2': <classmethod(<function Next.m2 at 0x00000184941F5480>)>, 'm3': <staticmethod(<function Next.m3 at 0x00000184941F5510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None}

n = Next()
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x00000234338D52D0>, 'm1': <function Next.m1 at 0x00000234338D53F0>, 'm2': <classmethod(<function Next.m2 at 0x00000234338D5480>)>, 'm3': <staticmethod(<function Next.m3 at 0x00000234338D5510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 'q': 2}

n.m1()
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x0000021BFE8552D0>, 'm1': <function Next.m1 at 0x0000021BFE8553F0>, 'm2': <classmethod(<function Next.m2 at 0x0000021BFE855480>)>, 'm3': <staticmethod(<function Next.m3 at 0x0000021BFE855510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 'r': 3}

Next.m2()
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x000001CF9D9052D0>, 'm1': <function Next.m1 at 0x000001CF9D9053F0>, 'm2': <classmethod(<function Next.m2 at 0x000001CF9D905480>)>, 'm3': <staticmethod(<function Next.m3 at 0x000001CF9D905510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 's': 4}

Next.m3()
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x00000207242F52D0>, 'm1': <function Next.m1 at 0x00000207242F53F0>, 'm2': <classmethod(<function Next.m2 at 0x00000207242F5480>)>, 'm3': <staticmethod(<function Next.m3 at 0x00000207242F5510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 't': 5}

Next.u = 6
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x00000252CBFB52D0>, 'm1': <function Next.m1 at 0x00000252CBFB53F0>, 'm2': <classmethod(<function Next.m2 at 0x00000252CBFB5480>)>, 'm3': <staticmethod(<function Next.m3 at 0x00000252CBFB5510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 't': 5, 'u': 6}

del Next.t
print(Next.__dict__)        # {'__module__': '__main__', '__init__': <function Next.__init__ at 0x0000016F49CC52D0>, 'm1': <function Next.m1 at 0x0000016F49CC53F0>, 'm2': <classmethod(<function Next.m2 at 0x0000016F49CC5480>)>, 'm3': <staticmethod(<function Next.m3 at 0x0000016F49CC5510>)>, '__dict__': <attribute '__dict__' of 'Next' objects>, '__weakref__': <attribute '__weakref__' of 'Next' objects>, '__doc__': None, 'u': 6}
print("-------------------------------------------------------------------------")


### IF we try to delete by object reference, Than we will get Error:

class Don:
    o = 0

d = Don()
del d.o     
'''
OUTPUT:
line 74, in <module>
    del d.o
AttributeError: o
'''