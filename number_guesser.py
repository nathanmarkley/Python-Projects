import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Guess a number between 0 and " + str(top_of_range) + "? ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please type a number.")
        continue

    if userGuess == random_number:
        print("Yes, you guessed correctly!")
        break
    elif userGuess > random_number:
        print("You guessed above the number!")
    else:
        print("You guessed below the number!")

print("You guessed in", guesses, "guesses")