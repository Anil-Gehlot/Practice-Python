'''

Setter and Getter Methods:

We can set and get the values of instance variables by using getter and setter methods.


Setter Method:

setter methods can be used to set values to the instance variables. setter methods also known as
mutator methods.

syntax:
def setVariable(self,variable):
 self.variable=variable

 Example:
def setName(self,name):
 self.name=name

 
 
Getter Method:

Getter methods can be used to get values of the instance variables. Getter methods also known as
accessor methods.

syntax:
def getVariable(self):
 return self.variable

Example:
def getName(self):
 return self.name
'''

class Student:

    # setter and getter within the class.
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks =marks
    def getMarks(self):
        return self.marks 

n = int(input("Enter number of Student: "))
for i in range(n):
    name = input("Enter student Name: ")
    marks = int(input("Enter Marks: "))

    s = Student()
    s.setName(name)
    s.setMarks(marks)

    print("Hii ",s.getName())
    print("Your marks are: ",s.getMarks())
    print()



s = Student()

# setter and getter from outside the class.
s.setName('anil')
print(s.getName())

print(s.__dict__)   #{'name': 'anil'}

'''
** We have to make setter and getter method for each variable if we 
want to create(instance variable)

Biggest advantage of setter and getter method is SECURITY..
Biggest problem is lengthy code.


'''
