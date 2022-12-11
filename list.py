# student1= ['tiku','mca','tiku007@gmail.com']

# print(student1[0])
# print(student1)

# phone="8269529568"
# student1.append(phone)    #with additional variable
# print(student1)

# student1.append("9098606045")   #without additional variable
# print(student1)


# student1.insert(1,"sec A")
# print(student1)

# section="sec b"
# student1.insert(1,section)
# print(student1)

# student1.pop()
# print(student1)   #delete last element

# student1.remove("tiku") # delete specified element
# print(student1)


# # this is wrong code😂😂😂
# for i in range(3):
# 	name =input( "enter name of the student : ")
# 	classs = input( "enter class of the student : ")
# 	contact = input( "enter contact of the student : ")
# 	email = input( "enter email of the student : ")

# 	list=[name,classs,contact,email]

# 	print("my nane is {} , i study in {} , my contact no. is {} and my email is {}".format(name,classs,contact,email))
# 	print(" ")

# # program
# student1=[input("enter name : ") , input("enter course : ") , input("enter email : ")]
# student2=[input("enter name : ") , input("enter course : ") , input("enter email : ")]
# print("I am {}.I am student of {}. my email is {}.".format(student1[0],student1[1],student1[2]))
# print("I am {}.I am student of {}. my email is {}.".format(student2[0],student2[1],student2[2]))


# ###string ko reverse karna
# userstr=input("enter your string : ")
# reverse= ""
# for i in range(len(userstr)-1,-1,-1):
#     reverse=reverse+userstr[i]
# print("user given string is {} ".format(userstr))
# print("reverse string is {} ".format(reverse))

##id 
# list1= [15,12,13,14,15]
# list1.append(23)
# print(list1)
# print(id(list1))

# list1.remove(15)
# print(list1)
# print(id(list1))


###adding lists each other
# l1=[15,12,13,14]
# l2=[21,16,11]
# print(l1,l2)

# l1=l1+l2
# print(l1)

# l1.append(l2)
# print(l1)

# for i in l2:
# 	l1.append(i)
# print(l1,l2)


i=int(input("enter fact : "))
fact=1
if i==0 or i==1:
	print("{} is factorial of {}".format(fact,i))
else:
	for j in range(1,i+1):
		fact=fact*j
	print("{} is factorial of {}".format(fact,i))