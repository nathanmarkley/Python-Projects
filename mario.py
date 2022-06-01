import time

def main():
    height = get_height()
    width = get_width()
    for i in range(width):
        for j in range(height):
            print("#", end="")
        print()

def get_height():
    while True:
        try:
            n = int(input("Enter Height: "))
            if n > 0:
                break
        except ValueError:
            print("Please enter a number!")
    return n 

def get_width():
    while True:
        try:
            n = int(input("Enter Width: "))
            if n > 0:
                break
        except ValueError:
            print("Please enter a number!")
    return n 

main()