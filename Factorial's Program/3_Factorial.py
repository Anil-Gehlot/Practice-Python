
num=int(input("enter a no. : "))
fact=1
if num==0 or num==1:
	print("{} is factorial of {}".format(fact,num))
else:
	for j in range(1,num+1):
		fact=fact*j
	print("{} is factorial of {}".format(fact,num))