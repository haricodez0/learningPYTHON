import pyttsx3
import datetime

engine = pyttsx3.init()

while True:
    question = input("What do you want to know? ")

    if "time" in question.lower():
        now = datetime.datetime.now().strftime("%I:%M %p")
        print("The time is:", now)
        engine.say(f"The time is {now}")
    elif "who made you?" in question.lower():
        print("I was made by hariharan")
        engine.say("I was made by hariharan")
  
    else:
        print("I don't know that yet.")
        engine.say("I don't know that yet.")

    engine.runAndWait()
    

