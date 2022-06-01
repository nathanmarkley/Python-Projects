try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("That is not an number! Please enter a number.")
    exit()
#try:
 #   y = int(input("y: "))
#except ValueError:
    #print("That is not an number! Please enter a number.")
    #exit()
print(x + y)