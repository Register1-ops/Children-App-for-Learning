import tkinter as tk
from tkinter import *

import pygame
from PIL import ImageTk, Image
import LoginPage
import SignUpPage


class FirstPage:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/advertising-corporate-long-9967.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.stop()
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#adbd00"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("800x800")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("First Page")  # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.

        # creates a label called Login-In or Sign-Up in arial font
        # Label is a Label widget with an Arial font and a size of 18
        # creates a label called question for kids which is at the top of the screen as a title for the page
        self.label = tk.Label(self.root, text="Login-In or Sign-Up", font=("Arial", 18))
        # pads the label
        self.label.pack(padx=20, pady=20)

        # creates a variable called buttonFrame in self.root
        # buttonFrame is Frame within the root
        self.buttonFrame = tk.Frame(self.root)
        # this button is in column 1 with a weight of 1 which is the amount of space it takes within a column compared to other buttons in that row
        self.buttonFrame.columnconfigure(0, weight=1)
        # this button is in column 1 with a weight of 1 which is the amount of space it takes within a column compared to other buttons in that row
        self.buttonFrame.columnconfigure(1, weight=1)
        # self.buttonFrame.columnconfigure(2, weight=1)

        # creates a button called login inside column 1 and row 0 
        self.LoginButton = tk.Button(self.buttonFrame, text="Login", font=("Arial", 18), command=self.LoginPage)
        self.LoginButton.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.LoginButton["bg"] = "#ff00ff"
        # creates a button called signup in column 1 
        self.SignUpButton = tk.Button(self.buttonFrame, text="Signup", font=("Arial", 18), command=self.SignUpPage)
        self.SignUpButton.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.SignUpButton["bg"] = "#affbaa"
        # anchor = W to the creation of your widget we keep the textvariable of the label aligned to the left.
        # and by changing the sticky to say sticky = N+W+E i can tell python to stretch the widget to fit the cell up left and right.

        self.buttonFrame.pack(fill="x")
        # the buttonFrame is packed so that it fills the x - axis
        self.AddFrame = tk.Frame(self.root)
        # I have created another frame within the root
        self.AddFrame["bg"] = "#adbd00"
        # the Frame has a background colour of the hexadecimal value abdb00

        self.width = 1 # sets the width to a member variable of the clas within the value of 1
        self.height = 1 # sets the height to a member variable of the clas within the value of 1

        self.root.bind("<Configure>", resize_func(self))  # bind: binding function resize to event configure
        # resize: passes the function through
        # this calls the function resize_func
        # this resizes the

        self.imageRaw = Image.open("Pictures for project/pexels-jaime-reimer-2662116(1).jpg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        #
        self.imgpanel = Label(self.AddFrame, width=self.width, height=self.height, image=self.img)
        # anel.grid(row=9)
        self.imgpanel.pack(side="right", fill="none", expand=False)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw2 = Image.open("Pictures for project/pexels-pixabay-147411.jpg")
        self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        self.imgpanel2 = Label(self.AddFrame, width=self.width, height=self.height, image=self.img2)
        # panel.grid(row=9)
        self.imgpanel2.pack(side="left", fill="none", expand=False)

        self.AddFrame.pack(fill="x")

        self.root.mainloop()

    def LoginPage(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        LoginPage.LoginPage()

    def SignUpPage(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        SignUpPage.SignUpPage1()

def resize_func(self):
    def resize(event):
        self.newWidth = max(self.root.winfo_width() / 2, 1)
        if self.newWidth != self.width:
            self.width = self.newWidth
            self.height = max((2 / 3) * self.width, 1)
            self.imgpanel.config(width =  self.width, height = self.height)
            self.imgpanel2.config(width=self.width, height=self.height)
            self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
            self.imgpanel["image"] = self.img
            self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
            self.imgpanel2["image"] = self.img2
    return resize


if __name__ == "__main__":
    FirstPage()
