
# Program to track the number of objects created for a class:

class Sample:
    count = 0
    def __init__(self):
        Sample.count = Sample.count +1
    @classmethod
    def TotalCount(cls):
        print("Total number of object: ",cls.count)

t1 = Sample()
t1 = Sample()
t1 = Sample()
t1 = Sample()
Sample.TotalCount()     #4
t1 = Sample()
t1 = Sample()
t1 = Sample()
Sample.TotalCount()     #7
