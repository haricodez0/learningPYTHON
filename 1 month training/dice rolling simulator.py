import random
import time

def dice():
    print("Dice rolling simulator: \n")

    while True:
        input("Press enter to roll the dice..")
        print(f"You rolled a {random.randint(1,6)}")
        dice = str(input("Do you want to roll the dice again(y/n)")).lower()

        if dice != "y":
            print("Thanks for playing!")
            time.sleep(1)
            break

dice()
