import string
import time

def Palindrom_checker():
    print("This program checks is the word is the same as the inverted: \n")

    while True:
        word = str(input("Type a word(or type exit to leave program): "))

        if word == "exit":
            print("exiting program...")
            time.sleep(1)
            break

        word = "".join(ch for ch in word if ch.isalnum())
        
        reverse = word[:: -1]
        
       
        if word == reverse:
            print("Yes, this word is a palindrome")
        else:
            print("No, this word is not a palindrome")

Palindrom_checker()

    

