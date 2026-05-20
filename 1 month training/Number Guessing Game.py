import random
import time

def Guessing_Game():

    print("Im thinking of a number between 1 - 100, can you try an guess it\n")
    
    Secret_Number = random.randint(1,100)
  
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess == Secret_Number:
            print("congrats! you guessed it right!")
            time.sleep(1)
            break
        elif guess < Secret_Number:
            if Secret_Number-guess < Secret_Number:
                print("It's low, guess higher!")
            else:
                print("It's too low, guss higher!")
        elif guess > Secret_Number:
            if guess-Secret_Number < Secret_Number:
                print("It's high, guess lower!")
            else:
                print("It's too high, guess lower!")
            

Guessing_Game()

            
