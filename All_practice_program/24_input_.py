
"""
Therer are two types of input function :
        1. input(): it always takes input in string form.
        2. eval() : it convert given input according to datatype.It can also solve any given expression.



    split() :The split() method splits a string into a list.it is only applicable for string value.
   You can specify the separator, default separator is any whitespace.

   
"""

# To take multiple user input in one line with seperation with space.
a,b = [int(i) for i in input("enter two no.").split()]
print(a,b)

# read 4 float values from the key-board which are specified with ',' seperation and print sum.
w,x,y,z = [int(i) for i in input("enter four no.").split(',')]
print("sum : ",w+x+y+z)


x=eval('1+33-8.5')    # eval can solve the expression
print(x)
print()

p = eval(input("enter you choice : ")) # the output will be converted according to it's datatye.
print(type(p))

# reading different datatype (int,float,bool,complex..) value in one line seperated with comma .
a,b,c = [eval(x) for x in input('Enter 3 values : ').split(',')]
print(type(a))
print(type(b))
print(type(c))


 # reading different datatype (int,float,bool,complex..) value in one line seperated with 5 .
s, t, u = [eval(x) for x in input("enter 3 no. : ").split('5')]
print(s,type(s))
print(t,type(t))
print(u,type(u))
