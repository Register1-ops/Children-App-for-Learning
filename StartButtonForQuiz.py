import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import Level1Alphabet
import Grammar
import LivingThingsAndTheirHabitats
import Level2Colours
import Level2Maths
import Level3Maths
import Level1Colours
import RhymingWords
import Punctation
import Level1Maths
import Shapes
import OwnQuestions
import WHATTODOForChildrenToReadToAdults



class StartButton:
    def __init__(self, count):

        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("600x490")  # This method is used to set the dimensions of the Tkinter window and is used to
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
        self.menubar.add_cascade(menu=self.filemenus, label="Close application")
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)

        # configures the menu menubar so that the menu bar actually appears on the screen
        self.root.config(menu=self.menubar)

        self.count = count # sets the count variable that has been passed through into this module to a member
        # variable so it can be accessed throughout the code

        # create a submit button
        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 35), command=self.StartButtonFunc)
        # places button in a certain area
        self.start_button.place(x=225, y=200)
        # creates a coloured label
        self.start_button["bg"] = "#fada45"

        self.width = 150
        self.height = 150
        self.imageRaw = Image.open("Pictures for project/pexels-cottonbro-studio-9668535(1).jpg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        self.imgpanel = tk.Button(self.root, width=self.width, height=self.height, image=self.img)
        # anel.grid(row=9)
        self.imgpanel.pack(side="right", fill="none", expand=False)
        # CreateImage =  panel.create_image(width,height,image = img)
        self.imgpanel.place(x=1, y=1)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw2 = Image.open("Pictures for project/pexels-pixabay-358457 (1).jpg")
        # this opens the specific image in the folder named
        self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        self.imgpanel2 = tk.Button(self.root, width=self.width, height=self.height, image=self.img2)
        # anel.grid(row=9)
        self.imgpanel2.pack(side="right", fill="none", expand=False)
        self.imgpanel2.place(x=300, y=300)

        self.imageRaw3 = Image.open("Pictures for project/pexels-eberhard-grossgasteiger-1624496.jpg")
        # this opens the specific image in the folder named
        self.img3 = ImageTk.PhotoImage(self.imageRaw3.resize((int(self.width), int(self.height))))
        self.imgpanel3 = tk.Button(self.root, width=self.width, height=self.height, image=self.img3)
        # anel.grid(row=9)
        self.imgpanel3.pack(side="right", fill="none", expand=False)
        self.imgpanel3.place(x=100, y=300)

        self.imageRaw4 = Image.open("Pictures for project/pexels-op-12118245.jpg")
        # this opens the specific image in the folder named
        self.img4 = ImageTk.PhotoImage(self.imageRaw4.resize((int(self.width), int(self.height))))
        self.imgpanel4 = tk.Button(self.root, width=self.width, height=self.height, image=self.img4)
        # anel.grid(row=9)
        self.imgpanel4.pack(side="right", fill="none", expand=False)
        self.imgpanel4.place(x=250, y=3)

        self.imageRaw5 = Image.open("Pictures for project/pexels-alexander-dummer-1919030.jpg")
        # this opens the specific image in the folder named
        self.img5 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        self.imgpanel5 = tk.Button(self.root, width=self.width, height=self.height, image=self.img5)
        # anel.grid(row=9)
        self.imgpanel5.pack(side="right", fill="none", expand=False)
        self.imgpanel5.place(x=6, y=600)

        self.imageRaw6 = Image.open("Pictures for project/pexels-şahin-durmaz-10618404.jpg")
        # this opens the specific image in the folder named
        self.img6 = ImageTk.PhotoImage(self.imageRaw6.resize((int(self.width), int(self.height))))
        self.imgpanel6 = tk.Button(self.root, width=self.width, height=self.height, image=self.img6)
        # anel.grid(row=9)
        self.imgpanel6.pack(side="right", fill="none", expand=False)
        self.imgpanel6.place(x=425, y=225)

        self.imageRaw7 = Image.open("Pictures for project/pexels-brett-sayles-2479312.jpg")
        # this opens the specific image in the folder named
        self.img7 = ImageTk.PhotoImage(self.imageRaw7.resize((int(self.width), int(self.height))))
        self.imgpanel7 = tk.Button(self.root, width=self.width, height=self.height, image=self.img7)
        # anel.grid(row=9)
        self.imgpanel7.pack(side="right", fill="none", expand=False)
        self.imgpanel7.place(x=25, y=225)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()


    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidently,
        # the page will close and be destroyed.

    def StartButtonFunc(self):
        # since the count variable is a member i don't need to pass it into the function since it can be
        # accessed throughout the module

        self.root.destroy() # the root is then destroyed

        # this is a decision based on the count value that has been passed through,
        # this chooses what quiz to show to the user
        if self.count == 0:
            Level1Alphabet.Level1Alphabet()

        elif self.count == 1:
            Level1Maths.Maths()

        elif self.count == 2:
            Level1Colours.Level1Colours()

        elif self.count == 3:
            Shapes.Shapes()

        elif self.count == 4:
            Level2Maths.Level2Maths()

        elif self.count == 5:
            Level2Colours.Level2Colours()

        elif self.count == 6:
            Level3Maths.Level3Maths()

        elif self.count == 7:
            LivingThingsAndTheirHabitats.LivingThingsAndTheirHabitat()

        elif self.count == 8:
            RhymingWords.RhymingWords()

        elif self.count == 9:
            Punctation.Punctuation()

        elif self.count == 10:
            Grammar.Grammar()

        elif self.count == 11:
            WHATTODOForChildrenToReadToAdults.What()

        elif self.count == 12:
            OwnQuestions.OwnQuestions()

        return
if __name__ == "__main__":
    StartButton(count=None)