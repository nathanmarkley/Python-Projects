from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('pwd.csv', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, user, passw = data.split("|")
            print("Account name:", name, "- Username:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    username = input('Username: ')
    pwd = input('Password: ')

    with open('pwd.csv', 'a') as f:
        f.write(name + "|" + username + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Do you want to view or add a new password (view/add/q)? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invaild mode.")
        continue