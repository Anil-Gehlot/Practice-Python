# ##upper to lower 

# x=input("enter value : ")
# y=""
# for i in x:
# 	if ord(i)>=65 and ord(i)<=90:
# 		a=ord(i)+32
# 		b=chr(a)
# 		y=y+b
# 	# elif ord(i)>=97 and ord(i)<=122:
# 	# 	y=y+i
# 	# else:
# 	# 	print("invalid character")    #this is overcode ....jarurat hi ni h  
# 	# 	break
# 	else:
# 		y=y+i

# print("value before conversion : ",x)
# print("value after conversion : ",y)

##upper to  lower 

x=input("enter value : ")
y=""
for i in x:
	if ord(i)>=97 and ord(i)<=122:
		a=ord(i)-32
		b=chr(a)
		y=y+b
	
	else:
		y=y+i

print("value before conversion : ",x)
print("value after conversion : ",y)