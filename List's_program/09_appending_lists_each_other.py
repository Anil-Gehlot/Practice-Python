#appending list each other 
l1=[23,43,3,534,3]
l2=[234,65,5,67,7]
l3=[345,6,4,575,8]


l3.append(l2) #it will append whole list  
print(l3)          

for i in l2:
	l1.append(i)    #it will append the each elementn one by one
print(l1)
