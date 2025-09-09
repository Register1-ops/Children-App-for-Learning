import tkinter as tk # importing tkinter as tk so can use tk as abbreviation
from tkinter import messagebox

import Level2Colours
import Level1Maths


class Ages5To6():
    def __init__(self, userID):
        self.root = tk.Tk() # accessing Tkinter, in a variable root, so everything can be stored inside the root
        self.root["bg"] = "#aeed99" # create a background colour for the page
        self.menubar = tk.Menu(self.root) # creates a menu within the root of thr program
        self.root.geometry("800x800") # creates size of page
        self.root.title("Level 2") # creates the title of the page

        self.filemenu = tk.Menu(self.menubar, tearoff=0)  # accesses the menu bar creates
        self.filemenu.add_command(label="Close", command=self.on_closing)  # adds a command to close the program
        self.filemenu.add_separator()  # adds a seperator so both commands are not on top of each other
        self.filemenu.add_command(label="Close Without question", command=exit)  # adds another command

        # creates a button
        self.submit_button = tk.Button(self.root, text="Alphabet", font=("Arial", 20), command=self.Alphabet)
        # under the root, with the text called alphabet with the font being arial at size 20, when clicked on,
        # the function alphabet will be accessed and processed
        self.submit_button.place(x=250, y=100)  # places a button
        self.submit_button["bg"] = "#dbce45"  # creates a button background colour

        # creates a button
        self.submit_button = tk.Button(self.root, text="Colours", font=("Arial", 20), command=self.Colours)
        # under the root, with the text called colours with the font being arial at size 20, when clicked on,
        # the function colours will be accessed and processed
        self.submit_button.place(x=100, y=100)  # places a button on the screen
        self.submit_button["bg"] = "#fbce45"  # creates a button background colour

        # creates a button
        self.submit_button = tk.Button(self.root, text=" Maths", font=("Arial", 20), command=self.Maths)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=400, y=100)
        self.submit_button["bg"] = "#dbce45"

        # creates a button
        self.submit_button = tk.Button(self.root, text="Punctuation", font=("Arial", 20), command=self.Alphabet)
        # under the root, with the text called punctuation with the font being arial at size 20, when clicked on,
        # the function punctuation will be accessed and processed
        self.submit_button.place(x=550, y=100)
        self.submit_button["bg"] = "#dbce45"

        self.root.config(menu=self.menubar)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagbox was clicked
            self.root.destroy()  # the program will close if clicked.

    def Alphabet(self):
        pass

    def Maths(self):
        MathsForAges5to6.MathsAges5to6()

    def Colours(self):
        ColoursForAges5To6.ColoursAges5To6()


if __name__ == "__main__":
    Ages5To6(None)

