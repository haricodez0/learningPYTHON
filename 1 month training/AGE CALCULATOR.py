from datetime import date

def AGE_CALCULATOR():

    print("Age calculator: ")
    
    BirthDate = int(input("Enter your birth year: "))
    CurrentDate = date.today().year198
    AGE = CurrentDate - BirthDate 

    print(AGE)

    input("press enter to exit")

AGE_CALCULATOR()