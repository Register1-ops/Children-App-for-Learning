import tkinter as tk
from tkinter import messagebox

import TKINTER
import pygame 


class GAME():

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/infinity-heroes-epic-inspiring-adventurous-soundtrack-9278.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#ffbf00"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("800x800")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Game")  # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # The tk.Menu widget allows you to add a menubar to the main window (tk.Tk) or to a child window
        # Tearoff allows you to detach menus for the most window, resulting in floating menus. When you click a
        # top menu item after creating a menu, you may notice dotted lines at the top. To remedy this, set tearoff to 0
        # at the time of menu declaration.
        self.filemenu.add_command(label="Close", command = self.on_closing)
        # add a menu item to the menu to close the program by calling the on_closing function
        self.filemenu.add_separator()
        # adds a seperator so that both the command on the menubar can be seen
        self.filemenu.add_command(label="Close Without question", command = exit)
        # creates a command called close without question which exits the program without asking the user
        # whether they want to
        
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        # adds a menu item to the menu bar
        self.actionmenu.add_command(label="Show message", command=self.show_message)
        # adds a command under the menu item actionmenu called show message
        # when clicked it will call the function show_message
        
        self.menubar.add_cascade(menu=self.filemenu, label = "Close application")
        self.menubar.add_cascade(menu=self.actionmenu, label = "Action")
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)

        # configures the menu menubar so that the menu bar actually appears on the screen
        self.root.config(menu= self.menubar)

        # Label is a Label widget with an Parchment font and a size of 50
        # creates a label called question for kids which is at the top of the screen as a title for the page
        self.Titlelabel = tk.Label(self.root, text = "Question for Kids", font=("Parchment", 50))
        # this packs the label so it has a padding of 10 pixels in both the x and y coordinate axis
        self.Titlelabel.pack(padx=10, pady = 10)
        self.Titlelabel["bg"] = "#6290dd"

        # creates a textbox which the user is able to write in
        self.textbox = tk.Text(self.root, height = 5, font = ("Arial", 16))
        # creates a key press which outputs the characters that the user has entered, it calls the function shortcut
        self.textbox.bind("<KeyPress>", self.shortcut)

        #scrollbar
        #scrollview
        # pads the textbox
        self.textbox.pack(padx=10, pady = 10)
        
        self.check_state = tk.IntVar() # IntVar is a function in the Tkinter module that defines a variable that holds
        # integer data12. The variable can be set and retrieved using getter and setter methods2.
        # The variable is declared like this: x = IntVar() # Holds an integer; default value is 0


        # creates a button so that the user can click on it to therefore click on the display your message button to display their message
        # just incase they click on the display your message button by accident it prevents the text from being outputted unecesarily
        self.check = tk.Checkbutton(self.root, text = "Show Messagebox", font=("Wide Latin", 16), variable = self.check_state)
        # pads the button
        self.check.place(x = 0, y = 250)
        self.check["bg"] = "#ea2323"


        # creates a button to display their message
        self.button = tk.Button(self.root, text="Display your message", font=("Stencil", 16), command = self.show_message)
        self.button.place(x = 0, y = 300)
        self.button["bg"] = "#db3e00"

        # creates a button to clear what they have written in the textbox
        self.ClearButton = tk.Button(self.root, text="Clear", font=("Poor Richard", 16), command=self.clear)
        self.ClearButton.place(x =0, y = 400)
        self.ClearButton["bg"] = "#fccb00"

        # creates a button to go onto the next page
        self.NextPage = tk.Button(self.root, text="Next page", font=("Century", 16), command = self.NextPage)
        self.NextPage.place(x =0, y = 350)
        self.NextPage["bg"] = "#008b02"

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()

        
    def show_message(self):
        if (self.check_state.get()) == 0:  # when the function is called,
            # this checks the state of the button that is pressed
            print(self.textbox.get("1.0", tk.END))  # this will print out the text inside the text box
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get("1.0", tk.END))



    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            # if the event.state = 4 and event.keysym is Return, then the message will be outputted to the user
            # in a force of a messagebox
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidentally,
        # the page will close and be destroyed.


    def clear(self):
        self.textbox.delete("1.0", tk.END)
        # this will delete the text in thee textbox from beginning to end

    def NextPage(self):
        self.root.destroy()
        # destroys the page and calls the TKINTER module
        pygame.mixer.music.stop()
        TKINTER.FirstPage()


if __name__ == "__main__":
    GAME()
