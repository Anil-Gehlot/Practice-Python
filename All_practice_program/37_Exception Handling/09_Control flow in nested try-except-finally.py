'''

try:
    statement 1
    statement 2
    statement 3
    try:
        statement 4
        statement 5
        statement 6
    except X:
        statement 7
    finally:
        statement 8
    statement 9
except Y:
    statement 10
finally:
    statement 11
statement 12



case-1: If there is no exception
1,2,3,4,5,6,8,9,11,12 Normal Termination

Case-2: If an exception raised at staement-2 and the corresponding except block matched
1,10,11,12  Normal Termination (** inner fianlly block will never be executed if controll didn't go to inner try block.)

Case-3: If an exceptiion raised at statement 2 and the corresponding except block not matched
1,11 Abnormal Termination(** before termination finally block always executed)

Case-4: If an exception raised at statement 5 and inner except block matched 
1,2,3,4,7,8,9,11,12 Normal Termination

Case-5: If an exception raised at statement 5 and inner except block not matched but outer
except block matched...
1,2,3,4,8,10,11,12 Normal Termination

case-6: If an exception raised at statement 5 and both inner and outer except blocks are not
matched
1,2,3,4,8,11 Abnormal Termination

case-7: If an exception raised at statement 7 and corresponding except block matched
1,2,3,(4 or 5 or 6),8,10,11,12,Normal Termination

case-8: If an exception raised at statement 7 and corresponding except block not matched.
 1,2,3,(4 or 5 or 6),8,11,Abnormal Termination

case-9: If an exception raised at statement 8 and corresponding except block matched.
1,2,3,(4 or 5 or 6 may or may not), (7 may or may not),10,11,12 Normal Termination

case-10: If an exception raised at statement 8 and corresponding except block not matched
1,2,3,(4 or 5 or 6 may or may not), (7 may or may not) ,11 abNormal Termination

case-11: If an exception raised at statement 9 and corresponding except block matched
1,2,3,(4 or 5 or 6 may or may not), (7 may or may not) ,8,10,11,12 Normal Termination

case-12: If an exception raised at statement 9 and corresponding except block not matched
1,2,3,(4 or 5 or 6 may or may not), (7 may or may not) ,8,11 ABNormal Termination

case-13: If an exception raised at statement 10 then it is always abonormal termination but
before abnormal termination finally block(statement 11) will be executed.

case-14: If an exception raised at statement 11 or statement 12 then it is always abnormal
termination.



**Note: 
If the control entered into try block then compulsary finally block will be executed.
If the control not entered into try block then finally block won't be executed.

'''