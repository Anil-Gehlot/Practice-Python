# # by taking additional variable(1st type of swapping)
# a=1
# b=5
# print(a,b)
# temp=a
# a=b
# b=temp
# print(a,b)

##by not taking the additional variable
# a=1
# b=5
# print(a,b)
# a=a+b
# b=a-b
# a=a-b
# print(a,b)



# #python ko khoobsurti❤️ batane ke liye
# a=1
# b=5
# print(a,b)
# a,b=b,a
# print(a,b)

#program to find greatest among five number without using "and" & "or" operator......

a=int(input("enter first number  : "))
b=int(input("enter second number : "))
c=int(input("enter third number  : "))
d=int(input("enter fourth number : "))
e=int(input("enter fifth number  : "))
smallest=a

if smallest>b:
	smallest=b

if smallest>c:
	smallest=c

if smallest>d:
	smallest=d
	
if smallest>e:
	smallest=e

print(smallest)



