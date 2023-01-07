#2.2.1
list=[55,42,77,63,29,57,89]
count_pass=0
total_no_of_marks=len(list)

for i in list:
    if i>=50:
        count_pass+=1

percentage= (count_pass*100)/total_no_of_marks