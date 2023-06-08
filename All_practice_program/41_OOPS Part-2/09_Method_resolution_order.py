
'''
Method Resolution Order (MRO):


In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
This algorithm is also known as C3 algorithm.
Samuele Pedroni proposed this algorithm.

It follows DLR (Depth First Left to Right)
i.e Child will get more priority than Parent.
Left Parent will get more priority than Right Parent

MRO(X)=X+Merge(MRO(P1),MRO(P2),...,ParentList)



Head Element vs Tail Terminology:

Assume C1,C2,C3,...are classes.
In the list : C1C2C3C4C5....
C1 is considered as Head Element and remaining is considered as Tail.



How to find Merge:

Take the head of first list
If the head is not in the tail part of any other list,then add this head to the result and remove it
from the lists in the merge.
If the head is present in the tail part of any other list,then consider the head element of the next
list and continue the same process.


'''

# Note: We can find MRO of any class by using mro() function.
# Syntax:   print(ClassName.mro())
class A:pass
class B:pass
class C:pass
class D(A, B):pass
class E(B, C):pass
class F(D, E):pass

print(A.mro())                  # [<class '__main__.A'>, <class 'object'>]
print(B.mro())                  # [<class '__main__.B'>, <class 'object'>]
print(C.mro())                  # [<class '__main__.C'>, <class 'object'>]
print(D.mro())                  # [<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(E.mro())                  # [<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
print(F.mro())                  # [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
print("-----------------------------------------------------------------------------------------------")



class D:pass
class E:pass
class F:pass

class B(D,E):pass
class C(D,F):pass
class A(B,C):pass

print(A.mro())          # [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
print(B.mro())          # [<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]
print(C.mro())          # [<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]
print(D.mro())          # [<class '__main__.D'>, <class 'object'>]
print(E.mro())          # [<class '__main__.E'>, <class 'object'>]
print(F.mro())          # [<class '__main__.F'>, <class 'object'>]

print("-----------------------------------------------------------------------------------------------")



# Final example

class A:
    # def m1(self):
    #     print('A class method.')

    pass

class B:
    # def m1(self):
    #     print('B class method.')

    pass

class C:
    # def m1(self):
    #     print('C class method.')

    pass

class Z:
    def m1(self):
        print('Z class method.')

class X(A, B):
    # def m1(self):
    #     print('X class method.')

    pass

class Y(B, C):
    # def m1(self):
    #     print('Y class method.')

    pass

class P(X, Y, Z):
    pass

print(P.mro())          # [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Z'>, <class 'object'>]

p = P()
p.m1()



''''
OUTPUT:

P class method.

if we delete m1 method in P class and pass that method.
op ==> X class method.

if we delete m1 method in X class and pass that method.
op ==> A class method.

if we delete m1 method in A class and pass that method.
op ==> Y class method.

if we delete m1 method in Y class and pass that method.
op ==> B class method.

if we delete m1 method in B class and pass that method.
op ==> C class method.

if we delete m1 method in C class and pass that method.
op ==> Z class method.

if we delete m1 method in Z class and pass that method.
op ==> object class method.

same as for all..........
'''