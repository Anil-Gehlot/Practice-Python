try:
    print(10/0)
except  ZeroDivisionError as msg:
    print("exception raised and its description is:",msg)


# Output:  exception raised and its description is: division by zero 
