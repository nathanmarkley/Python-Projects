from string import ascii_letters, digits
from itertools import product

for passcode in product(ascii_letters + digits, repeat=6):
    print("".join(passcode))
