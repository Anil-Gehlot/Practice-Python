'''
We can use the following 3 methods to remove spaces from the string.

1. rstrip()===>To remove spaces at right hand side.
2. lstrip()===>To remove spaces at left hand side.
3. strip() ==>To remove spaces both sides.
'''

city1 = "  Indore  "        # removing space from left side only.
print(city1.lstrip())        # Indore

city2 = '  Hyderabad'       # removing space from right side only.
print(city2.rstrip())           #   Hyderabad

city3 = '   Chennai   '         # removing space from both side .
print(city3.strip())            # Chennai
print()

# program 

city=input("Enter your city Name:")
scity=city.strip()
if scity=='hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity=='chennai':
    print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
    print("Hello Kannadiga...Shubhodaya")
elif scity=="indore":
    print("Bhiyao ramm...❤️❤️")
else:
    print("your entered city is invalid")
    
