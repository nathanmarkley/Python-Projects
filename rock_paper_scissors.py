import random

userWins = 0
computerWins = 0

options = ["rock", "paper", "scissors"]

while True: 
    userInput = input("Choose either Rock, Paper, Scissors, or Q to quit: ").lower()
    if userInput == "q":
        break
    
    if userInput not in options:
        continue

    randomNumber = random.randint(0, 2)
    #rock: 0, paper: 1, scossirs: 2
    computerPick = options[randomNumber]
    print("Computer picked", computerPick + ".")

    if userInput == "rock" and computerPick == "scissors":
        print("You Won!")
        userWins += 1

    elif userInput == "paper" and computerPick == "rock":
        print("You Won!")
        userWins += 1

    elif userInput == "scissors" and computerPick == "paper":
        print("You Won!")
        userWins += 1
    
    else:
        print("You lost!")
        computerWins += 1

print("You won", userWins, "times.")
print("The computer won", computerWins, "times.")
print("Goodbye!")
