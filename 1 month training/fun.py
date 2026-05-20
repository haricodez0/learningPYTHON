from operator import add


def addition():
    print("Addition calculator: \n")
    while True:
        
        
        try:
            total = 0
            n = int(input("How many numbers do u want to add: "))

            for i in range(n):
                num = float(input(f"Enter number {i+1} = "))
                total += num

            print(f"Total = {total}")
        
        except ValueError:
            print("Error please enter a number!\n")


addition()