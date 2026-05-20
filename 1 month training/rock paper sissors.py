import random
import time

def Rock_Paper_scissors():
    wins = 0
    losses = 0
    ties = 0
    while True:

        options = ["rock","paper","scissors"]

        print("Rock Paper scissors game\n")
        print("ROCK!")
        time.sleep(1)
        print("PAPER!")
        time.sleep(1)
        print("SCISSORS!")
        time.sleep(1)

        guess = input("enter your guess: ").lower()
    
        if guess not in options:
            print("enter only rock/paper/scissors")
            continue

        output = random.choice(options)
        print(f"computer chose: {output}")

        if guess == output:
            print("Its a tie!")
            print()
            ties += 1
        elif (guess == "rock" and output == "scissor") or \
            (guess == "scissor" and output == "paper") or \
            (guess == "paper"  and  output == "rock"):
            print('Congrats! you won')
            print()
            wins += 1
        else:
            print("You lost, better luck next time")
            print()
            losses += 1

        print("Scoreboard: ")
        print(f"Wins = {wins} | losses = {losses} | ties = {ties}")
        
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again != "y":
            print("Thanks for playing")
            time.sleep(1)
            break
        
            


       

Rock_Paper_scissors()




    




