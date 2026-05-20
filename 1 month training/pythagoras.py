import math
print("Hypotenuse finder")
while True:
        a = int(input("Enter the adjacent side of the triangle: "))
        b = int(input("Enter the opposite side of the triangle: "))

        
        c = math.sqrt(a**2 + b**2)
        print(f"Hypotenuse = {c}")
        
        