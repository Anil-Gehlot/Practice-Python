'''

For the existing function we can give another name, which is nothing but function aliasing. 

In Python, aliasing means whenever one variable's value is assigned to another variable,
             because variables are just names that store references to values.

'''

def birthday(name):
    print(f"Happy birth day {name} ❤️❤️")

wish = birthday         # birthday is assigned to wish , now we can use both wish & birthday.
greet = wish

print(id(birthday))         # 2221838777888
print(id(wish))             # 2221838777888
print(id(greet))            # 2221838777888

birthday('Anil')            # Happy birth day Anil ❤️❤️
wish("Harsh")               # Happy birth day Harsh ❤️❤️
greet('Lokesh')             # Happy birth day Lokesh ❤️❤️
'''
Note: In the above example only one function is available but we can call that function by using
        either wish name or birthday name.
'''

# If we delete one name still we can access that function by using alias name

del birthday
del greet

birthday("Lokesh")          # NameError: name 'birthday' is not defined
greet("paritosh")             # NameError: name 'greet' is not defined
wish("Lokesh")                # Happy birth day Lokesh ❤️❤️

