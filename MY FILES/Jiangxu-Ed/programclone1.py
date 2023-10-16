import random
import string
from tkinter import *



def goodpassword():
	password = string.ascii_letters + string.digits
	print(''.join(random.choice(password) for i in range(6)))  # function uses for loop to create a random good password

def badpassword():
	password = string.ascii_lowercase
	print(''.join(random.choice(password) for i in range(4)))  # function uses for loop to create a random bad password

def greatpassword():
	password = string.ascii_letters + string.digits + string.punctuation
	print(''.join(random.choice(password) for i in range(12))) # function uses for loop to create a random great password

# GUI made with Tkinter

root = Tk()



goodPasswordButton = Button(root, text="Generate good strength password", command=goodpassword, padx=21) # generates the button that creates a good strength passoword
goodPasswordButton.pack()

badPasswordButton = Button(root, text="Generate bad password", command=badpassword, padx=53) # generates the button that creates a bad passoword
badPasswordButton.pack()

greatPasswordButton = Button(root, text="Generate great password", command=greatpassword, padx=50) # generates the button that creates a great passoword
greatPasswordButton.pack()

root.mainloop()
