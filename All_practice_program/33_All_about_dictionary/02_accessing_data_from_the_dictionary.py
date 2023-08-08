
'''
We can access data by using keys.
If the specified key is not available then we will get KeyError

'''

d1 = {'anil':'MCA',"manoj":'b.com','manish':'BCA'}

print(d1['anil'])       # MCA
print(d1['manish'])     # BCA
print(d1['BCA'])        # KeyError: 'BCA'
