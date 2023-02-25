"""
Escape character : Escape character are used to insert characters that are illegal in a string. 
"""


#1. \n : To change the line.
a = "Anil\nGehlot"
print(a)
"""Output: 
            Anil
            Gehlot
"""


#2. \t : for tab
b = "Anil\tGehlot"
print(b)              # Output : Anil    Gehlot


#3. \r : for carriage return :
c = "Python is included in CodeSpeedy\r Anil gehlot works "
print(c)  
""" Output : Anil gehlot works in CodeSpeedy

you can see " Anil gehlot works " are having 19 characters so 
first 19 characters are being replaced by those 19 numbers.""" 


#4. \b : for backspace
d = "Prabhas\b bahaubali "
print(d)            # Prabha bahaubali


#5. \\ : form backslash 
e = "anil \\ gehlot"
print(e)            # anil \ gehlot
