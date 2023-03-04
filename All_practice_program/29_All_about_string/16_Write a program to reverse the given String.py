
# 1st Way:
s=input("Enter Some String:")
print(s[::-1])

# 2nd way:
t=input("Enter Some String:")
print(''.join(reversed(t)))

# 3rd way :
s=input("Enter Some String:")
i=len(s)-1
target=''
while i>=0:
    target=target+s[i]
    i=i-1
print(target)
