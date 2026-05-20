import time
while True:
    try:
        name = str(input("enter your name: "))
    except ValueError:
        print("ERROR! Name should only contain letters")
    try:
        Date = int(input("which year where you born: "))
    except ValueError:
        print("ERROR! year should only be in numbers")
    email =input("enter your email: ")
    print("processing...")
    time.sleep(1)
    print("your gay")
