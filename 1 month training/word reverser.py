from tkinter import N


def Word_reverser():
    while True:
        print("this program reverses the word you type\n")

        word = input("Type a word: ")
        word = list(word)
        word.reverse()

        print(word)
        print()

Word_reverser()
