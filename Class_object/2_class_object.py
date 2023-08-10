class Student:
    def __init__(self):
        self.name=input("Enter name : ")
        self.course=input("Enter course : ")
        self.subject=input("Enter subject : ")

    def show(self):
        print("Name : ",self.name)
        print("Course : ",self.course)
        print("subject : ",self.subject)
    
s1=Student()
s1.show()
s2=Student()
s2.show()
