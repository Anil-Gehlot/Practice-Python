# Function of Factorial Program 

def factorioal(num):
    fact=1
    if num==0 or num==1:
        fact=1
    else:
        for i in range(1,num+1):
            fact=fact*i
    return fact

choice = int (input("enter value : "))
factorioal_value=factorioal(choice)
print("factorial of {} is {} ".format(choice,factorioal_value))
