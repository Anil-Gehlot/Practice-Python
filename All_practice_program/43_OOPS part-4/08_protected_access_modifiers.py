


'''


 Protected Access Modifier:

The data member of the class is declared protected by adding a single underscore “_” and this prevents it from being access. 
The protected members of the class can be accessed by other members within the class also it can be accessible to the class derived from it.

Eg:     _Name = "Prabhas"
'''


# Example:

class Student:

    def __init__(self, name, roll, branch):

        # protected  instance variable
        self._name = name
        self._roll = roll
        self._branch = branch

    # protected display method
    def _display(self):
        # accessing protected data members
        print("Name: ", self._name)
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


class School(Student):
    def __init__(self, name, roll, branch):
        # Student.__init__(self, name, roll, branch)            # we can also call parent class constructor by class name or super() method.
        super().__init__(name, roll, branch)

s = School("anil", 11, "MCA")
s._display()

'''
OUTPUT:

Name:  anil
Roll:  11
Branch:  MCA
'''
