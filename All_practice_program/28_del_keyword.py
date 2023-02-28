"""
del is a keyword in Python.

    After using a variable, it is highly recommended to delete that variable if it is no longer
required,so that the corresponding object is eligible for Garbage Collection.
We can delete variable by using del keyword.

"""


x = 10
print(x)

"""After deleting a variable we cannot access that variable otherwise we will get NameError"""
#del x       
#print(x)       # NameError: name 'x' is not defined

"""Note:
We can delete variables which are pointing to immutable objects.But we cannot delete
the elements present inside immutable object."""
#s = 'anil'
#del s           # valid
#del s[1]        # TypeError: 'str' object doesn't support item deletion

"""
If multiple variable references pointing to the same object(& we delete among one variable by using 'del' keyword)
  than only variable will be deleted, not the object"""

p = "anil"
q = 'anil'
r = 'anil'

print(id(p),id(q),id(r))        # 1804549895536 1804549895536 1804549895536
del p
del id(p)
print(q)
print(r)


"""
Difference between del and None:

del : 
    In the case del, the variable will be removed and we cannot access that variable(unbind
operation)

## after deleting there will be no object & no variable.

FOR EXAMPLE:
1) s="anil"
2) del s
3) print(s) ==>NameError: name 's' is not defined. 


NOne :
     in the case of None assignment the variable won't be removed but the corresponding
object is eligible for Garbage Collection(re bind operation). Hence after assigning with
None value,we can access that variable.

FOR EXAMPLE:

in this case None is not pointing to any object but variable exist.If we want a variable but no objecct then use "None"
1) s="durga"
2) s=None
3) print(s) # None

"""