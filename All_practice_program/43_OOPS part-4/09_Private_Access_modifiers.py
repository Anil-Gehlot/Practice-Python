

'''
Private Access Modifier:

A double underscore “__” makes the variable private as well as secure and the members of the class which is declared private are accessible within the class. 
Also, it is not possible to access them outside the class because it will throw an error.
private access modifier is the most secure access modifier.

Eg:     __name = "Raghav"


 Private members are not available for derived class also.

 we can not access private modifiers from outside of the class
'''


# Example:

class Student:

    def __init__(self, name, roll, branch):

        # protected  instance variable
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    # protected display method
    def __display(self):
        # accessing protected data members
        print("Name: ", self.__name)
        print("Roll: ", self.__roll)
        print("Branch: ", self.__branch)

    def dis(self):
        self.__display()

a = Student("anil", 11, "MCA")

# a.__display()                     # It will raise an error because we can not access private modifiers from outside of the class.

a.dis()

"""OUTPUT:

Name:  anil
Roll:  11
Branch:  MCA
"""









class School(Student):
    def __init__(self, name, roll, branch):
        # Student.__init__(self, name, roll, branch)            # we can also call parent class constructor by class name or super() method.
        super().__init__(name, roll, branch)

s = School("anil", 11, "MCA")
s.__display()

# Private members are not available for derived class also.
