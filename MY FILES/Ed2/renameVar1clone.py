import random
import string
from tkinter import *

def badpassword():
	passkey = string.ascii_lowercase
	print(''.join(random.choice(passkey) for i in range(4)))  # function uses for loop to create a random bad password
	
def goodpassword():
	passkey = string.ascii_letters + string.digits
	print(''.join(random.choice(passkey) for i in range(6)))  # function uses for loop to create a random good password

def greatpassword():
	passkey = string.ascii_letters + string.digits + string.punctuation
	print(''.join(random.choice(passkey) for i in range(12))) # function uses for loop to create a random great password

# GUI made with Tkinter

roots = Tk()



badPasswordButton = Button(roots, text="Generate bad password", command=badpassword, padx=53) # generates the button that creates a bad passoword
badPasswordButton.pack()

goodPasswordButton = Button(roots, text="Generate good strength password", command=goodpassword, padx=21) # generates the button that creates a good strength passoword
goodPasswordButton.pack()

greatPasswordButton = Button(roots, text="Generate great password", command=greatpassword, padx=50) # generates the button that creates a great passoword
greatPasswordButton.pack()

roots.mainloop()
