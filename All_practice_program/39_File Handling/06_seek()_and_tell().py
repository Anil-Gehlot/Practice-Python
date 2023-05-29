'''
tell():

We can use tell() method to return current position of the cursor(file pointer).
The position(index) of first character in files is zero just like string index.
'''

f = open('abcde.txt','r')
print('Cursor position: ',f.tell())

print(f.read(5))
print('Cursor position: ',f.tell())

print(f.read(7))
print('Cursor position: ',f.tell())

print(f.readline())
print('Cursor position: ',f.tell())

print(f.read())
print('Cursor position: ',f.tell())

'''
OUTPUT:

Cursor position:  0
Venka
Cursor position:  5
ta
Sury
Cursor position:  13
anarayana

Cursor position:  24
PRABHAS
Raju
Uppalpati
Cursor position:  48
'''

#------------------------------------------------------------------------------------

print("------------")
'''
seek():

We can use seek() method to move cursor(file pointer) to specified location.
Eg: f.seek(offset)
'''

data='I am a good boy with bad attiquetes.'
f=open('abc.txt','w')
f.write(data)
f.close()

with open('abc.txt','r+') as f:
    text = f.read()
    print(text)
    print('Cursor position: ',f.tell())

    f.seek(12)
    f.write('boy with good attiquetes.')
    f.seek(0)
    text=f.read()
    print('Data with modification: ',text)
    print('Cursor position: ',f.tell())
    f.seek(0)
    print('Cursor position: ',f.tell())

'''
OUTPUT:

I am a good boy with bad attiquetes.
Cursor position:  36
Data with modification:  I am a good boy with good attiquetes.
Cursor position:  37
Cursor position:  0
'''
