
try:
    print('statement 1')
    print('statement 2')
    print('statement 3')
except:
    print('statement 4')
finally:
    print('statement 5')

print("statement 6")



'''
Case 1: if  there is no exception.
1,2,3,5,6 will be executed (Normal Termination)

Case 2: If an exception raised at stmt2 and the corresponding except block matched.
1,4,5,6 will be executed Normal Termination.

Case 3: If an exception raised at stmt2 but the corresponding except block not matched.
1,5 will be executed Abnormal Termination

Case 4: :If an exception raised at stmt4(in exept block) then it is always abnormal termination but before
that finally block will be executed.

Case 5: : If an exception raised at stmt-5 or at stmt-6 then it is always abnormal
termination

'''
