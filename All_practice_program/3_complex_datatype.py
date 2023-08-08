"""
syntax of complex number : a + bj    (where j is necessary)

    a = Real part
    b = Imaginary part 
    j = (-1)^1/2   (underroot -1  ====iota)

    Real part dcan be anything like binary,octal,hexa-decimal,decimal
    BUT the Imaginary Part must be decimal(int  or float )

    x = 0B11111 + 20j   (it is right)
    y = 15 + 0B1111j     (it is not right)
"""

a = 10+20j
b = 20+30j

print("Addition of complex number : ", a+b)
print("--------------------------------------")
print("Substraction of complex number : ", a-b)
print("--------------------------------------")
print("multiplication of complex number : ", a*b)
print("--------------------------------------")
print("division of complex number : ", a/b)
print("--------------------------------------")

# To find the real part of the complex number 
print("Real part of a : ",a.real)
print("Real part of b : ",b.real)
print("--------------------------------------")

# To find the imaginary part of the complex number 
print("Imaginary part of a : ",a.imag)
print("Imaginary part of b : ",b.imag)
print("--------------------------------------")


