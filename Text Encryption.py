"""

Text Encryption

Purpose: Encrypts text using a very simple encryption
Programer: ExcaliburZero / Rocketslime_1_1

"""
#Imports
from tkinter import *

#Encrypt Text Function
def encrypt():

    #Grab input and make a list with each character
    to_be_encrypted = list(input_text.get(1.0, END))

    #Encrypt text
    current = 0
    for letter in to_be_encrypted:
        if letter == "a":
            to_be_encrypted[current] = "u"
        if letter == "b":
            to_be_encrypted[current] = "s"
        if letter == "c":
            to_be_encrypted[current] = "t"
        if letter == "d":
            to_be_encrypted[current] = "z"
        if letter == "e":
            to_be_encrypted[current] = "r"
        if letter == "f":
            to_be_encrypted[current] = "v"
        if letter == "g":
            to_be_encrypted[current] = "p"
        if letter == "h":
            to_be_encrypted[current] = "w"
        if letter == "i":
            to_be_encrypted[current] = "q"
        if letter == "j":
            to_be_encrypted[current] = "x"
        if letter == "k":
            to_be_encrypted[current] = "o"
        if letter == "l":
            to_be_encrypted[current] = "y"
        if letter == "m":
            to_be_encrypted[current] = "n"
        if letter == "n":
            to_be_encrypted[current] = "m"
        if letter == "o":
            to_be_encrypted[current] = "k"
        if letter == "p":
            to_be_encrypted[current] = "g"
        if letter == "q":
            to_be_encrypted[current] = "i"
        if letter == "r":
            to_be_encrypted[current] = "e"
        if letter == "s":
            to_be_encrypted[current] = "b"
        if letter == "t":
            to_be_encrypted[current] = "c"
        if letter == "u":
            to_be_encrypted[current] = "a"
        if letter == "v":
            to_be_encrypted[current] = "f"
        if letter == "w":
            to_be_encrypted[current] = "h"
        if letter == "x":
            to_be_encrypted[current] = "j"
        if letter == "y":
            to_be_encrypted[current] = "l"
        if letter == "z":
            to_be_encrypted[current] = "d"
        current = current + 1
    
    #Put together output
    output = "".join(to_be_encrypted)

    #Output template code
    output_text.insert(END, output)

    return

#Generate GUI
theGUI = Tk()
theGUI.geometry("435x350+200+200")
theGUI.title("Text Encryption")

#Setup input variable
to_be_encrypted = StringVar()

#Setup labels
label_intro = Label(theGUI, text="Welcome to the Text Encryption Program").grid(row = 0, columnspan = 2)
label_input = Label(theGUI, text="Input:").grid(row = 1, column = 0)
label_output = Label(theGUI, text="Output:").grid(row = 1, column = 1)

#Setup input and output boxes
input_text = Text(theGUI, height = 16, width = 30)
input_text.grid(row = 2, column = 0)
output_text = Text(theGUI, height = 16, width = 30)
output_text.grid(row = 2, column = 1)

#Setup button
button_generate = Button(theGUI, text = "Encrypt", command = encrypt).grid(row = 3, column = 0)

#Add GUI to main loop
theGUI.mainloop()
