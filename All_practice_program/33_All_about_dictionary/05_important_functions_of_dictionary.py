
# 1. dict() function : To create a dictionary.

d1 = dict() 
d2 = dict({100:"anil",200:"harsh"})
d4 = dict([(100,"harsh"),(200,"lokesh"),(300,"ravi")])

print(d1)           # {}
print(d2)           # {100: 'anil', 200: 'harsh'}
print(d4)           # {100: 'harsh', 200: 'lokesh', 300: 'ravi'}


# 2. len() : Returns the number of items in the dictionary.

d5 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'} 
print(len(d5))      # 3

# 3. clear(): To remove all elements from the dictionary.

d5 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'} 
d5.clear()
print(d5)               # {}


'''
4. get(): To get the value associated with the key.

d.get(key) : If the key is available then returns the corresponding value otherwise returns None.
            It wont raise any error.

d.get(key,defaultvalue) : If the key is available then returns the corresponding value otherwise returns default
                            value.
'''
d6 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}

print(d6[100])        # harsh
# print(d6[400])      # KeyError: 400

# if key doesn't found , it will not raise any error.
print(d6.get(100))      # harsh
print(d6.get(500))      # None : it doesn't raise any error.

# we can set default value too, if key doen't found.
print(d6.get(100))                      # harsh
print(d6.get(500,"key not found"))      # key not found


'''
5. pop():  It removes the entry associated with the specified key and returns the corresponding value.
             If the specified key is not available then we will get KeyError

            Syntax : d.pop(key)
'''
d6 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}

print(d6.pop(100))      # harsh
print(d6)               # {200: 'lokesh', 300: 'ravi'}

# print(d6.pop(500))      # KeyError: 500


'''
6. popitem() : It removes an arbitrary item(key-value) from the dictionaty and returns it.
                If the dictionary is empty then we will get KeyError.
'''
d7 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}

print(d7.popitem())         # (300, 'ravi')
print(d7)                   # {100: 'harsh', 200: 'lokesh'}

d8 = {}
# print(d8.popitem())         # KeyError: 'popitem(): dictionary is empty'


'''
7. keys() : It returns all keys associated eith dictionary
'''

d9 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}
a = d9.keys()
print(type(a))          # <class 'dict_keys'>
print(d9.keys())        # dict_keys([100, 200, 300])


'''
8. values() : It returns all values associated with the dictionary.
'''
d10 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}
b = d10.values()
print(type(b))          # <class 'dict_values'>
print(b)                # dict_values(['harsh', 'lokesh', 'ravi'])


'''
9. items() : It returns list of tuples representing key-value pairs.
'''
d11 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}

c = d11.items()
print(type(c))              # <class 'dict_items'>
print(d11.items())          # dict_items([(100, 'harsh'), (200, 'lokesh'), (300, 'ravi')])


'''
10. copy() : To create exactly duplicate dictionary(cloned copy)
'''
d12 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}
d13 = d12.copy()

print(id(d12))          # 1628196642752
print(id(d13))          # 1628196642688


'''
11. setdefault():
        If the key is already available then this function returns the corresponding value.
        If the key is not available then the specified key-value will be added as new item to the dictionary.
        
        Syntax : dict.setdefault(key,value)
'''
d14 = {100: 'harsh', 200: 'lokesh', 300: 'ravi'}

d14.setdefault(400,'Prabhas')
print(d14)              # {100: 'harsh', 200: 'lokesh', 300: 'ravi', 400: 'Prabhas'}

d14.setdefault(100,"Amrendra")
print(d14)              # {100: 'harsh', 200: 'lokesh', 300: 'ravi', 400: 'Prabhas'}

