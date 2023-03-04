'''
We can use the following 4 methods to find the index of substring.

For forward direction:    find() & index()

For backward direction:    rfind() &  rindex()
'''

'''
1. find():
syntaxs : s.find(substring)
Returns index of first occurrence of the given substring. If it is not available then we will get -1.it doesn't raise error.It will always search from bEgin index to end-1 index.
        
        By default find() method can search total string. We can also specify the boundaries to
search.    
s.find(substring,bEgin,end)

2. rfind():
syntaxs : s.find(substring)
rfind method works same as find but it starts search from backward direction.

***Both find() and rfind() return positive index value.

'''
str="Learning Python is very easy"
print(str.find('s'))             # 17
print(str.find('Python'))        # 9
print(str.find('is'))            # 16
print(str.find('python'))        # -1
print(str.find('java'))          # -1
print(str.find('r'))             # 3
print(str.find('i',7,99))        #16

print()
print(str.rfind('is'))           # -1
print(str.rfind('r'))            # 21
print(str.rfind('s'))            # 26
print()

'''
index() method:  index() method is exactly same as find() method except that if the specified substring is not
available then we will get ValueError.
'''

str="Learning Python is very easy"
print(str.index('s'))             # 17
print(str.index('Python'))        # 9
print(str.index('is'))            # 16
# print(str.index('python'))        # ValueError: substring not found
# print(str.index('java'))          # ValueError: substring not found
print(str.index('r'))             # 3
print(str.index('i',7,99))        # 16

print()
print(str.rindex('is'))           # 16
print(str.rindex('r'))            # 21
print(str.rindex('s'))            # 26
print()

'''
******index() and find() both are same, both returns index value of given substring ,
BUt find() doen't raise any error when element not found in main error ,it returns -1,,
whereas index() raise ValueError: substring not found.*******'''

s=input("Enter main string:")
subs=input("Enter sub string:")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at position",pos)
    flag=True
if flag==False:
    print("Not Found")
    

    