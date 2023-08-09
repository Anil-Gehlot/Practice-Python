star={ 2,4,6,1,2,11,"yes","no",2.4,255,2+1j}

"""discard() method also removes the specified element , 
	but  remove() method will raise an error if the specified element does not exist in set, 
	whereas the discard() method will not."""
	
star.discard("no")
star.discard("anil")
print(star)
