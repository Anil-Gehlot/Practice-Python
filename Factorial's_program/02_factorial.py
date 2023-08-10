 
# Factorial in Reverse Loop 

num = int(input("enter a no. : "))
y=1
for i in range(num,0,-1):
	y=y*i

print("factorial of {} is {} ".format(num,y))
