'''
replace() method is used to replace every occurrence of oldstring with new string.
SYNTAX : str.replace(oldstring,newstring)
'''
str="Learning Python is very difficult"
s1 = str.replace('Python','java')
print(s1)           # Learning java is very difficult.
print()

a="ababababababab"
a1=a.replace("a","b")
print(a1)               # bbbbbbbbbbbbbb


'''
Q. String objects are immutable then how we can change the content by
using replace() method.

ANS : Once we creates string object, we cannot change the content.This non changeable behaviour is
nothing but immutability. If we are trying to change the content by using any method, then with
those changes a new object will be created and changes won't be happend in existing object.

Hence with replace() method also a new object got created but existing object won't be changed.
'''
p="abab"
p1=p.replace("a","b")
print(p,"is available at :",id(p))      # 2238717048176
print(p1,"is available at :",id(p1))        # 2238717344432

'''
In the above example, original object is available and we can see new object which was created
because of replace() method.
'''
