'''
Handling csv files:

CSV==>Comma seperated values

As the part of programming, it is very common requirement to write and read data wrt csv
files. Python provides csv module to handle csv files.
'''

import csv
f = open('emp.csv','w',newline="")
w = csv.writer(f)       # # returns csv writer object
w.writerow(['E_NO', "E_NAME", "E_SALARY", "E_CITY"])
num = int(input('enter no of emp: '))
for i in range(num):
    e_no=input('Enter employee number: ')
    e_name=input('Enter employee name: ')
    e_salary=input('Enter employee salry: ')
    e_city=input('Enter employee city: ')
    w.writerow([e_no,e_name,e_salary,e_city])
print("Data written successfully")
f.close()

'''
OUTPUT:

E_NO,E_NAME,E_SALARY,E_CITY
1,lokesh,100,byawara
2,anil,200,indore
3,harsh,300,dewas
4,pari,400,indore
5,sunny,500,indore


Note: Observe the difference with newline attribute and without
with open("emp.csv","w",newline='') as f:
with open("emp.csv","w") as f:

Note: If we are not using newline attribute then in the csv file blank lines will be included
between data. To prevent these blank lines, newline attribute is required in Python-3,but
in Python-2 just we can specify mode as 'wb' and we are not required to use newline
attribute.
'''


# Reading Data from csv file:

import csv
f = open("emp.csv",'r')
r = csv.reader(f)
data=list(r)
# print(data)
for line in data:
    for word in line:
        print(word, '\t',end="")
    else:
        print()
    # print(line)

"""
OUTPUT:

E_NO    E_NAME  E_SALARY        E_CITY 
1       lokesh  100     byawara
2       anil    200     indore
3       harsh   300     dewas
4       pari    400     indore
5       sunny   500     indore

"""