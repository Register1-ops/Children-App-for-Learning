import tkinter as tk # importing tkinter as tk so can use tk as abbreviation
from tkinter import messagebox # from the module tkinter, i import messagebox
import LivingThingsAndTheirHabitats
import Level3Maths


class Ages7To8():
    def __init__(self, userID):
        self.root = tk.Tk() # accessing Tkinter, in a variable root, so everything can be stored inside the root
        self.root["bg"] = "#adbd99" # create a background colour for the page
        self.menubar = tk.Menu(self.root) # creates a menu within the root of thr program
        self.root.geometry("800x800") # creates size of page
        self.root.title("Level 3") # creates the title of the page

        self.filemenu = tk.Menu(self.menubar, tearoff=0)  # accesses the menu bar creates
        self.filemenu.add_command(label="Close", command=self.on_closing) # adds a command to close the program
        self.filemenu.add_separator() # adds a seperator so both commands are not on top of each other
        self.filemenu.add_command(label="Close Without question", command=exit) # adds another command

        self.menubar.add_cascade(menu=self.filemenu, label="Close application")
        # the commands are under the cascade called close application, the commands are under the close application
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)


        # creates a button
        self.submit_button = tk.Button(self.root, text="Alphabet", font=("Arial", 20), command=self.Alphabet)
        # under the root, with the text called alphabet with the font being arial at size 20, when clicked on,
        # the function alphabet will be accessed and processed
        self.submit_button.place(x = 250, y=100) # places a button
        self.submit_button["bg"] = "#dbce45" # creates a button background colour

        # creates a button
        self.submit_button = tk.Button(self.root, text="Colours", font=("Arial", 20), command=self.LivingThingsAndTheirHabitat)
        # under the root, with the text called colours with the font being arial at size 20, when clicked on,
        # the function colours will be accessed and processed
        self.submit_button.place(x=100, y = 100) # places a button on the screen
        self.submit_button["bg"] = "#fbce45" # creates a button background colour

        # creates a button
        self.submit_button = tk.Button(self.root, text="Simple Maths", font=("Arial", 20), command=self.simpleMaths)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=400, y=100)
        self.submit_button["bg"] = "#dbce45"

        self.root.config(menu=self.menubar) # it configrates the menubar

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"): # if the messagbox was clicked
            self.root.destroy() # the program will close if clicked.
            print("Goodbye, see you later")

    def Alphabet(self):
        pass

    def simpleMaths(self):
        MathsForAges7to8.MathsAges7to8()

    def LivingThingsAndTheirHabitat(self):
        LivingThingsAndTheirHabitatsForAges7to8.LivingThingsAndTheirHabitat()

if __name__ == "__main__":
    Ages7To8(None)
