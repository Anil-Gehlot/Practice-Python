#Factorial Program using Recusion.

def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)

var1=int(input("enter value : "))
result=fact(var1)
print("factorial of {} = {} ".format(var1,result))