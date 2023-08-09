

'''

In Python we cannot specify the type explicitly. Based on provided value at runtime the type will
be considered automatically. Hence Python is considered as Dynamically Typed Programming
Language.


Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. 
where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.

The name Duck Typing comes from the phrase:
“If it looks like a duck and quacks like a duck, it’s a duck”


'''

# Demo Program.

class Duck:
    def talk(self):
        print("Quack...Quack..")

class Dog:
    def talk(self):
        print("Bhow...Bhow..")

class Cat:
    def talk(self):
        print("Meow...Meow..")

class Goat:
    def talk(self):
        print("Myanha...Myanha..")


def f1(obj):
    obj.talk()

l = [Duck(),Cat(),Dog(),Goat()]

for i in l:
    f1(i)
'''
OUTPUT:

Quack...Quack..
Meow...Meow..
Bhow...Bhow..
Myanha...Myanha..
'''

#  The problem in this approach is if obj does not contain talk() method then we will get AttributeError

class Donkey:
    def speak(self):
        print('dechuu...dechhuu..')

f1(Donkey())                    #  AttributeError: 'Donkey' object has no attribute 'talk'.




''''
But we can solve this problem by using hasattr() function.
 
hasattr(obj,'attributename')

attributename can be method name or variable name

'''

class Ducks:
    def talk(self):
        print('Quack.. Quack..')

class Humans:
    def talk(self):
        print('Hello Hi...')

class Dogs:
    def bark(self):
        print('Bow Bow..') 

def f2(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()


l1 = [ Dogs(), Ducks(), Humans()]

for i in l1:
    f2(i)
'''
OUTPUT:

Bow Bow..
Quack.. Quack..
Hello Hi...
'''
