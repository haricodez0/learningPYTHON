def vowels():
    print("This program counts the number of vowels in a word\n")
   
    while True:
      vowels = ["a","e","i","o","u"]

      Word = str(input("type a word: "))

      count = 0
      for char in Word:
          if char in vowels:
              count += 1
      

      print(f"number of vowels = {count}")

      
vowels()