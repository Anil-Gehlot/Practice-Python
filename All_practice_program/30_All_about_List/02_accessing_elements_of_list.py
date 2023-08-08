'''
Accessing elements of List : 
                            We can access elements of the list either by using index or by using slice operator(:).                            

        1) By using index:

        list's index starts with zero means that index of first element of list is zero.
        list supports both positive(+ve) & negative(-ve) indexes.
        positive(+ve) index means for Left to Right direction.
        negative(-ve) index means for Right to Left direction.
        
        2) By using slice operator:
        Syntax : list2= list1[start:stop:step]

        start ==>it indicates the index where slice has to start default value is 0.

        stop ===>It indicates the index where slice has to end
                    default value is max allowed index of list ie length of the list.

        step ==>increment value default value is 1.
        
'''
l = [1,2,3,5,6,'a','g','prabhas',43,64,35]

print(l[0])            # 1
print(l[-1])           # 35
print(l[8])            # 43

print(l[2:8])           # [3,5,6,'a','g','prabhas']
print(l[8:2:-2])        # [43, 'g', 6]
print(l[4:80])          # [6, 'a', 'g', 'prabhas', 43, 64, 35]
print(l[-1:8])          # []
