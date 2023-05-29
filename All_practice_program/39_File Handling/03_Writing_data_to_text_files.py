'''
We can write character data to the text files by using the following 2 methods.

1. write(str)
2. writelines(list of lines)
'''

# 1st Method.....

f=open("abcd.txt",'w')
f.write("Jay\n")
f.write("Mahishmati\n")
f.write("Samrajya\n")

print("Data written to the file successfully")
f.close() 

'''
OUTPUT:
Jay
Mahishmati
Samrajya


**Note: In the above program, data present in the file will be overridden everytime if we
run the program. Instead of overriding if we want append operation then we should open
the file as follows.

 f = open("abcd.txt","a")
'''

# 2nd Method...

f=open("abcde.txt",'w')
list=["Venkata\n","Suryanarayana\n","PRABHAS\n","Raju\n","Uppalpati"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close() 

'''
OUTPUT:
Venkata
Suryanarayana
PRABHAS
Raju
Uppalpati


Note: while writing data by using write() methods, compulsory we have to provide line
seperator(\n),otherwise total data should be written to a single line.

Such as : VenkataSuryanarayanaPRABHASRajuUppalpati
'''