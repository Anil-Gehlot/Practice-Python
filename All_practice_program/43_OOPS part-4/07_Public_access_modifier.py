

'''

Public Access Modifier:

The members of a class that are declared public are easily accessible from any part of the program.
All data members and member functions of a class are public by default.

This access modifiers are define as usual as we define directly in our program such as variable, function etc.
Eg:     name = 'Anil'
'''


# Example 1:

class Teacher:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

t1=Teacher("Anil", 12500)
print(t1.name) # Anil                  # accessing public modifier.

# we can also modify the public modifiers.
t1.name = 'chhaya'
print(t1.name)  # chhaya