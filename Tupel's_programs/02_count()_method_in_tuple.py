
#count() method is used to to count the number of element in tuple.It takes 1 argument.

tuple1=(25,10,25.5,"star wars",5)
epic=tuple((25,10,11,25,0.75,"thar",25))

print(tuple1.count(5))
print(epic.count(25))

#if there is no element in tuple which we are passing as an argument , occurence of that number is zero(0).
print(epic.count(7))
