#E = MC^2
#Ask user for mass as an integer (in kilograms)
m = int(input("Enter mass: "))

#C = speed of light 300000000 meters per second
exp = 2
c = pow(300000000, exp)

#take input and times by speed of light(c) to find energy(e)
e = m*c

#output energy
print(e)