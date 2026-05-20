print("Type exit to leave\n")
words = []

while True:
    
    word = input("Enter a word: ")
    words.append(word)

    print(words)

    if word == "exit":
        break