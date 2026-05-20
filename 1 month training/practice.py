print("Welcome to the calculator: ")
while True:
    print("[1] Addition")
    print("[2] Subtraction")
    print("[3] Multiplication")
    print("[4] Division")
    print("[0] exit")

    option = int(input("which operation do you want to do (enter option): "))

   
    if option == 1:
        total = 0
        n = int(input("Enter how many numbers you want to add: "))

        for i in range(n):
            num = float(input(f"Enter number {i + 1} =  "))
            total += num
        print(f"Total = {total}")
    elif option == 2:
        total = 0
        n = int(input("Enter how many numbers you want to subtract: "))

        for i in range(n):
            num = float(input(f"Enter number {i + 1} = "))
            total -= num
        print(f"Total = {total}")
    elif option == 3:
        total = 1
        n = int(input("Enter how many numbers you want to multiply: "))
    
        for i in range(n):
            num = float(input(f"Enter number {i + 1} = "))
            total *= num
        print(f"Total = {total}")
    elif option == 4:
        total = 1
        n = int(input("Enter how many numbers you want to divide: "))
    
        for i in range(n):
            num = float(input(f"Enter number {i +1} = "))
            total /= num
        print(f"Total = {total}")
    elif option == 0:
        break
    else:
        print("INVALID OPTION")
    print()




    