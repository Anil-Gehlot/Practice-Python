x = 10
print(x)
#del x       # NameError: name 'x' is not defined
#print(x)

#s = 'anil'
#del s[1]        # TypeError: 'str' object doesn't support item deletion

"""
If multiple variable references pointing to the same object(& we delete among one variable by using 'del' keyword)  than only variable will be deleted, not the object"""
p = "anil"
q = 'anil'
r = 'anil'

print(id(p),id(q),id(r))        # 1804549895536 1804549895536 1804549895536
del p
del id(p)
print(q)
print(r)