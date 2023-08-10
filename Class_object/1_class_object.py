"""
OOps concept.

process does not matter, data matters

1. Class & Object. 
2. Data abstraction.
3. Polymorphism.
4. Inheritence.
5. Data Encapsulation.
6. Dynamic Binding

....Classs=== basically ek real world entity ko computer me map karne k liye (collection of real world entities is known as class) 

lets make a class of name student  , where attributes are:

name
course



"""

class Student:
    def __init__(self,name,course,subject):
        self.name=name
        self.course=course
        self.subject=subject

    def show(self):
        print("Name : ",self.name)
        print("Course : ",self.course)
        print("subject : ",self.subject)
    
s1=Student("Ram","BCA","ADA")
s1.show()
s2=Student("Aman","B.tech","CN")
s2.show()