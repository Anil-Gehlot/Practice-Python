'''
We can read character data from text file by using the following read methods.

read()      :To read total data from the file
read(n)     : To read 'n' characters from the file
readline()  : To read only one line
readlines() : To read all lines into a list
'''

# Eg 1: To read total data from the file.

f = open('abcde.txt','r')
data = f.read()
print(data)
f.close()

'''
OUTPUT:

Venkata
Suryanarayana
PRABHAS
Raju
Uppalpati
'''

# Eg 2: To read only first 10 characters:

f = open('abcde.txt','r')
data = f.read(10)
print(data)
f.close()
'''
OUTPUT:
Venkata
Su
'''

# Eg 3: To read data line by line:

f=open('abcde.txt','r')
line1 = f.readline()
print('Line 1: ',line1,end="")
line2 = f.readline()
print('Line 2: ',line2,end="")
line3 = f.readline()
print('Line 3: ',line3,end="")

'''
OUTPUT:
Line 1:  Venkata
Line 2:  Suryanarayana
Line 3:  PRABHAS

if we will not add end="" inside the print statement,
then our output will be :

Line 1:  Venkata

Line 2:  Suryanarayana

Line 3:  PRABHAS

because we have added \n after each line, print() also 
starts with new line.
'''

# Eg 4: To read all lines into list:
f = open('abcde.txt','r')
list=f.readlines()
print(list)

'''
OUTPUT:

['Venkata\n', 'Suryanarayana\n', 'PRABHAS\n', 'Raju\n', 'Uppalpati']
'''

# Final Example:

f = open('abcde.txt','r')

print(f.read(3)) #now cursor will be at 3rd position

print(f.readline(), end="") # now cursor will be on the second line.

print(f.read(4)) # now the cursor will be on the fourth position of the 2nd line.
print('Remaining Data: ')
print(f.read()) # now the cursor will be at the end

'''
OUTPUT:

Ven
kata
Sury
Remaining Data: 
anarayana
PRABHAS
Raju
Uppalpati
'''
