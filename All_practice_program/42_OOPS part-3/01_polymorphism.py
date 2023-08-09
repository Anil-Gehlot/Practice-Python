'''
Polymorphism:

Poly means many. Morphs means forms.
Polymorphism means 'Many Forms', In programming it refers to methods/ functions/ operators etc
with the same name that can be executed on many object or classes.

A single entity having many forms is known as Polymorphism.

'''

# Example 1: + operator acts as concatenation and arithmetic addition

print(10 + 20)                      # 30
print('anil' + 'gehlot')            # anilgehlot


# Example 2: * operator acts as multiplication and repetition operator

print(10 * 20)             # 200
print('anil' * 3)           # anilanilanil

# Example 3: len() returs number of characters fro string object , whereas it also returns number of object for tuples

s = 'hello ..!'
t = ('anil', 'harsh', 'lokesh')

print(len(s))           # 9
print(len(t))           # 3

# Example 4: function name is same but performing different tasks for both classes.

class P:
    def marry(self):
        print('Subba Laxmi')

class C(P):
    def marry(self):
        print('Katrina Saif')
print('---------------------------------------------------------------------------------------------------------------')



'''
Related to polymorphism the following 4 topics are important.

1. Duck Typing Philosophy of Python

2. Overloading
     1. Operator Overloading
     2. Method Overloading
     3. Constructor Overloading

3. Overriding
     1. Method overriding
     2. constructor overriding

'''
