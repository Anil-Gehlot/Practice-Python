import typecheck as tc
import convert_into_final_number as final

def calculator():
    print("""============================
  WELCOME TO MY CALCULATOR  
============================""")
    choice=input("""Please, enter your choice : which operation do wnn'na perform....
    \n1.Addition \n2.Substaction \n3.Multiplication \n4.Division \n5.Modules \n6.Exponent\n\n  Enter your choice : """)

    first_number=input("Enter first number : ")
    second_number=input("Enter second number : ")

    print("\nFirst Number is given in : ",type(first_number))
    print("Second Number is given in : ",type(second_number))

    first_number=tc.typecheck(first_number)
    second_number=tc.typecheck(second_number)

    print("\nFirst Number is converted into : ",type(first_number))
    print("Second Number is converted into : ",type(second_number))



    if choice=="1":
      result=first_number+second_number
    elif choice=="2":
      result=first_number-second_number
      
    elif choice=="3":
      result=first_number*second_number
      
    elif choice=="4":
      if second_number != 0:
          result=first_number/second_number
      else:
        print("\n CAN NOT DEVIDE BY ZERO(0): PLEASE TRY AGAIN")
        calculator()
      
    elif choice=="5":
      result=first_number%second_number
      
    elif choice=="6":
      result=first_number**second_number
    else :
      print("\nInvalid selection :: please select from the given choice.")
      calculator()
    
    return result

