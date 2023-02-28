"""
Flow Control :

Flow control describes the order in which statements will be executed at runtime

There are 3 types of control flow :

1) Conditional statements.
    i)   if 
    ii)  if-elif 
    iii) if-elif-else

2) Iterative Statements.
    i) for loop
    ii) while loop

3) Transfer Statements.
    i)   break
    ii)  continue
    iii) pass

    i) break : We can use break statement inside loops to break loop execution based on some
                condition.
    ii)  continue : We can use continue statement to skip current iteration and continue next iteration.

    iii) pass : pass is a keyword in Python.

            In our programming syntactically if block is required which won't do anything then we can
            define that empty block with pass keyword.

         
            pass It is an empty statement.
            pass It is null statement.
            pass It won't do anything.

"""
# Example 1. for "break" statement.
for i in range(10):
    if  i==7:
        print("processing is enough....plz break.")
        break
    else:
        print("processing....")
print()

# Example 2 . for "break" statement.
cart = [10,20,444,506,4466,78,45]
for item in cart:
    if item>500:
        print("Sorry we can't process this order : ",item)
        break
    print("Processing item :",item)
print()

# Example 3. for "continue" statement.
for i in range(10):
    if i%2==0:
        continue
    print(i)
print()

# Example 4. for "continue" statement.
cart = [10,20,444,506,4466,78,45]
for item in cart:
    if item>500:
        print("Sorry we can't process this order : ",item)
        continue
    print("Processing item :",item)
print()


# Example 5. for "continue" statement.
num = [10,20,30,0,40,5,50]
for i in num:
    if i==0:
        print("can not devide by zero.")
        continue
    print(f"100 / {i} : ",100/i)
print()

# Example 6. for "pass" statement.

for i in range(100):
    if i%10==0:
        pass
    else:
        print(i) 

"""Sometimes in the parent class we have to declare a function with empty body and child
class responsible to provide proper implementation. Such type of empty body we can
define by using pass keyword. (It is something like abstract method in java)"""
# Example 

def m1(): 
    pass

