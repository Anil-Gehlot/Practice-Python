'''
it is the list the data will be internally saved to memory. in this case if memory requirement will be high so automatically performance will be down.

generator is a function, which is responsible to generate a sequence of values.
we can write generator function as simple function we define, But it uses 'yield' keyword to generate values.
If the body of a def contains yield, the function automatically becomes a generator function. 

in the generator concept nothing will be saved to the mameory,it generates value one by one.
if we want to huge amount of data the we should always go to generator..

Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

***Normal function contains only one Lreturn statement whereas generator function can contain one or more yield statement.
'''

# EX. 1
# gen is a generator function
def gen():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'    

g = gen()                       # g is a generator object


# Iterating over the generator object using next
print(next(g))                # a
print(next(g))                # b
print(next(g))                # c
print(next(g))                # d
# print(next(g))                #     StopIteration

print(type(g))                  # <class 'generator'>
print(type(gen()))              # <class 'generator'>

# accessing element by for loop
for i in g:
    print(i)                    # a b c d

# EX. 2

def count(num):
    while num>0:
        yield num
        num = num -1

final = count(6)
print(final)                # in this way we will always get generator object, not values : <generator object count at 0x0000015F46E75EE0>
for i in final:
    print(i)            # 6, 5, 4, 3, 2, 1
print()


# EX. 3 program to print the table of the given number using the generator.

def table(num):
    n = 1
    while n <=10:
        yield num*n
        n = n+1
result = table(5)
for i in result:
    print(i)

'''
5
10
15
20
25
30
35
40
45
50
'''

# EX. 4 to generate first n numbers.
def number(num):
    n = 1
    while n <=num:
        yield n
        n = n+1
result = number(8)
for i in result:
    print(i)
'''
1
2
3
4
5
6
7
8
'''

# EX. 5 To generate Fibonacci Numbers...

#  simple generator for Fibonacci Numbers
def fibo():

    # Initialize first two Fibonacci Numbers
    a , b = 0 , 1

     # One by one yield next Fibonacci Number
    while True:
        yield a
        a , b = b ,a+b

# Creating a generator object
result = fibo()

# Iterating over the generator object using for loop.
for i in range(10):
    print(next(result))    

"""
output :
0
1
1
2
3
5
8
13
21
34
"""      

for j in result:
    if j < 100:
        print(j)
    else:
        break
'''
output :
0
1
1
2
3
5
8
13
21
34
55
89
'''
# -------------------------------------------------------------------------------------------------------------------------------------------------

# Generators vs Normal Collections wrt Memory Utilization:

# Normal Collection:

l = [i*i for i in range(10000000000000000000000000000)]

print(type(l))              # <class 'list'>
print(l[0])
# We will get MemoryError in this case because all these values are required to store in the memory.


# Generators:

t = (i*i for i in range(10000000000000000000000))

print(type(t))              # <class 'generator'> : because no tuple comprehension in python.
print(next(g))

# Output: 0 :: We won't get any MemoryError because the values won't be stored at the beginning



'''
Advantages of Generator Functions:

1. when compared with class level iterators, generators are very easy to use
2. Improves memory utilization and performance.
3. Generators are best suitable for reading data from large number of large files
4. Generators work great for web scraping and crawling

'''
