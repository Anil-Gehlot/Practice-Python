"""
Operator precedence : Operator precedence describes the order in which operations are performed.

              Operators	                            Description

                 ()	                                Parentheses	
                 **	                                Exponentiation	
                 +x  -x  ~x	                        Unary plus, unary minus, and bitwise NOT	
                 *  /  //  %	                    Multiplication, division, floor division, and modulus	
                 +  -	                            Addition and subtraction	
                 <<  >>	                            Bitwise left and right shifts	
                 &                                 	Bitwise AND	
                 ^	                                Bitwise XOR	
                 |                                  Bitwise OR	
                 ==  !=  >  >=  <  <=               Comparisons operators	
                 is , is not                         Identity operators 
                 in , not in                         Membership operators 
                 not	                            Logical NOT	
                 and	                            Logical AND	
                 or	                                Logical OR

    If two operators have the same precedence, the expression is evaluated from left to right.
"""

a = 30
b = 20
c = 10
d = 5

print((a+b)*c/d)        # 100.0
print((a+b)/c*d)        # 25.0

print(a+b-c)            # 40
print(a-d+b)            # 45