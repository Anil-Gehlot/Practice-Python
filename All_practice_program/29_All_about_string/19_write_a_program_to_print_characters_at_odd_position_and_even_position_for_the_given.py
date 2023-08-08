
# 1st way 

s=input("Enter Some String:")
print("Characters at Even Position:",s[0::2])
print("Characters at Odd Position:",s[1::2])

# 2nd way 

s=input("Enter Some String:")
i=0
print("Characters at Even Position:")
while i< len(s):
    print(s[i],end=',')
    i=i+2
print()
print("Characters at Odd Position:")
i=1
while i< len(s):
    print(s[i],end=',')
    i=i+2 
