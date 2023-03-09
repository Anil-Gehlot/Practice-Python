
'''
We can update new pair of key-value.
Syntax : d[key]=value

If the key is not available then a new entry will be added to the dictionary with the
specified key-value pair.

If the key is already available then old value will be replaced with new value.
'''


d1 = {'anil':'MCA',"manoj":'b.com','manish':'BCA'}

d1['kapil'] = "BBA"
print(d1)                   # {'anil': 'MCA', 'manoj': 'b.com', 'manish': 'BCA', 'kapil': 'BBA'}

d1['chetan']= 'MBA'
print(d1)                   # {'anil': 'MCA', 'manoj': 'b.com', 'manish': 'BCA', 'kapil': 'BBA', 'chetan': 'MBA'}

d1['anil'] = "B.Tech"       # old value will be replaced to the new one.
print(d1)                   # {'anil': 'B.Tech', 'manoj': 'b.com', 'manish': 'BCA', 'kapil': 'BBA', 'chetan': 'MBA'}

