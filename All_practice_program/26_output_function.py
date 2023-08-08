"""
Output function :
                We can use print() function to display output."""

'''
Form-1: 
        print() without any argument Just it prints new line character'''

print()    # It will just print a new line.


'''
Form-2:
        print() with string arguments.
        We can use escape characters also with string type.
        We can use repetetion operator (*) in the string.
        We can use + operator also.
        '''

print("Anil Gehlot")        # Anil Gehlot

print("Anil \nGehlot") 
print("Anil \tGehlot")      # Anil    Gehlot

print(3*"Anil")             # AnilAnilAnil
print("Anil"*4)             # AnilAnilAnilAnil

print("Hello"+"World")      # HelloWorld

'''
Note:
    1. If both arguments are String type then + operator acts as concatenation operator.
    2. If both arguments are number type then + operator acts as arithmetic addition operator.
    3. If one argument is string type and second is any other type like int then we will get Error.
    '''
print("Hello"+"World")      # HelloWorld : + will not add whitespace b/w both argument.
print("Hello","World")      #  Hello World : , will  add whitespace b/w both argument.
print(2+3)                  # 5


"""
Form - 3:
          print() with variable n number of arguments. """

a,b,c=10,20,30
print("The Values are :",a,b,c)     # The Values are : 10 20 30 

'''
sep attribute :
                By default output values are seperated by space.If we want we can specify seperator by
using "sep" attribute'''

x,y,z=10,20,30
print(x,y,z,sep=',')            # 10,20,30
print(x,y,z,sep=':')            # 10:20:30


'''
Form-4:  print() with end attribute:
        This attribute is used to print next line data in current line with space.
        The default value for end attribute is \n,which is nothing but new line character.

'''
print("Hello",end=' ')
print("Durga",end=' ')
print("Soft")               # Hello Durga Soft


'''
Form 5:
        printa() with formatted string.
        '''


name="Anil"
salary=10000
gf="#"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z=gf))

print(f"Hello {name} your salary is {salary} and Your Friend {gf} is waiting")
# output : Hello Anil your salary is 10000 and Your Friend # is waiting
