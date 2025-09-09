import tkinter as tk # importing tkinter as tk so can use tk as abbreviation
from tkinter import messagebox # from the module tkinter, i import messagebox

import MainPage
import Grammar
import OwnQuestions
import StartButtonForQuiz
import WHATTODOForChildrenToReadToAdults


class OtherLevelOptions():
    def __init__(self, userID):
        self.root = tk.Tk() # accessing Tkinter, in a variable root, so everything can be stored inside the root
        self.root["bg"] = "#adbd99" # create a background colour for the page
        self.menubar = tk.Menu(self.root) # creates a menu within the root of thr program
        self.root.geometry("2000x2000") # creates size of page
        self.root.title("Options") # creates the title of the page

        self.filemenu = tk.Menu(self.menubar, tearoff=0)  # accesses the menu bar creates
        self.filemenu.add_command(label="Close", command=self.on_closing) # adds a command to close the program
        self.filemenu.add_separator() # adds a seperator so both commands are not on top of each other
        self.filemenu.add_command(label="Close Without question", command=exit) # adds another command

        self.menubar.add_cascade(menu=self.filemenu, label="Close application")
        # the commands are under the cascade called close application, the commands are under the close application

        # create text box labels
        self.level1_label = tk.Label(self.root, text="Other", font = ("Arial",25))
        self.level1_label.place(x=600, y=75)
        # creates a coloured label
        self.level1_label["bg"] = "#fead90"


        # creates a button
        self.submit_button = tk.Button(self.root, text="Grammar", font=("Arial", 17), command=self.Grammar)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=600, y=150)
        self.submit_button["bg"] = "#dbce45"

        # creates a button
        self.submit_button = tk.Button(self.root, text="Book Log", font=("Arial", 17), command=self.BookLog)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=600, y=300)
        self.submit_button["bg"] = "#dbce45"

        # creates a button
        self.submit_button = tk.Button(self.root, text="Own Questions", font=("Arial", 17), command=self.OwnQuestions)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=600, y=225)
        self.submit_button["bg"] = "#dbce45"

        # creates a button
        self.submit_button = tk.Button(self.root, text="⬅️Previous Page", font=("Arial", 17), command=self.PrevPage)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.submit_button.place(x=2, y=500)
        self.submit_button["bg"] = "#dbce45"

        self.root.config(menu=self.menubar) # it configurates the menubar

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"): # if the messagebox was clicked
            self.root.destroy() # the program will close if clicked.
            print("Goodbye, see you later")

    def Grammar(self):
        StartButtonForQuiz.StartButton(10)

    def PrevPage(self):
        self.root.destroy()
        MainPage.LevelOptions()

    def BookLog(self):
        StartButtonForQuiz.StartButton(11)

    def OwnQuestions(self):
        StartButtonForQuiz.StartButton(12)


if __name__ == "__main__":
    OtherLevelOptions(None)
