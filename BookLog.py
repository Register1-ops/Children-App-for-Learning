import datetime
import tkinter as tk
from tkinter import messagebox

import pygame
import tkcalendar
import sqlite3
import MainPage
import Login
from PIL import ImageTk, Image

from ScrollFrame import ScrollFrame


class BookLog:

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/gypsy-jazz-guitar-relaxing-acoustic-nylon-guitar-141860.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        self.BookNameList = []  # this initiates a list called BookNameList
        self.DateList = []  # this initiates a list called DataList
        self.SummaryList = []  # this initiates a list called SummaryList
        self.root = tk.Tk() # creates a root window and displays it on the screen
        self.root["bg"] = "#adbd99" # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("1000x700") # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Book Log") # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.

        self.row = 2  # initialises the variable row to 2 as well as making it a member variable so it can be accessed
        # throughout the module

        self.TableFrame = ScrollFrame(self.root)  # A frame is a widget that displays as a simple rectangle.
        # Typically, you use a frame to organize other widgets both visually and at the coding level.
        # Table Frame is a frame inside root so widgets can be changed just inside the frame
        self.TableFrame.pack(side = "left", fill = "both", expand = True, anchor="nw")
        # the TableFrame is packed to the left side of the window that fills both the x and y-axis

        self.TableFrame.viewPort["bg"] = "#adbd99"
        self.TableFrame.canvas["bg"] = "#adbd99"
        #self.TableFrame.pack(fill=tk.BOTH, expand=True, anchor="nw")

        self.FrameButton = tk.Frame(self.root) # FrameButton is instantiated as Frame inside the root window
        self.FrameButton.pack(side="right", fill="both", expand=True)
        # the FrameButton is packed to the right side of the window screen and both the x and y-axis are filled

        # both lines below create the background colour of both the Frames
        self.TableFrame["bg"] = "#abcc87"
        self.FrameButton["bg"] = "#abcc87"




        self.width = 300
        self.height = 300

        self.imageRaw = Image.open("Pictures for project/pexels-photo-3358707.jpeg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        # this creates the image
        self.imgpanel = tk.Label(self.FrameButton, width=self.width, height=self.height, image=self.img)
        # anel.grid(row=9)
        self.imgpanel.place(x=1, y=1)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw2 = Image.open("Pictures for project/pexels-maël-balland-3457273.jpg")
        # this opens the specific image in the folder named
        self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        # this creates the image
        self.imgpanel2 = tk.Label(self.FrameButton, width=self.width, height=self.height, image=self.img2)
        # anel.grid(row=9)
        self.imgpanel2.place(x=1, y=300)
        # CreateImage =  panel.create_image(width,height,image = img)



        self.BookName = tk.Label(self.TableFrame.viewPort, text = "Book Name", font = ("Arial",20))
        self.BookName.grid(row=1, column = 0)
        # BookName is a Label widget with an arial font and a size of 20
        # Grid geometry manager puts the widgets in a 2-dimensional table, BookName is put in a specific row and column

        self.Date = tk.Label(self.TableFrame.viewPort, text="Date", font=("Arial", 20))
        self.Date.grid(row=1, column=1)
        # Date is a Label widget with an arial font and a size of 20
        # Grid geometry manager puts the widgets in a 2-dimensional table, Date is put in a specific row and column

        self.Summary = tk.Label(self.TableFrame.viewPort, text="Summary", font=("Arial", 20))
        self.Summary.grid(row=1, column=2)
        # Summary is a Label widget with an arial font and a size of 20
        # Grid geometry manager puts the widgets in a 2-dimensional table, Summary is put in a specific row and column

        self.RetrieveData() # this calls the function RetrieveData
        self.EntryBoxes() # this calls the EntryBoxes function

        self.AddRow = tk.Button(self.FrameButton, text="Add Another Row", font=("Poor Richard", 16), command=self.EntryBoxes)
        self.AddRow.grid(row = 5, column = 15, padx = 100, pady = 100)
        self.AddRow["bg"] = "#fabcd1"
        # Button widgets represent a clickable item in the applications, AddRow is a button that is in the root
        # that has the text of "Add another row". Once it is clicked it calls the function EntryBoxes
        # Grid geometry manager puts the widgets in a 2-dimensional table, AddRow is put in a specific row and column

        self.Save = tk.Button(self.FrameButton, text="Save", font=("Poor Richard", 16), command=self.Save)
        self.Save.grid(row=10, column=15, padx= 100, pady=100)
        self.Save["bg"] = "#fabcd1"
        # Button widgets represent a clickable item in the applications, Save is a button that is in the root
        # that has the text of "Save". Once it is clicked it calls the function Save
        # Grid geometry manager puts the widgets in a 2-dimensional table, Save is put in a specific row and column

        self.PrevPageButton = tk.Button(self.FrameButton, text="⬅️Previous Page", font=("Poor Richard", 16),
                                       command=self.PrevPage)
        self.PrevPageButton.grid(row=15, column=15)
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
        # and no since the user may have clicked on the exit button accidently,
        # the page will close and be destroyed.

    def EntryBoxes(self, bookName="", dateRead="", summary=""):  # passes in the respective parameters,
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



        if dateRead == "":  # if the variable dateRead has no value inside it
            date = datetime.datetime.now() # the variable date will hold the date that it is now
            # datetime.datetime.now () function returns datetime object containing current date
            # and time of the system during the execution of now () statement.
            dateRead = f"{date.month}/{date.day}/{date.year}"
            # the date is stored in the variable dateRead
            # the way this stored in the way so that e.g. date.month and date.day are python actions that get
            # the respective month, day and year in the brackets and allowing the string value of the forward
            # slash to be inbetween the month, day and year


        self.row+= 1 # self.row is assigned above with the value 2, here the self.row variable will increment by
        # 1 each time this function is called
        # since self.row is a member variable of the class, it can be changed throughout the code and saved
        # throughout the code, since i am only using it in this function, i don't need to make it just a local variable
        BookNameEntry = tk.Entry(self.TableFrame.viewPort, width= 30, )
        BookNameEntry.grid(row = self.row, column = 0 )
        # The Entry widget allows you to enter a sing-line text.
        # The BookNameEntry is within the root window and has a width of 30
        # It is then gridded with an incrementing row each time since the row will need to be
        # underneath each other, not over each other
        BookNameEntry.insert(0,bookName)

        Date = dateRead.split("/")
        print(Date)
        DateEntry = tkcalendar.DateEntry(self.TableFrame.viewPort, width=12, background='darkblue',
                        foreground='white', borderwidth=2, month=int(Date[0]), day=int(Date[1]) , year=int(Date[2]))
        DateEntry.grid(row = self.row, column = 1)


        SummaryEntry = tk.Entry(self.TableFrame.viewPort, width=30)
        SummaryEntry.grid(row=self.row, column=2, padx=2, pady=1)
        # The Entry widget allows you to enter a sing-line text.
        # The SummaryEntry is within the root window and has a width of 30
        # It is then gridded with an incrementing row each time since the row will need to be
        # underneath each other, not over each other
        SummaryEntry.insert(0, summary)

        self.BookNameList.append(BookNameEntry)
        # the values that are in all the BookNameEntry are appended to the list BookNameList
        self.DateList.append(DateEntry)
        # the values that are in all the DateEntry are appended to the list DataList
        self.SummaryList.append(SummaryEntry)
        # the values that are in all the SummaryEntry are appended to the list SummaryList


    def Save(self):
        userID = Login.getUserID() # This line gets the userID of the user that has logged into the account
        array = [] # sets a local variable, array, to an empty list

        for item in range(0, len(self.BookNameList)): # since the length of all the lists above are going to be the
            # same length, this means that i can access the lists with the same for loop of the same length
            # i chose BookNameList since it is the first list that i made

            BookName = self.BookNameList[item].get() # for a given index inside the list, BookNameList,
            # i get the text that the user has inputted into the entry box
            dateObject : datetime.date = self.DateList[item].get_date()
            Date = f"{dateObject.month}/{dateObject.day}/{dateObject.year}"
            # The first one gets the date from the given row (at index `item`) as a `datetime.date` object -
            # this is just an object that contains the info about the date. The bit between the colon (inclusive) and
            # equals sign is called a "type hint" or a "type annotation". the reason I  added it was
            # to make sure that it exists and is really useful, and b. PyCharm
            # was having a hard time inferring the type itself - part of the reason type
            # hints are really useful is that it can help your tooling to know what type something should be, and
            # therefore give you better autocomplete suggestions and flag up potential bugs caused from misusing a
            # given type/the wrong type)
            # The second line constructs a string to represent that date, to be stored in the database
            # The way i am doing it is with a String Interpolation,
            # where i am passing in python variables to specific parts of the string,
            # rather than having to go `"this thing" + "that thing" + "this other thing"` etc.
            # - it mostly just makes the code a lot more readable/harder to make a mistake


            Summary = self.SummaryList[item].get()
            # for a given index inside the list, SummaryList,
            # i get the text that the user has inputted into the entry box

            if BookName != "" or  Summary != "":
                array.append((userID, item,BookName, Date, Summary)) # this appends the values inside the tuple
            # to the list called array, so the values can be stored as list within a list so the values can be
            # accessed

        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database

        cursor.execute("""DELETE FROM BookLog
        WHERE userId = ?
        """, (userID,))
        # this query deletes a record from the table BookLog where the userID is given in the variable userID


        for items in array: # for each value inside the list called array
            cursor.execute("""INSERT INTO BookLog (userID, entryNo, BookName, dateRead, Summary)
            VALUES (?, ?, ?, ?, ?)
            """,(items[0], items[1], items[2], items[3], items[4]))
            # the query that is executed is where the values that are in the 1 tuple of the array is accessed
            # by accessing the individual indexes as inserted into the table BookLog, into the respective fields

        conn.commit() # this commits the changes to the database that have been made, if there have been any changes
        conn.close() # closes the database so that it cant be edited and changed

    def RetrieveData(self):
        userID = Login.getUserID() # the userID is obtained from the Login module

        conn = sqlite3.connect("address_book.db")  # connects to the address book database
        cursor = conn.cursor()  # allows a cursor to be used so items can be accessed from the database

        cursor.execute("""SELECT BookName, dateRead, Summary
        FROM BookLog
        WHERE userID = ?
        ORDER BY entryNo
        """, (userID,))
        # the query selects the respective fields from the BookLog database where the userID is given by the account
        # that has been accessed. This is then ordered by entry number, so the fields can be outputted in order
        # the same order the user has inputted the values

        rows = cursor.fetchall()  # the variable row stores all the values in the respective fields that have
        # been obtained in database

        for items in rows:  # for each item in rows, which rows stores a tuple of the respective fields
            self.EntryBoxes(bookName=items[0], dateRead=items[1], summary=items[2])
            # the EntryBoxes function is called passing the bookName, the dateRead and the summary as parameters

    def PrevPage(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        MainPage.LevelOptions()


if __name__ == "__main__":
    Login.verification("test123", "test12345")
    BookLog()