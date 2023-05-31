'''

class: 
    Class represent a physical entity, It is like a blueprint or model of an object.
    By this blueprint  or model, we can create multiple object.
     
    It is like a container or blueprint or model.
    
    Properties can be represented by variables
     
    Actions can be represented by Methods.
    
    Hence class contains both variables and methods.      
      
Syntax:
class className:

        '' documenttation string ''
        variables:instance variables,static and local variables
        methods: instance methods,static methods,class methods

Documentation string represents description of the class. Within the class doc string is always
optional. We can get doc string by using the following 2 ways.

1. print(classname.__doc__)
2. help(classname)



What is Object:

Pysical existence of a class is nothing but object. We can create any number of objects for a class.

Syntax to create object: referencevariable = classname()
Eg:    s = Student()



What is Reference Variable:

The variable which can be used to refer object is called reference variable.
By using reference variable, we can access properties and methods of object.
'''



class Student:
    '''This is a class of student.'''

    # creating object related method
    def read(self):
        print( 'I am learning python.')

# printing documentstring(docstring)
print(Student.__doc__)
#or
help(Student)
    
# creating an object of Student class.
s = Student()

# calling a method.
s.read()

