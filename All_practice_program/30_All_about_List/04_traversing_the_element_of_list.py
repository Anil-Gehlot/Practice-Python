'''
The sequential access of each element in the list is called traversal.
'''
# By using while loop:
n=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1 
print()

# By using for loop:
n1 = [1,2,3,4,5,6,7,8,9,10]
for i in n1:
    print(i)
print()


# To display only even numbers :
n2 = [1,2,3,4,5,6,7,8,9,10,32,67,3,56,5,23,234,23423,452]
for i in n2:
    if i%2==0:
        print(i)

# To display elements by index wise :
l = [1,'d',6,'define']
for i in range(len(l)):
    print(f'Index of {l[i]} : {i} and {i-len(l)}')
    
