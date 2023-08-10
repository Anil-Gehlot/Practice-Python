# Simple Factorial program..

num=int(input("enter a no. : "))
y=1
for i in range(1,num+1):
	y=y*i

print("the factorial of {} is {} ".format(num,y))
