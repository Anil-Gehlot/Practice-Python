
'''
The __str__() method returns a human-readable, or informal, string representation of an object. 
This method is called by the built-in print(), str(), and format() functions. 
If you don’t define a __str__() method for a class, then the built-in object implementation calls the __repr__() method instead.


The __repr__() method returns a more information-rich, or official, string representation of an object. 
This method is called by the built-in repr() function. If possible, the string returned should be a valid Python expression that can be used to recreate the object. 
In all cases, the string should be informative and unambiguous.

In general, the __str__() string is intended for users and the __repr__() string is intended for developers.

'''


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f'Name: {self.name} & Roll no.: {self.roll}'
    
s1 = Student("Anil", 11)
s2 = Student("Lokesh", 43)


# Output without __str__()
print(s1)         #   <__main__.Student object at 0x000001D2AE380400>
print(s2)         #   <__main__.Student object at 0x000001D2AE3801F0>


# Output with __str__()
print(s1)        # Name: Anil & Roll no.: 11
print(s2)        # Name: Lokesh & Roll no.: 43
