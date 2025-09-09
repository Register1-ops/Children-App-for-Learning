import tkinter as tk
from tkinter import messagebox

import MainPage
import TKINTER
import pygame


class Songs():

    def __init__(self):
        self.MusicOn = False
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
        self.filemenu.add_command(label="Close", command=self.on_closing)
        # add a menu item to the menu to close the program by calling the on_closing function
        self.filemenu.add_separator()
        # adds a seperator so that both the command on the menubar can be seen
        self.filemenu.add_command(label="Close Without question", command=exit)
        # creates a command called close without question which exits the program without asking the user
        # whether they want to

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        # adds a menu item to the menu bar

        self.menubar.add_cascade(menu=self.filemenu, label="Close application")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        # add_cascade - it's because im  not adding a single element per se, im adding a submenu
        # (which may have multiple entries) to the menu. In programming the term "cascade" generally
        # means something like "perform multiple operations/tasks in this statement" (
        # so in this case it'd be adding multiple things i.e. the contents of the sub menu to the menu)

        # configures the menu menubar so that the menu bar actually appears on the screen
        self.root.config(menu=self.menubar)


        self.Label = tk.Label(self.root, text = "Select a song to listen to", font = ("Poor Richard", 20))
        self.Label.place(x=50,y=50)
        self.Label["bg"] = "#ffaa12"

        self.TheBeatOfNatureGuitarButton = tk.Button(self.root, text="The Beat of Nature Guitar", font=("Poor Richard", 16), command=self.TheBeatOfNatureGuitar)
        self.TheBeatOfNatureGuitarButton.place(x=250, y=400)
        self.TheBeatOfNatureGuitarButton["bg"] = "#aadd12"

        self.ElectronicRockButton = tk.Button(self.root, text="Electronic Rock",
                                                     font=("Poor Richard", 16), command=self.ElectronicRock)
        self.ElectronicRockButton.place(x=250, y=200)
        self.ElectronicRockButton["bg"] = "#aadd12"

        self.AdvertisingSongButton = tk.Button(self.root, text="Advertisement Song",
                                                     font=("Poor Richard", 16), command=self.AdvertisingSong)
        self.AdvertisingSongButton.place(x=250, y=350)
        self.AdvertisingSongButton["bg"] = "#aadd12"

        self.InfinityHeroesButton = tk.Button(self.root, text="Infinity",
                                               font=("Poor Richard", 16), command=self.InfinityHeroes)
        self.InfinityHeroesButton.place(x=250, y=300)
        self.InfinityHeroesButton["bg"] = "#aadd12"

        self.StopButton = tk.Button(self.root, text="Stop", font=("Poor Richard", 16),
                                                     command=self.StopMusic)
        self.StopButton.place(x=250, y=550)

        self.GoBackButton = tk.Button(self.root, text="Go Back", font=("Poor Richard", 16),
                                    command=self.GoBack)
        self.GoBackButton.place(x=50, y=550)

        self.StompingSongButton = tk.Button(self.root, text="Stomping Song",
                                              font=("Poor Richard", 16), command=self.StompingSong)
        self.StompingSongButton.place(x=250, y=250)
        self.StompingSongButton["bg"] = "#aadd12"

        # creates a button to go onto the next page
        #self.NextPage = tk.Button(self.root, text="Next page", font=("Century", 16), command=self.NextPage)
        #self.NextPage.place(x=0, y=350)

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

    def StopMusic(self):
        if self.MusicOn == True:
            pygame.mixer.music.stop()
            self.MusicOn = False

    def TheBeatOfNatureGuitar(self):
        if self.MusicOn == False:  # if the member variable Music on is False
            pygame.mixer.init()  #  it initializes pygame modules
            pygame.mixer.music.load("Music For Project/the-beat-of-nature-122841.mp3") # this loads the specific music
            # in
            pygame.mixer.music.play() # this plays the music
            self.MusicOn = True  # sets Music on to True since the music has started playing

        else:
            messagebox.showwarning(message="Please stop the music that is already playing") # outputs a warning
            # to show the user that another music piece is being played, shows warning incase user clicked
            # another song by mistake

    def ElectronicRock(self):
        if self.MusicOn == False:  # if the member variable Music on is False
            pygame.mixer.init()  # it initializes pygame modules
            pygame.mixer.music.load("Music For Project/electronic-rock-king-around-here-15045.mp3")  # this loads the specific music
            # in
            pygame.mixer.music.play()  # this plays the music
            self.MusicOn = True  # sets Music on to True since the music has started playing

        else:
            messagebox.showwarning(message="Please stop the music that is already playing")  # outputs a warning
            # to show the user that another music piece is being played, shows warning incase user clicked
            # another song by mistake

    def AdvertisingSong(self):
        if self.MusicOn == False:  # if the member variable Music on is False
            pygame.mixer.init()  #  it initializes pygame modules
            pygame.mixer.music.load("Music For Project/advertising-corporate-long-9967.mp3") # this loads the specific music
            # in
            pygame.mixer.music.play() # this plays the music
            self.MusicOn = True  # sets Music on to True since the music has started playing

        else:
            messagebox.showwarning(message="Please stop the music that is already playing") # outputs a warning
            # to show the user that another music piece is being played, shows warning incase user clicked
            # another song by mistake

    def InfinityHeroes(self):
        if self.MusicOn == False:  # if the member variable Music on is False
            pygame.mixer.init()  #  it initializes pygame modules
            pygame.mixer.music.load("Music For Project/infinity-heroes-epic-inspiring-adventurous-soundtrack-9278.mp3")
            # this loads the specific music
            # in
            pygame.mixer.music.play() # this plays the music
            self.MusicOn = True  # sets Music on to True since the music has started playing

        else:
            messagebox.showwarning(message="Please stop the music that is already playing") # outputs a warning
            # to show the user that another music piece is being played, shows warning incase user clicked
            # another song by mistake

    def StompingSong(self):
        if self.MusicOn == False:  # if the member variable Music on is False
            pygame.mixer.init()  #  it initializes pygame modules
            pygame.mixer.music.load("Music For Project/stomping-rock-four-shots-111444.mp3")
            # this loads the specific music
            # in
            pygame.mixer.music.play() # this plays the music
            self.MusicOn = True  # sets Music on to True since the music has started playing

        else:
            messagebox.showwarning(message="Please stop the music that is already playing") # outputs a warning
            # to show the user that another music piece is being played, shows warning incase user clicked
            # another song by mistake




    def GoBack(self):
        self.root.destroy()  # destroys the root page
        if self.MusicOn == "True":  # if the music is on
            pygame.mixer.music.stop() # stops the music
        MainPage.LevelOptions()



if __name__ == "__main__":
    Songs()
