import pyttsx3

engine = pyttsx3.init()
name = input("What is your name? ")
engine.say(f"hello, {name}")
engine.runAndWait()
