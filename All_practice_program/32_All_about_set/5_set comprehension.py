
s1 = {x*2 for x in range(5)}
print(s1)           # {0, 2, 4, 6, 8}

s2 = {int(i) for i in range(10) if i%3==0}
print(s2)           # {0, 9, 3, 6}

s3 = {j*j for j in range(7)}
print(s3)           # {0, 1, 4, 36, 9, 16, 25}

s4 = {2**k for k in range(1,20,2)}
print(s4)           # {512, 32, 2, 128, 2048, 8192, 32768, 131072, 8, 524288}