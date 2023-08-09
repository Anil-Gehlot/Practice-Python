student1= ['anil','mca','ag7@gmail.com']

#The insert() method add an element in List at specified index.
#Syntax : listname.insert(index,element)

student1.insert(1,"sec A")
print(student1)

section="sec b"
student1.insert(3,section)
print(student1)


# if we give index value out of range of list,it will add element at last.
section="sec b"
student1.insert(9,section)
print(student1)
