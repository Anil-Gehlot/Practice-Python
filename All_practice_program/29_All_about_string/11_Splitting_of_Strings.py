'''
We can split the given string according to specified seperator by using split() method.
The default seperator is space. The return type of split() method is List.

There is 'rsplit()' method too, which works as same as 'split()' method.but it works in backward direction.
SYNTAX : l=str.split(seperator)
'''

a="hello I,m  anil gehlot."
l=a.split()
print(l)            # ['hello', 'I,m', 'anil', 'gehlot.']
print(a.split())    # ['hello', 'I,m', 'anil', 'gehlot.']
print()

s="23-10-1979"
l=s.split('-')
print(l)            # ['23', '10', '1979']
print()


'''
we can take atmost two arguments in split() method.
first argument for seperating values (seperater)
second argument will be a interger number , which means how many element do you wan'na seperate.
'''

p = 'hello,bro!!,how,are,you,,?' 
print(p.split(','))         # ['hello', 'bro!!', 'how', 'are', 'you', '', '?']
print(p.split(',',3))       # ['hello', 'bro!!', 'how', 'are,you,,?']
print(p.rsplit(',',3))      # ['hello,bro!!,how,are', 'you', '', '?'] : backward direction.
