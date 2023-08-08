"""
None Datatype: None means nothing or NO value associated. It is used to define null values."""


x = None

print(type(x))         # <class 'NoneType'>
print(x)                # None

def f1():
    a=10

c = f1()
print(type(c))       # <class 'NoneType'>   : Because the function is not returning value.
print(f1())          # it will print "None"

def f2():
    print("Jai Prabhas")

d = f2()
print(type(c))       # <class 'NoneType'>   : Because the function is not returning value.
print(f1())          # it will print "None"
