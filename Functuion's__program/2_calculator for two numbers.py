def calculater(x,y,z):
    if z == "+" :
        result = x+y
    elif z== "-" :
        result = x-y
    elif z== "*":
        result = x*y
    else:
        result=x/y
    return result

a = float(input("enter first no. :  "))
b=float(input("enter second no. : "))
c=input("enter the operation (+ , - , * , /) : ")
d=calculater(a,b,c)

print("\n the result is : ",d)