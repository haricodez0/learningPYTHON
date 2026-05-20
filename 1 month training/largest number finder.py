

def Largest_Number():
    print("largest number finder: ")

    while True:
        numbers = []
        n = int(input("Enter the number of numbers: "))

        for i in range(n):
          num = float(input(f"Enter number{i + 1}:"))
          numbers.append(num)

        largest = max(numbers)
        print(largest)


    
Largest_Number()

