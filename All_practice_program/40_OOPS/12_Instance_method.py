'''

1. Instance Methods:

Inside method implementation if we are using instance variables then such type of methods are
called instance methods.

Inside instance method declaration,we have to pass self variable.
 def m1(self):

 By using self variable inside method we can able to access instance variables.

**Within the class we can call instance method by using self variable and from outside of the class
we can call by using object reference.

'''


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Hii",self.name)
        print("Your marks are: ",self.marks)

    def grade(self):
        if self.marks>=60:
            print("You got A Grade.")
        elif self.marks>=50:
            print("You got B Grade")
        elif self.marks>=35:
            print('You got C Grade')
        else :
            print('You are Failed')

n = int(input('Enter number of student: '))
for i in range(n):
    name = input("Enter Name: ")
    marks= int(input("Enter Marks: "))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()
