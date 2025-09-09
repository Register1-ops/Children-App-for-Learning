import tkinter as tk
from functools import partial
from tkinter import messagebox
import sqlite3
from tkinter.ttk import Scrollbar

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pygame

import MainPage
import Login
from ScrollFrame import ScrollFrame


class OwnQuestions:

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/gypsy-jazz-guitar-relaxing-acoustic-nylon-guitar-141860.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.stop()

        self.ShowHideAnswerButton = []
        self.AnswerEntry = []
        self.YourOwnQuestions = []
        self.isAnswerShown = []

        # the section above creates empty lists

        self.BookNameList = []  # this initiates a list called BookNameList
        self.DateList = []  # this initiates a list called DataList
        self.SummaryList = []  # this initiates a list called SummaryList
        self.root = tk.Tk() # creates a root window and displays it on the screen
        self.root["bg"] = "#adbd99" # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("600x600") # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Own Questions") # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.
        # scrollbar = tk.Scrollbar(self.root, orient="vertical")
        # scrollbar.pack(sticky="ns")

        self.ScrollFrame = ScrollFrame(self.root)
        self.ScrollFrame.viewPort["bg"] = "#adbd99"
        self.ScrollFrame.canvas["bg"] = "#adbd99"
        self.ScrollFrame.pack(fill=tk.BOTH, expand=True, anchor="nw")



        self.row = 2  # initialises the variable row to 2 as well as making it a member variable so it can be accessed
        # throughout the module

        self.TableFrame = tk.Frame(self.ScrollFrame.viewPort)  # A frame is a widget that displays as a simple rectangle.
        # Typically, you use a frame to organize other widgets both visually and at the coding level.
        # Table Frame is a frame inside root so widgets can be changed just inside the frame
        self.TableFrame.pack(side = "left", fill = "both", expand = True)
        # the TableFrame is packed to the left side of the window that fills both the x and y axis

        self.FrameButton = tk.Frame(self.ScrollFrame.viewPort) # FrameButton is instantiated as Frame inside the root window
        self.FrameButton.pack(side="right", fill="both", expand=True)
        # the FrameButton is packed to the right side of the window screen and both the x and y axis are filled

        # both lines below create the background colour of both the Frames
        self.TableFrame["bg"] = "#abcc87"
        self.FrameButton["bg"] = "#abcc87"


        self.Question = tk.Label(self.TableFrame, text ="Question", font = ("Arial", 20))
        self.Question.grid(row=1, column = 0)
        # BookName is a Label widget with an arial font and a size of 20
        # Grid geometry manager puts the widgets in a 2-dimensional table, BookName is put in a specific row and column


        self.Answer = tk.Label(self.TableFrame, text="Answer", font=("Arial", 20))
        self.Answer.grid(row=1, column=2)
        # Summary is a Label widget with an arial font and a size of 20
        # Grid geometry manager puts the widgets in a 2-dimensional table, Summary is put in a specific row and column

        self.RetrieveData() # this calls the function RetrieveData
        self.EntryBoxes() # this calls the EntryBoxes function

        self.AddRowButton = tk.Button(self.FrameButton, text="Add Another Row", font=("Poor Richard", 16), command=self.EntryBoxes)
        self.AddRowButton.grid(row = 5, column = 5, padx = 50, pady =50)
        self.AddRowButton["bg"] = "#fabcd1"
        # Button widgets represent a clickable item in the applications, AddRow is a button that is in the root
        # that has the text of "Add another row". Once it is clicked it calls the function EntryBoxes
        # Grid geometry manager puts the widgets in a 2-dimensional table, AddRow is put in a specific row and column

        self.SaveButton = tk.Button(self.FrameButton, text="Save", font=("Poor Richard", 16), command=self.Save)
        self.SaveButton.grid(row=10, column=5, ipadx=50,pady=50)
        self.SaveButton["bg"] = "#fabcd1"
        # Button widgets represent a clickable item in the applications, Save is a button that is in the root
        # that has the text of "Save". Once it is clicked it calls the function Save
        # Grid geometry manager puts the widgets in a 2-dimensional table, Save is put in a specific row and column

        self.PrevPageButton = tk.Button(self.FrameButton, text="⬅️Previous Page", font=("Poor Richard", 16), command=self.PrevPage)
        self.PrevPageButton.grid(row=15, column=5)
        self.PrevPageButton["bg"] = "#fabcd1"
        # Button widgets represent a clickable item in the applications, Save is a button that is in the root
        # that has the text of "Save". Once it is clicked it calls the function Save
        # Grid geometry manager puts the widgets in a 2-dimensional table, Save is put in a specific row and column

        self.root.config(menu=self.menubar)
        # root.config (menu=self.menubar is then used to "draw" the Menu object on
        # our window. This results in a cascading menu at the top of the screen where each option in the menu allows us
        # to change the font size of a label object.'

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?",message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidentally,
        # the page will close and be destroyed.



    def EntryBoxes(self, TheirOwnQuestions="", Answer=""):  # passes in the respective parameters,
        # the parameters are. the given parameters are set to nothing, just incase the function is called accidently,
        # the respective parameters will hold a value, even though the value is nothing, it still holds a value and
        # the program won't break

        # Keyword arguments. I am doing it "normally" like
        # def my_function(arg1, arg2)
        # where they are called Positional Arguments.
        # When you call it, you have to pass in both arguments in the right order, like:
        # my_function(value1, value2)
        # Keyword arguments on the other hand are handled using their name. So you define it like:
        # def my_function(arg1=default1, arg2=default2)
        # And then you can call it like:
        # my_function(arg1=value1, arg2=value2)
        # But you can also call it like:
        # my_function(arg2=value2)
        # i.e. only provide one of the arguments. `arg1` will just be treated as though you passed in
        # the default value i set (i.e. `default1` in the definition above), but `arg2` will take the value of
        # `value2` that you passed in. Since it has no positional arguments, i can actually just call it without
        # any arguments as well if you're just using the defaults:
        # my_function()
        # Which is what i have done with my function to add an entry row to the book log
        # I can use both positional and keyword arguments at the same time,
        # but the positional ones have to appear before the keyword ones
        # def my_function(arg1, arg2, arg3=default1, arg4=default2)
        # Then when you call it, I have to provide all the positional arguments in the right order,
        # i.e. the minimum you can pass it is
        # my_function(value1, value2)
        # But then you can also pass keyword arguments like
        # my_function(value1, value2, arg4=value4)


        self.row += 1 # self.row is assigned above with the value 2, here the self.row variable will increment by
        # 1 each time this function is called
        # since self.row is a member variable of the class, it can be changed throughout the code and saved
        # throughout the code, since i am only using it in this function, i don't need to make it just a local variable
        self.YourOwnQuestions.append(tk.Entry(self.TableFrame, width= 30, ))
        self.YourOwnQuestions[-1].grid(row = self.row, column = 0)
        # The Entry widget allows you to enter a sing-line text.
        # The BookNameEntry is within the root window and has a width of 30
        # It is then gridded with an incrementing row each time since the row will need to be
        # underneath each other, not over each other
        self.YourOwnQuestions[-1].insert(0, TheirOwnQuestions)

        self.ShowHideAnswerButton.append(tk.Button(self.TableFrame, text = "Show Answer", width = 30, command = partial(self.ShowHideAnswer, self.row-3)))
        self.ShowHideAnswerButton[-1].grid(row = self.row, column = 2)


        self.AnswerEntry.append(tk.Entry(self.TableFrame, show = "*", width=30))
        self.AnswerEntry[-1].grid(row=self.row, column=1)
        # The Entry widget allows you to enter a sing-line text.
        # The SummaryEntry is within the root window and has a width of 30
        # It is then gridded with an incrementing row each time since the row will need to be
        # underneath each other, not over each other
        self.AnswerEntry[-1].insert(0, Answer)
        self.AnswerEntry[-1].config(state = tk.DISABLED)

        self.isAnswerShown.append(False)


    def Save(self):
        userID = Login.getUserID() # This line gets the userID of the user that has logged into the account
        array = [] # sets a local variable, array, to an empty list



        for item in range(0, len(self.YourOwnQuestions)): # since the length of all the lists above are going to be the
            # same length, this means that i can access the lists with the same for loop of the same length
            # i chose BookNameList since it is the first list that i made

            OwnQuestions = self.YourOwnQuestions[item].get() # for a given index inside the list, BookNameList,
            # i get the text that the user has inputted into the entry box


            # The second line constructs a string to represent that date, to be stored in the database
            # The way i am doing it is with a String Interpolation,
            # where i am passing in python variables to specific parts of the string,
            # rather than having to go `"this thing" + "that thing" + "this other thing"` etc.
            # - it mostly just makes the code a lot more readable/harder to make a mistake


            Answer = self.AnswerEntry[item].get()
            # for a given index inside the list, SummaryList,
            # i get the text that the user has inputted into the entry box

            if OwnQuestions != "" or Answer != "":
                array.append((userID, item,OwnQuestions, Answer)) # this appends the values inside the tuple
            # to the list called array, so the values can be stored as list within a list so the values can be
            # accessed

        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database

        cursor.execute("""DELETE FROM OwnQuestions
        WHERE userId = ?
        """, (userID,))
        # this query deletes a record from the table BookLog where the userID is given in the variable userID


        for items in array: # for each value inside the list called array
            cursor.execute("""INSERT INTO OwnQuestions (userID, questionNo, TheirOwnQuestions, Answer)
            VALUES (?, ?, ?, ?)
            """,(items[0], items[1], items[2], items[3]))
            # the query that is executed is where the values that are in the 1 tuple of the array is accessed
            # by accessing the individual indexes as inserted into the table BookLog, into the respective fields

        conn.commit() # this commits the changes to the database that have been made, if there have been any changes
        conn.close() # closes the database so that it cant be edited and changed

    def RetrieveData(self):
        userID = Login.getUserID() # the userID is obtained from the Login module

        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database

        cursor.execute("""SELECT TheirOwnQuestions, Answer
        FROM OwnQuestions
        WHERE userID = ?
        ORDER BY questionNo
        """, (userID,))
        # the query selects the respective fields from the BookLog database where the userID is given by the account
        # that has been accessed. This is then ordered by entry number, so the fields can be outputted in order
        # the same order the user has inputted the values

        rows = cursor.fetchall()  # the variable row stores all the values in the respective fields that have
        # been obtained in database

        for items in rows:  # for each item in rows, which rows stores a tuple of the respective fields
            self.EntryBoxes(TheirOwnQuestions=items[0], Answer=items[1])
            # the EntryBoxes function is called passing the bookName, the dateRead and the summary as parameters



    def ShowHideAnswer(self, index):
        if not self.isAnswerShown[index]:  # if isPasswordShown not equal to True
            self.AnswerEntry[index].config(show="", state = tk.NORMAL)  # password will be set to the actual letters the user has entered
            # entered, so that the user can see if their password and confirm password are the same
            self.ShowHideAnswerButton[index].config(text="Hide Password")  # changes the button to say Hide password
        else:
            self.AnswerEntry[index].config(show="*", state = tk.DISABLED)
            # the password is set to an asterisk so that the password can be kept safe
            self.ShowHideAnswerButton[index].config(text="Show Password")  # changes the button to say show password

        self.isAnswerShown[index] = not self.isAnswerShown[index]
        # changes the isPasswordShown to the opposite boolean value
        # e.g. from True to False, so that the next time, the section of code that will be run will be the other
        # section from the previous section and would be the right section respective to the show and hide password

    def PrevPage(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        MainPage.LevelOptions()


if __name__ == "__main__":
    OwnQuestions()
