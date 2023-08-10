
#index() method is used to find the index of any element where it occurs first.

tuple1=(25,10,25.5,"star wars",5)
epic=tuple((25,10,11,25,0.75,"thar",25))

print(tuple1.index(10))
print(epic.index(25))

# if we are passing an element which is not in the Tuple, it will raise an error.
print(epic.index(7))
