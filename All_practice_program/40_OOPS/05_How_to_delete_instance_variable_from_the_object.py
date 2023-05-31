'''

1. Within a class we can delete instance variable as follows
    del self.variableName

2. From outside of class we can delete instance variables as follows
    del objectreference.variableName
'''
# Example 1:

class Test:
    def __init__(self):
        self.x = 5
        self.y = 6
        self.z = 7

        
    def m1(self):
        self.a = 8
        self.b = 9

        # deleting instance variable within the class.
        del self.z

t = Test()

# before calling the method
print(t.__dict__)       #{'x': 5, 'y': 6, 'z': 7}

# after calling the method
t.m1()
print(t.__dict__)       # {'x': 5, 'y': 6, 'a': 8, 'b': 9}
print("------------------------------------------------------------")


# Example 2 :  The instance variables which are deleted from one object,will not be deleted from other objects.

class Test1:
    def __init__(self):
        self.x = 5
        self.y = 6
        self.z = 7

    def m1(self):
        self.a = 8
        self.b = 9

t1 = Test1()
t2 = Test1()

# deleting instance variable from outside of the class for t1 object only.
del t1.z
print(t1.__dict__)      # {'x': 5, 'y': 6}

print(t2.__dict__)      # {'x': 5, 'y': 6, 'z': 7}

'''
If we change the values of instance variables of one object then those changes won't be reflected
to the remaining objects, because for every object we are separate copy of instance variables are
available.
'''
print("------------------------------------------------------------")


# Example 3:

class Test3:
    def __init__(self):
        self.x = 5
        self.y = 6
        self.z = 7

    def m1(self):
        self.a = 8
        self.b = 9

a1 = Test3()
a1.x = 123
a1.y = 456

a2 = Test3()

print(a1.__dict__)  # {'x': 123, 'y': 456, 'z': 7}

print(a2.__dict__)  # {'x': 5, 'y': 6, 'z': 7}