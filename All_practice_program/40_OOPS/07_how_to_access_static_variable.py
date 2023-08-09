'''
How to access static variables:
#1. inside constructor: by using either self or classname
#2. inside instance method: by using either self or classname
#3. inside class method: by using either cls variable or classname
#4. inside static method: by using classname
#5. From outside of class: by using either object reference or classnmae

InShort (self, cls, object reference, class name(preferred))
'''

class Cars:
    p = 10
    def __init__(self):
        print(self.p)       #1
        print(Cars.p)       #1

    def a1(self):
        print(self.p)       #2
        print(Cars.p)       #2

    @classmethod
    def a2(cls):
        print(cls.p)        #3
        print(Cars.p)       #3

    @staticmethod
    def a3():
        print(Cars.p)       #4

c = Cars()
c.a1()      # CALLING INSTANCE METHOD
Cars.a2()   # calling class method
Cars.a3()   # calling static metohd

print(c.p)          #5
print(Cars.p)       #5

