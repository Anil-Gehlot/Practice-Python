# This function is used to repeat again the process of calculator, if user wants...
 
def takechoice():
    choice=input("\n Enter y for Yes and n for No : ")
    if choice=="y" or choice=="Y":
        return True
    elif choice=="n" or choice=="N":
        return False
    else:
        print('\nInvaid choice')
        takechoice()
