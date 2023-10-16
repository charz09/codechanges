import random
import string
from tkinter import *
def weakpassword():
	password = string.ascii_lowercase
	print(''.join(random.choice(password) for i in range(4)))  # function uses for loop to generate a random strong password
def mediumpassword():
	password = string.ascii_letters + string.digits
	print(''.join(random.choice(password) for i in range(6)))  # function uses for loop to generate a random weak password
def strongpassword():
	password = string.ascii_letters + string.digits + string.punctuation
	print(''.join(random.choice(password) for i in range(12))) # function uses for loop to generate a random strong password
root = Tk()
weakPasswordButton = Button(root, text="Generate weak password", command=weakpassword, padx=53) # creates the button that generates a weak passoword
weakPasswordButton.pack()
mediumPasswordButton = Button(root, text="Generate medium strength password", command=mediumpassword, padx=21) # creates the button that generates a medium strength passoword
mediumPasswordButton.pack()
strongPasswordButton = Button(root, text="Generate strong password", command=strongpassword, padx=50) # creates the button that generates a strong passoword
strongPasswordButton.pack()
root.mainloop()





