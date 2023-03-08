

# Tuple Comprehension is not supported by Python.

t= ( x**2 for x in range(1,6))
print(type(t))      # <class 'generator'>
# Here we are not getting tuple object and we are getting generator object.

