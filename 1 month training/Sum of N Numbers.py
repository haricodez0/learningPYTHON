def Sum_of_N_Numbers():
    total = 0

    n = int(input("Enter how many numbers you want to add: "))

    for i in range(n):
        num = float(input(f"Enter number {i + 1} = "))
        total += num

    print(f"The sum = {total} ")

    input("press enter to exit")

Sum_of_N_Numbers()
