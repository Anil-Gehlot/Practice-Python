"""
Identity Operators : Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
        is : Returns True if both variables are the same object
        is not : Returns True if both variables are not the same object.

        Identity opearator always used for address comparison....
        if we want content comparison , we have to use "==" operator.
        "==" is not identity operator.
"""
a = 20
b = 20

print(id(a),id(b))  # Both are same : 1992598029136 1992598029136
print(a is b)       # True
print(a is not b)   # False
print(a == b)       # True
print()

x = 20
y = 30

print(x is y)       # False
print(x is not y)   # True
print()


"""then the problem is that why the both list are not showing same address even they are having same content ...
the answer is that .... same value's object are allotted same address(memory location) only for fundamental data type , Because they all are immutable......
AND  the list is not fundamental dataype and also it is mutable , so that is why same adrress can not be allocated to the list.
"""
list1 = [10,20,30]
list2 = [10,20,30]

print(id(list1),id(list2))  # Both are not same : 1559421728384 1559421662080
print(list1 is list2)       # False
print(list1 == list2)       # True : because content is same.

