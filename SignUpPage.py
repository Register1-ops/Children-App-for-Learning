import tkinter as tk
from tkinter import messagebox
from tkinter import *
import sqlite3

import pygame

#from PIL import ImageTk, Image
import getHashPassword
import TKINTER

class SignUpPage1():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/stomping-rock-four-shots-111444.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.stop()
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("1000x700")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Start Button")  # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.

        self.filemenus = tk.Menu(self.menubar, tearoff=0)
        # The tk.Menu widget allows you to add a menubar to the main window (tk.Tk) or to a child window
        # tear-off allows you to detach menus for the most window, resulting in floating menus. When you click a
        # top menu item after creating a menu, you may notice dotted lines at the top. To remedy this, set tearoff to 0
        # at the time of menu declaration.
        self.filemenus.add_command(label="Close", command=self.on_closing)
        # add a menu item to the menu to close the program by calling the on_closing function
        self.filemenus.add_separator()
        # adds a seperator so that both the command on the menubar can be seen
        self.filemenus.add_command(label="Close Without question", command=exit)
        # creates a command called close without question which exits the program without asking the user
        # whether they want to
        self.menubar.add_cascade(menu=self.filemenus, label = "Close application")
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)

        # configures the menu menubar so that the menu bar actually appears on the screen
        self.root.config(menu=self.menubar)


        # create text boxes, entry boxes within the root window with a certain width
        # the entry box is then placed in a certain place based on a given x and y coordinate since the page
        # is like a graph


        self.firstname = tk.Entry(self.root, width= 30)
        self.firstname.place(x = 250, y = 150)

        # create text boxes, entry boxes within the root window with a certain width
        # the entry box is then placed in a certain place based on a given x and y coordinate since the page
        # is like a graph
        self.surname = tk.Entry(self.root, width=30)
        self.surname.place(x=250, y=250)

        # create text boxes, entry boxes within the root window with a certain width
        # the entry box is then placed in a certain place based on a given x and y coordinate since the page
        # is like a graph
        self.user_name = tk.Entry(self.root,width=30)
        self.user_name.place(x = 250, y=350)

        # create text boxes, entry boxes within the root window with a certain width
        # the entry box is then placed in a certain place based on a given x and y coordinate since the page
        # is like a graph
        self.stringVarPassword = tk.StringVar()
        self.stringVarPassword.trace_add("write", self.charPassword)
        self.password = tk.Entry(self.root,show = "*", width=30, textvariable=self.stringVarPassword)
        self.password.place(x = 250, y=450)

        # create text boxes, entry boxes within the root window with a certain width
        # the entry box is then placed in a certain place based on a given x and y coordinate since the page
        # is like a graph
        self.confirmPassword = tk.Entry(self.root, show = "*", width=30)
        self.confirmPassword.place(x=250, y=550)

        #create text box labels
        # Label is a Label widget
        # creates a label called First Name
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        self.firstname_label = tk.Label(self.root, text="First Name")
        self.firstname_label.place(x=100, y=150)
        self.firstname_label["bg"] = "#aead90"
        # this label is also given a specific background colour

        # Label is a Label widget
        # creates a label called Surname
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        self.surname_label = tk.Label(self.root, text="Surname")
        self.surname_label.place(x=100, y=250)
        self.surname_label["bg"] = "#aead90"
        # this label is also given a specific background colour

        # Label is a Label widget
        # creates a label called description_label
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        # this label is also given a specific background colour
        self.description_label = tk.Label(self.root, text="Create a username and password: ", font = ("Arial", 15))
        self.description_label.place(x=225, y=25)
        self.description_label["bg"] = "#edad90"

        # Label is a Label widget
        # creates a label called user_name_label
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        self.user_name_label = tk.Label(self.root, text="Create User Name")
        self.user_name_label.place(x=100, y=350)
        self.user_name_label["bg"] = "#aead90" #
        # this label is also given a specific background colour

        # Label is a Label widget
        # creates a label called password_label
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        self.password_label = tk.Label(self.root, text="Create Password")
        self.password_label.place(x=100, y=450)
        self.password_label["bg"] = "#aead90" # # this label is also given a specific background colour

        # Label is a Label widget
        # creates a label called ConfirmPassword_label
        # the label is also placed in a certain place inside the window since the window is
        # like a graph with a y and x axis
        self.Confirmpassword_label = tk.Label(self.root, text="Confirm Password")
        self.Confirmpassword_label.place(x=100, y=550)
        self.Confirmpassword_label["bg"] = "#aead90" # # this label is also given a specific background colour

        # creates a button
        # it has the text Show Password
        # when it is clicked it will call the function ShowHidPassword
        self.showPasswordBut = tk.Button(self.root, text="Show Password", font=("Arial", 12), command=self.ShowHidePassword)
        self.showPasswordBut.place(x=550, y=500)

        self.isPasswordShown = False  # sets the member variable isPasswordShown to false
        # it is a member variable so that the variable can be accessed throughout the program
        # sets isPasswordShown to False since the password is not shown yet

        # creates a button
        # it has the text Submit
        # when it is clicked it will call the function submit
        self.submit_button = tk.Button(self.root, text = "Submit", font=("Arial",14), command= self.submit)
        self.submit_button.place(x=800, y=150)
        self.submit_button["bg"] = "#edab47" # # it has a specific background colour

        self.NextPage = tk.Button(self.root, text="⬅️Previous page", font=("Arial", 15), command = self.PreviousPage)
        self.NextPage.place(x=800, y=45)
        self.NextPage["bg"] = "#abcd56"
        # this creates a button inside the root which when pressed calls the PreviousPage function
        # then the button is placed in a specific location within the page

        self.checkCharFrame = tk.Frame(self.root)
        self.checkCharFrame.place(x=725, y=475)
        self.checkCharFrame["bg"] = "#aabbdd"

        self.checkBoxlengthValue = tk.IntVar()
        self.checkBoxlengthPasswordCheckButton = tk.Checkbutton(self.checkCharFrame, state=tk.DISABLED, variable=self.checkBoxlengthValue)
        self.checkBoxlengthPasswordCheckButton.grid(row=3, column=1)
        self.checkBoxlengthPasswordCheckButton["bg"] = "#aabbdd"

        self.checkBoxlengthPasswordLabel = tk.Label(self.checkCharFrame, text="Length of at least 10 characters", font=("Ebrima",12))
        self.checkBoxlengthPasswordLabel.grid(row=3, column=2)
        self.checkBoxlengthPasswordLabel["bg"] = "#aabbdd"

        self.checkBoxAlphabetValue = tk.IntVar()
        self.checkBoxAlphabetChar = tk.Checkbutton(self.checkCharFrame, state=tk.DISABLED, variable=self.checkBoxAlphabetValue)
        self.checkBoxAlphabetChar.grid(row=1, column=1)
        self.checkBoxAlphabetChar["bg"] = "#aabbdd"

        self.checkAlphabetLabel = tk.Label(self.checkCharFrame, text="8 Letters of the Alphabet", font=("Ebrima",12))
        self.checkAlphabetLabel.grid(row=1, column=2)
        self.checkAlphabetLabel["bg"] = "#aabbdd"

        self.checkBoxSpecialValue = tk.IntVar()
        self.checkBoxSpecialChar = tk.Checkbutton(self.checkCharFrame, state=tk.DISABLED, variable=self.checkBoxSpecialValue)
        self.checkBoxSpecialChar.grid(row=2, column=1)
        self.checkBoxSpecialChar["bg"] = "#aabbdd"

        self.checkSpecialCharLabel = tk.Label(self.checkCharFrame, text="At least two special characters", font=("Ebrima",12))
        self.checkSpecialCharLabel.grid(row=2, column=2)
        self.checkSpecialCharLabel["bg"] = "#aabbdd"



        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidentally,
        # the page will close and be destroyed.


    def charPassword(self, *args):
        lengthPassword, alphabetPassword, specialCharPassword, theSame, inputted = self.checkPasswordChar()

        if lengthPassword:
            self.checkBoxlengthValue.set(1)
        else:
            self.checkBoxlengthValue.set(0)

        if alphabetPassword:
            self.checkBoxAlphabetValue.set(1)
        else:
            self.checkBoxAlphabetValue.set(0)

        if specialCharPassword:
            self.checkBoxSpecialValue.set(1)
        else:
            self.checkBoxSpecialValue.set(0)


    def checkPasswordChar(self):
        # this section of code gets the text that is in all the entry boxes and stored in the respective variables
        length = True
        alphabet = True
        special = True
        theSame = True
        inputted = True

        lowerCaseChar = 0
        upperCaseChar = 0
        specialCaseChar = 0

        PlainTextSurname = self.surname.get()
        PlainTextUsername = self.user_name.get()
        PlainTextPassword = self.password.get()
        PlainTextConfirmPassword = self.confirmPassword.get()
        PlainTextFirstname = self.firstname.get()
        lenPlainTextPassword = len(PlainTextPassword)

        # checks if there is actually something that the user has entered as a username, as a password
        # and as a firstname

        for character in PlainTextPassword:
            if (ord(character) <= 90 and ord(character) >= 65):
                lowerCaseChar += 1
            elif (ord(character) <= 122 and ord(character) >= 97):
                upperCaseChar += 1
            elif (ord(character) <= 47 and ord(character) >= 32) or (
                    ord(character) <= 64 and ord(character) >= 58) \
                    or (ord(character) <= 96 and ord(character) >= 91) or \
                    (ord(character) <= 123 and ord(character) >= 126):
                specialCaseChar += 1

        # checks if the password and confirm password are the same
        if PlainTextPassword != PlainTextConfirmPassword:
           theSame = False


        if ((lowerCaseChar + upperCaseChar) < 8):
            alphabet = False
        if (specialCaseChar <= 1):
            special = False
        if lenPlainTextPassword <= 10:
            length = False


        if PlainTextUsername == "" or PlainTextPassword == "" or PlainTextFirstname == "":
        # if the statement is not met, where the user hasn't actually inputted something in any of those fields
            inputted = False

        return (length, alphabet, special, theSame, inputted)


    # create submit function
    def submit(self):

        PlainTextSurname = self.surname.get()
        PlainTextUsername = self.user_name.get()
        PlainTextPassword = self.password.get()
        PlainTextFirstname = self.firstname.get()

        lengthPassword, alphabetPassword, specialCharPassword, theSame, inputted = self.checkPasswordChar()

        if not lengthPassword:
            messagebox.showwarning(message="Please enter a password with at least 10 characters")

        if not alphabetPassword:
            messagebox.showwarning(message="Please enter a password with at least 8 alphabetical characters")

        if not specialCharPassword:
            messagebox.showwarning(message="Please enter a password with at least two special characters")

        if not theSame:
            messagebox.showerror(message="Password and Confirm Password are not the same")

        if not inputted:
            messagebox.showerror(message="No value was entered in a field(s)")

        if lengthPassword and alphabetPassword and specialCharPassword and theSame and inputted:
            proceed = tk.messagebox.askquestion(title="message",
                                                message="Are the details correct and do you wish to proceed?")
            # if they selected yes
            if proceed == "yes":
                # it would add a user to the database, by calling the function addUser
                if self.addUser(PlainTextFirstname, PlainTextSurname, PlainTextUsername, PlainTextPassword):
                    tk.messagebox.showinfo(title="message",
                                           message="Please enter through the sign up page to make sure you can log in")

    def PreviousPage(self):
        self.root.destroy()  # destroys the page
        pygame.mixer.music.stop()
        TKINTER.FirstPage()  # calls the TKINTER window and displays it to a user
    
    def addUser(self, firstname, surname, username1, password1): # passes through these parameters

        try:
            # no error therefore must raise an exception so if there is any type of error beforehand, it will go to except line
            conn = sqlite3.connect("address_book.db")
            # includes white space, digits and letters and punctuation
            salts = getHashPassword.getSalt()
            # the 100, password+salt 100 times
            # encode() = changes from unicode string to byte string
            hashPassword = getHashPassword.getHashPassword(password1, salts)
            # string is SQL command
            # question marks means fill this in with value in give in next argument
            # username, password, salt = tuple of three
            # SQL escaping, this escapes any special characters
            # this avoids sql injection
            # .hex() = gives in binary representation
            conn.execute("""INSERT INTO users(
                    FirstName,Surname, username , password, salt) values(?,?,?,?,?)""",(firstname, surname, username1, hashPassword.hex(), salts))

            # this query inserts the following parameters into the database
            # the parameters are firstname, surname, username, a hashed password so that my database
            # is further protected as well as a salt

            conn.commit()  # this commits the changes to the database that have been made, if there have been any changes
            conn.close()  # closes the database so that it cant be edited and changed

            return True # returns True

        except sqlite3.IntegrityError as e: # if there is an integrity error in the sql of the database when putting
            # the values inside the database
            # this means that there is already a username that exists, therefore the error message pops up,
            # alerting the user that username already exists
            # An integrity error is an exception raised when the relational integrity of the database is affected1.
            # This can happen when a foreign key check fails, there is a duplicate key
            tk.messagebox.showerror(title="message",message="Username exists")
            return False # returns False

        except Exception as e: # any other error that occurs from putting the values inside the database will lead to
            # an error message sent to the user
            tk.messagebox.showerror(title="message",message="Error")
            return False

    def showPassword(self):
        self.password.config(show="") # sets the password to what the user has entered

    def ShowHidePassword(self):
        if not self.isPasswordShown: # if isPasswordShown not equal to True
            self.password.config(show="") # password will be set to the actual letters the user has entered
            self.confirmPassword.config(show="") # confirm password will be set to the actual letters the user has
            # entered, so that the user can see if their password and confirm password are the same
            self.showPasswordBut.config(text="Hide Password") # changes the button to say Hide password
        else:
            self.password.config(show="*") # the password is set to an asterisk so that the password can be kept safe
            self.confirmPassword.config(show="*") # confirm password is set to an asterisk so that the password can be kept safe
            self.showPasswordBut.config(text="Show Password") # changes the button to say show password

        self.isPasswordShown = not self.isPasswordShown # changes the isPasswordShown to the opposite boolean value
        # e.g. from True to False, so that the next time, the section of code that will be run will be the other
        # section from the previous section and would be the right section respective to the show and hide password


if __name__ == "__main__":
    SignUpPage1()
