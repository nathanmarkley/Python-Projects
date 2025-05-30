print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

anwser = input("What does CPU stand for? ")
if anwser.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

anwser = input("What does GPU stand for? ")
if anwser.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

anwser = input("What does RAM stand for? ")
if anwser.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

anwser = input("What does PSU stand for? ")
if anwser.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct! Which is " +  str((score / 4) * 100) + "%.")