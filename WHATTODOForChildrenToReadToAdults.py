# add sentences and words so that children can learn their vocab
# add a button so that words can be taken off the list
# two buttons, (they said it, they didn't say it correctly)
# add 1 to each variable so that when they get to 5, a notification pops up saying, you know the word, well done
# you can now use it


# add books you have read to keep a log
# what pages you have read


import json
import tkinter as tk
from tkinter import messagebox
from functools import partial
import random


class What:

    def __init__(self):
        self.countCorrect = 0 # initialises countCorrect to 0 as the amount of questions answered correctly right
        # now is 0
        self.countWrong = 0 # initialises countWrong to 0 as the amount of questions answered correctly right now is 0
        self.QuestionUsed = [] # creates a list to store which questions have been used
        self.WrongQuestions = [] # creates a list of the questions the user got wrong
        self.root = tk.Tk()
        self.root["bg"] = "#adbd99" # creates a background colour
        self.menubar = tk.Menu(self.root)
        self.root.geometry("800x800") # initialises the screen size, 800 pixels by 800 pixels
        self.root.title("What to do") # creates the page title

        with open("Level2MathsQuestions.json", "r") as infile: # opens file, then closes file without needing to type code to do so
            self.questions = json.load(infile)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)  # accesses the menu bar creates
        self.filemenu.add_separator()  # adds a seperator so both commands are not on top of each other
        self.filemenu.add_command(label="Close Without question", command=exit)  # adds another command
        self.menubar.add_cascade(menu=self.filemenu, label="Close application")


        self.root.config(menu=self.menubar)
        self.root.mainloop()


if __name__ == "__main__":
    What()
