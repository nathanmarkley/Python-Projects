#password generator
import random, string
from tkinter import *
import pyperclip

#Initialize Window
root = Tk()
root.geometry("400x400") #default size of the window

#title of the window
root.title("Randowm Pssword Generator")

output_pass = StringVar()

#Function for calculation of password 
#Random Password generator function 
def randPassGen():

    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*()?"

    all = letters + digits + special_chars

    while True:
        password = "" #to store password
        for y in range(passlen.get()):
            password += ''.join(random.choice(all))
        if (any(char in special_chars for char in password) and sum(char in digits for char in password)>=2):
            break
    return output_pass.set(password)

#copy to clipboard function
def copyPass():
    pyperclip.copy(output_pass.get())

#Main Function
pass_head = Label(root, text = 'Password Length', font = 'arial 12 bold').pack(pady=10) #to generate label heading
 
passlen = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(root, from_ = 4, to_ = 32 , textvariable = passlen , width = 24, font='arial 16').pack()

#Generate password button
 
Button(root, command = randPassGen, text = "Generate Password", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
pass_label = Label(root, text = 'Random Generated Password', font = 'arial 12 bold').pack(pady="30 10")
Label(root , textvariable = output_pass, width = 25, font='arial 16').pack()
 
#Copy to clipboard button

Button(root, text = 'Copy to Clipboard', command = copyPass, font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)
 
root.mainloop()  #to bundle pack the code for tkinter