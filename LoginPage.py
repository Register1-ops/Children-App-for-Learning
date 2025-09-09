import tkinter as tk
from tkinter import messagebox
import Login
import MainPage

import TKINTER
import pygame

class LoginPage():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/stomping-rock-four-shots-111444.mp3")
        pygame.mixer.music.play()
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        pygame.mixer.music.set_volume(0.05)
        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("825x530")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Login Page")  # title refers to the name provided to the window. It appears on the top of the
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
        self.menubar.add_cascade(menu=self.filemenus, label="Close application")
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)

        self.root.config(menu=self.menubar)  # configures the menubar so that the menubar actually shows up


        # create text boxes
        # creates an entry space for users to be able to input their credentials
        self.user_name = tk.Entry(self.root, width=30) # creates an entry box within the root with a width of 30 pixels
        self.user_name.grid(row = 5, column = 3, padx=50,pady=50) # places the entry box in a place inside the page
        # creates an entry space for users to type in their password
        self.passwordFrame = tk.Frame(self.root) # creates a frame from inside the root
        self.password = tk.Entry(self.root,show = "*",width=30) # creates a password entry box,
        # that shows * when they enter their password, which is more secure
        self.password.grid(row = 6, column = 3, padx=50,pady=50) # places the entry button

        self.showPasswordBut = tk.Button(self.root, text = "Show Password", font= ("Arial",12), command = self.ShowHidePassword)
        self.showPasswordBut.grid(row = 6, column = 4)

        self.isPasswordShown = False


        #create text box labels
        self.description_label = tk.Label(self.root, text="Enter your credentials/ username and password here: ", font = ("Arial",15))
        self.description_label.grid(row=1,column=3, padx = 50, pady=50)
        # creates a coloured label
        self.description_label["bg"] = "#fbad00"

        #create text box labels
        self.user_name_label = tk.Label(self.root, text="User Name")
        self.user_name_label.grid(row=5,column=0, padx = 10, pady =10)
        # creates a coloured label
        self.user_name_label["bg"] = "#fead90"

        self.password_label = tk.Label(self.root, text="Password")
        self.password_label.grid(row=6, column=0, padx = 10, pady =10)
        self.password_label["bg"] = "#faad90"

        #create a sumbmit button
        self.submit_button = tk.Button(self.root, text = "Submit", font=("Arial",12), command= self.submit)
        # places button in a certain area
        self.submit_button.grid(row=7, column = 4, columnspa=2, pady=20, padx=20, ipadx=2)
        # creates a coloured label
        self.submit_button["bg"] = "#fada45"

        # creates a button called previous page to allow user to go back to a previous page
        self.NextPage = tk.Button(self.root, text="Previous page", font=("Arial", 12), command = self.PreviousPage)
        self.NextPage.grid(row = 7, column = 3)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidentally,
        # the page will close and be destroyed.

    # create submit function
    def submit(self):
        PlainTextUsername = self.user_name.get()  # this line gets what the user has inputted in the user_name entry
        PlainTextPassword = self.password.get()  # the stores what the user has entered into the password entry box
        try:
            userID = Login.verification(PlainTextUsername, PlainTextPassword)  # this passes the two variables
            # as parameters to the login module to verify that the user actually exists in the database
            # or that they haven't accidentally mistyped their username or password
            self.root.destroy()  # the row window is destroyed
            pygame.mixer.music.stop()
            MainPage.LevelOptions()  # the main page module passing in the userID as a parameters to go to the
            # next window which is the page that shows all the options of the quizzes that the user can choose from
        except Login.NotLoggedInError:   # if the user does not have the correct credentials to log in
            tk.messagebox.showerror(title="message",message="Incorrect Username or Password") # an error message will
            # be shown to the user, so the user has to reenter the correct credentials or sign up

    def PreviousPage(self):
        self.root.destroy() # if the previous page is called, the root window is destroyed
        pygame.mixer.music.stop()
        TKINTER.FirstPage() # and the TKINTER module is called, so the that page is then shown to the user

    def showPassword(self):
        self.password.config(show="")  # sets the password to what the user has entered

    def ShowHidePassword(self):
        if not self.isPasswordShown:  # if isPasswordShown not equal to True
            self.password.config(show="")  # password will be set to the actual letters the user has entered
            # entered, so that the user can see if their password and confirm password are the same
            self.showPasswordBut.config(text="Hide Password")  # changes the button to say Hide password
        else:
            self.password.config(show="*")  # the password is set to an asterisk so that the password can be kept safe
            self.showPasswordBut.config(text="Show Password")  # changes the button to say show password

        self.isPasswordShown = not self.isPasswordShown  # changes the isPasswordShown to the opposite boolean value
        # e.g. from True to False, so that the next time, the section of code that will be run will be the other
        # section from the previous section and would be the right section respective to the show and hide password


if __name__ == "__main__":
    LoginPage()
