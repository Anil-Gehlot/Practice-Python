
'''
Once we creates tuple,we cannot change its content.
Hence tuple objects are immutable.
'''

t = (10,20,30,40,50)
t[3] = '70'     # TypeError: 'tuple' object does not support item assignment

"""
tuple is made only for performing reading operation ,
we can't update or delete element from the tuple.
"""