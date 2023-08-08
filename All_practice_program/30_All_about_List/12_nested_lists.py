'''
Sometimes we can take one list inside another list. Such type of lists are called nested lists.

Note: We can access nested list elements by using index just like accessing multi
        dimensional array elements.
'''
l1 = [1,2,3,4,[5,6,7,],23,45,[8,9,0],567,789]

print(l1)           # [1, 2, 3, 4, [5, 6, 7], 23, 45, [8, 9, 0], 567, 789]
print(l1[0])        # 1
print(l1[4])        # [5, 6, 7]
print(l1[4][0])     # 5
print(l1[7][1])     # 9

# print(l1[3][5])     # TypeError: 'int' object is not subscriptable
print()


# Nested List as Matrix:
l2 =[[10,20,30],[40,50,60],[70,80,90]] 
print("Element by row wise : ")
for i in l2 :
    print(i)

'''
output :
Element by row wise :
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
'''
# 1st way to display element in matrix style :
print("elemement in matrix style : ")
for j in l2:
    for k in j:
        print(k,end=" ")
    print()
'''
outpit :
Elements by Matrix style:
10 20 30
40 50 60
70 80 90
'''
# 2nd way to display element in matrix style : 
n =[[10,20,30],[40,50,60],[70,80,90]] 
print("Elements by Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()
'''
output :
Elements by Matrix style:
10 20 30
40 50 60
70 80 90
'''       
