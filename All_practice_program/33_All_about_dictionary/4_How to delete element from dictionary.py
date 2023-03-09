
# we are able to delete unneccessary key-value pair from our dictionary.

'''
1st way :   Syntax => del d[key]

            It deletes entry associated with the specified key.
             If the key is not available then we will get KeyError.
'''


dict = {'anil': 'MCA', 'manoj': 'b.com', 'manish': 'BCA', 'kapil': 'BBA', 'chetan': 'MBA'}

del dict['manish']
print(dict)             # {'anil': 'MCA', 'manoj': 'b.com', 'kapil': 'BBA', 'chetan': 'MBA'}

del dict["arjun"]       # KeyError: 'arjun'


'''
2nd Way : d.clear() ==>> To remove all the entries from the dictionary.
                        but dictionary will not be deleted.
'''

d1 = {'anil': 'MCA', 'manoj': 'b.com', 'manish': 'BCA', 'kapil': 'BBA', 'chetan': 'MBA'}
d1.clear()
print(d1)               # {}


'''
3rd Way :  del d ==>> To delete total dictionary.Now we cannot access d.
'''
d2 = {'anil': 'MCA', 'manoj': 'b.com', 'kapil': 'BBA', 'chetan': 'MBA'}

del d2
print(d2)           # NameError: name 'd2' is not defined.