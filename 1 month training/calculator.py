 
print("Basic calculator: \n ")
print("[1] addition")
print("[2] subtraction")
print("[3] multiplication")
print("[4] division")

option = input("enter what calculation you want to do: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if option == "1":
     result = num1 + num2
elif option == "2":
     result = num1 - num2
elif option == "3":
     result = num1 * num2
elif option == "4":
     if num2 == 0:
         print("CANNOT DIVIDE BY ZERO")
     result = num1 / num2
else:
     print("INVALID OPTION")
     


print(f"result = {result}")

 
input("/////////////////////////////////////////////////PRESS ENTER TO EXIT/////////////////////////////////////////////////")





            
