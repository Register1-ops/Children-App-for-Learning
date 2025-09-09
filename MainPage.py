
import time
import tkinter
import tkinter as tk  # importing tkinter as tk so can use tk as abbreviation
from tkinter import messagebox  # from the module tkinter, i import messagebox
import pygame
import BookLog
import Login
import OwnQuestions
import Songs
import StartButtonForQuiz
from PIL import Image, ImageTk
import random


class LevelOptions():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/gypsy-time-acoustic-jazz-guitar-143797.mp3")
        pygame.mixer.music.play()
        self.ball = None
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.UserID = Login.getUserID()
        # stores the userID that has been passed into the module, as a member variable to the class
        self.rootFrame = None  # defines rootFrame as None, so it can be used throughout the class
        self.FirstPage(self.UserID)  # calls the FirstPage function that passes in the userID as a parameter, this
        # function outputs the first page of options to the user
        self.menubar = tk.Menu(self.root)  # creates a menu within the root of thr program

        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("2000x775")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Options Page")  # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.

        self.Window_Width = 800

        self.Window_Height = 600

        self.Ball_Start_XPosition = 50

        self.Ball_Start_YPosition = 50

        self.Ball_Radius = 30

        self.Ball_min_movement = 5

        self.Refresh_Sec = 0.01

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


        self.root.bind("<Configure>", self.resize)  # bind: binding function resize to event configure
        # resize: passes the function through
        # this calls the function resize_func

        self.root.config(menu=self.menubar)  # configures the menubar so that the menubar actually shows up

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit

        #self.root.mainloop()
        self.animate_ball(self.Ball_min_movement, self.Ball_min_movement)


    def create_animation_canvas(self):
        canvas = tkinter.Canvas(self.root)
        canvas.configure(bg="Blue")
        canvas.pack(fill="both", expand=True)
        return canvas

    def animate_ball(self, xinc, yinc):
        xCurrentPos = self.Ball_Start_XPosition
        yCurrentPos = self.Ball_Start_YPosition
        while True:
            try:
                self.root.update()
            except Exception as e:
                break

            try:
                if self.ball is None:
                    self.ball = self.rootFrame.create_oval(self.Ball_Start_XPosition - self.Ball_Radius,
                                                   self.Ball_Start_YPosition - self.Ball_Radius,
                                                   self.Ball_Start_XPosition + self.Ball_Radius,
                                                   self.Ball_Start_YPosition + self.Ball_Radius,
                                                   fill="Red", outline="Black", width=4)
                    xCurrentPos = self.Ball_Start_XPosition
                    yCurrentPos = self.Ball_Start_YPosition

                xCurrentPos += xinc
                yCurrentPos += yinc
                self.rootFrame.move(self.ball, xinc, yinc)
                if (xCurrentPos > self.Window_Width) or (yCurrentPos > self.Window_Height):
                    xDiff = min(self.Window_Width - xCurrentPos - 2*self.Ball_Radius,0)
                    yDiff = min(self.Window_Height - yCurrentPos - 2*self.Ball_Radius,0)
                    self.rootFrame.move(self.ball, xDiff, yDiff)
                    xCurrentPos += xDiff
                    yCurrentPos += yDiff


                time.sleep(self.Refresh_Sec)
                ball_pos = self.rootFrame.coords(self.ball)
                # unpack array to variables
                al, bl, ar, br = ball_pos
                if al < abs(xinc) or ar > self.Window_Width - abs(xinc):
                    xinc = -xinc
                if bl < abs(yinc) or br > self.Window_Height - abs(yinc):
                    yinc = -yinc
            except Exception as e:
                print(e)

    def resize(self, event):
        self.Window_Width = self.root.winfo_width()
        self.Window_Height = self.root.winfo_height()




    def FirstPage(self, UserID):
        if self.rootFrame is not None:
            self.rootFrame.destroy()
            self.ball = None
        self.rootFrame = self.create_animation_canvas() # accessing Tkinter, in a variable root, so everything can be stored inside the root
        self.rootFrame["bg"] = "coral"  # create a background colour for the page
        self.rootFrame.pack(fill="both", expand=True)

        # create text box labels
        self.level1_label = tk.Label(self.rootFrame, text="Level 1", font=("Arial", 25))
        self.level1_label.grid(row=1, column=75, padx=50, pady=50)
        # creates a coloured label
        self.level1_label["bg"] = "#fead91"

        # create text box labels
        self.level2_label = tk.Label(self.rootFrame, text="Level 2", font=("Arial", 25))
        self.level2_label.grid(row=2, column=75, padx=30, pady=30)
        # creates a coloured label
        self.level2_label["bg"] = "#abcd45"

        # create text box labels
        self.level3_label = tk.Label(self.rootFrame, text="Level 3", font=("Arial", 25))
        self.level3_label.grid(row=3, column=75, padx=30, pady=30)
        # creates a coloured label
        self.level3_label["bg"] = "#dcba12"

        # create text box labels
        self.otherTopics_label = tk.Label(self.rootFrame, text="Other topics", font=("Arial", 25))
        self.otherTopics_label.grid(row=4, column=75, padx=30, pady=30)
        # creates a coloured label
        self.otherTopics_label["bg"] = "#baab99"

        # creates a button
        self.Level1Maths_Button = tk.Button(self.rootFrame, text="Maths", font=("Arial", 17), command=self.Level1Maths)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.Level1Maths_Button.grid(row=1, column=150, padx=30, pady=30)
        self.Level1Maths_Button["bg"] = "#fead91"

        # creates a button
        self.Level2Maths_Button = tk.Button(self.rootFrame, text="Maths", font=("Arial", 17), command=self.Level2Maths)
        # under the root, with the text called alphabet with the font being arial at size 20, when clicked on,
        # the function alphabet will be accessed and processed
        self.Level2Maths_Button.grid(row=2, column=150, padx=30, pady=30)  # grids a button
        self.Level2Maths_Button["bg"] = "#abcd45"  # creates a button background colour

        # creates a button
        self.Level3Maths_Button = tk.Button(self.rootFrame, text="Maths", font=("Arial", 17), command=self.Level3Maths)
        # under the root, with the text called alphabet with the font being arial at size 20, when clicked on,
        # the function alphabet will be accessed and processed
        self.Level3Maths_Button.grid(row=3, column=150, padx=2, pady=2)  # grids a button
        self.Level3Maths_Button["bg"] = "#dcba12"  # creates a button background colour

        # creates a button
        self.AlphabetButton = tk.Button(self.rootFrame, text="Alphabet", font=("Arial", 17), command=self.Alphabet)
        # under the root, with the text called alphabet with the font being arial at size 20, when clicked on,
        # the function alphabet will be accessed and processed
        self.AlphabetButton.grid(row=4, column=250, padx=30, pady=30)  # grids a button
        self.AlphabetButton["bg"] = "#baab99"  # creates a button background colour

        # creates a button
        self.Level1ColoursButton = tk.Button(self.rootFrame, text="Colours", font=("Arial", 17),
                                             command=self.Level1Colours)
        # under the root, with the text called colours with the font being arial at size 20, when clicked on,
        # the function colours will be accessed and processed
        self.Level1ColoursButton.grid(row=2, column=250, padx=30, pady=30)  # grids a button on the screen
        self.Level1ColoursButton["bg"] = "#abcd45"  # creates a button background colour

        # creates a button
        self.Level2ColoursButton = tk.Button(self.rootFrame, text="Colours", font=("Arial", 17),
                                             command=self.Level2Colours)
        # under the root, with the text called colours with the font being arial at size 20, when clicked on,
        # the function colours will be accessed and processed
        self.Level2ColoursButton.grid(row=1, column=250, padx=30, pady=30)  # grids a button on the screen
        self.Level2ColoursButton["bg"] = "#fead91"  # creates a button background colour

        # creates a button
        self.ShapesButton = tk.Button(self.rootFrame, text="Shapes", font=("Arial", 17), command=self.Shapes)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.ShapesButton.grid(row=4, column=300, padx=30, pady=30)
        self.ShapesButton["bg"] = "#baab99"

        # creates a button
        self.LivingThingsAndTheirHabitatButton = tk.Button(self.rootFrame, text="Living Things And Their Habitats",
                                                           font=("Arial", 17),
                                                           command=self.LivingThingsAndTheirHabitat)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.LivingThingsAndTheirHabitatButton.grid(row=4, column=150, padx=30, pady=30)
        self.LivingThingsAndTheirHabitatButton["bg"] = "#baab99"

        # creates a button
        self.PunctuationButton = tk.Button(self.rootFrame, text="Punctuation", font=("Arial", 17),
                                           command=self.Punctuation)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.PunctuationButton.grid(row=5, column=150, padx=30, pady=30)
        self.PunctuationButton["bg"] = "#baab99"

        # creates a button
        self.RhymingWordsButton = tk.Button(self.rootFrame, text="Rhyming Words", font=("Arial", 17),
                                            command=self.RhymingWords)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.RhymingWordsButton.grid(row=5, column=250, padx=30, pady=30)
        self.RhymingWordsButton["bg"] = "#baab99"

        self.NextPageButton = tk.Button(self.rootFrame, text="Next Page ➡️", font=("Arial", 17), command=self.NextPage)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.NextPageButton.grid(row=1, column=350, padx=10, pady=10)
        self.NextPageButton["bg"] = "#ccbb31"

        self.HelpButton = tk.Button(self.rootFrame, text="Help", font=("Arial", 17), command=self.Help)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.HelpButton.grid(row=1, column=340)
        self.HelpButton["bg"] = "#abca76"

        self.width = 100
        self.height = 100

        self.imageRaw = Image.open("Pictures for project/pexels-cottonbro-studio-9668535(1).jpg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        #
        self.imgpanel = tk.Button(self.root, width=self.width, height=self.height, image=self.img,
                                  command=self.PlaySound)
        self.imgpanel.place(x=1100, y=300)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw2 = Image.open("Pictures for project/pexels-maud-slaats-2326936.jpg")
        # this opens the specific image in the folder named
        self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        #
        self.imgpanel2 = tk.Button(self.root, width=self.width, height=self.height, image=self.img2,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel2.place(x=1100, y=200)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw3 = Image.open("Pictures for project/pexels-edd-sylvia-nenntwich-2664419.jpg")
        # this opens the specific image in the folder named
        self.img3 = ImageTk.PhotoImage(self.imageRaw3.resize((int(self.width), int(self.height))))
        #
        self.imgpanel3 = tk.Button(self.root, width=self.width, height=self.height, image=self.img3,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel3.place(x=1100, y=400)
        # CreateImage =  panel.create_image(width,height,image = img)

    def SecondPage(self, UserID):
        if self.rootFrame is not None:
            self.rootFrame.destroy()
            self.ball = None
        self.rootFrame = self.create_animation_canvas() # accessing Tkinter, in a variable root, so everything can be stored inside the root
        self.rootFrame["bg"] = "#accb76"  # create a background colour for the page
        # self.rootFrame.grid(row=1, column=2)
        self.rootFrame.pack(fill="both", expand=True)

        # create text box labels
        self.OtherLabel = tk.Label(self.rootFrame, text="Other", font=("Arial", 25))
        self.OtherLabel.grid(row=1, column=75, padx=60, pady=60)
        # creates a coloured label
        self.OtherLabel["bg"] = "#fead90"

        # creates a button
        self.GrammarButton = tk.Button(self.rootFrame, text="Grammar", font=("Arial", 17), command=self.Grammar)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.GrammarButton.grid(row=1, column=150, padx=60, pady=60)
        self.GrammarButton["bg"] = "#dbce45"

        # creates a button
        self.BookLogButton = tk.Button(self.rootFrame, text="Book Log", font=("Arial", 17), command=self.BookLog)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.BookLogButton.grid(row=1, column=300, padx=60, pady=60)
        self.BookLogButton["bg"] = "#dbce45"

        # creates a button
        self.OwnQuestionsButton = tk.Button(self.rootFrame, text="Own Questions", font=("Arial", 17),
                                            command=self.OwnQuestions)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.OwnQuestionsButton.grid(row=1, column=225, padx=60, pady=60)
        self.OwnQuestionsButton["bg"] = "#dbce45"

        self.MusicButton = tk.Button(self.rootFrame, text="Music", font=("Arial", 17),
                                            command=self.Music)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.MusicButton.grid(row=1, column=350, padx=60, pady=60)
        self.MusicButton["bg"] = "#dbce45"

        # creates a button
        self.PrevPageButton = tk.Button(self.rootFrame, text="⬅️Previous Page", font=("Arial", 17),
                                        command=self.PrevPage)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.PrevPageButton.grid(row=4, column=75, padx=60, pady=60)
        self.PrevPageButton["bg"] = "#dbce45"

        self.width = 100
        self.height = 100

        self.imageRaw = Image.open("Pictures for project/pexels-cottonbro-studio-9668535(1).jpg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        #
        self.imgpanel = tk.Button(self.root, width=self.width, height=self.height, image=self.img,
                                  command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel.place(x=1100, y=300)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw2 = Image.open("Pictures for project/pexels-maud-slaats-2326936.jpg")
        # this opens the specific image in the folder named
        self.img2 = ImageTk.PhotoImage(self.imageRaw2.resize((int(self.width), int(self.height))))
        #
        self.imgpanel2 = tk.Button(self.root, width=self.width, height=self.height, image=self.img2,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel2.place(x=1100, y=200)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.imageRaw3 = Image.open("Pictures for project/pexels-edd-sylvia-nenntwich-2664419.jpg")
        # this opens the specific image in the folder named
        self.img3 = ImageTk.PhotoImage(self.imageRaw3.resize((int(self.width), int(self.height))))
        #
        self.imgpanel3 = tk.Button(self.root, width=self.width, height=self.height, image=self.img3,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel3.place(x=1100, y=400)

        # CreateImage =  panel.create_image(width,height,image = img)
        self.imageRaw4 = Image.open("Pictures for project/pexels-ritratto-visual-18212916.jpg")
        # this opens the specific image in the folder named
        self.img4 = ImageTk.PhotoImage(self.imageRaw4.resize((int(self.width), int(self.height))))
        #
        self.imgpanel4 = tk.Button(self.root, width=self.width, height=self.height, image=self.img4,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel4.place(x=1000, y=400)
        # CreateImage =  panel.create_image(width,height,image = img)

        # CreateImage =  panel.create_image(width,height,image = img)
        self.imageRaw5 = Image.open("Pictures for project/pexels-musicotravel-17896249.jpg")
        # this opens the specific image in the folder named
        self.img5 = ImageTk.PhotoImage(self.imageRaw5.resize((int(self.width), int(self.height))))
        #
        self.imgpanel5 = tk.Button(self.root, width=self.width, height=self.height, image=self.img5,
                                   command=self.PlaySound)
        # anel.grid(row=9)
        self.imgpanel5.place(x=900, y=400)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.HelpButton = tk.Button(self.rootFrame, text="Help", font=("Arial", 17), command=self.HelpNext)
        # under the root, with the text called simple maths with the font being arial at size 20, when clicked on,
        # the function simpleMaths will be accessed and processed
        self.HelpButton.grid(row=4, column=150)
        self.HelpButton["bg"] = "#abca76" \
                                ""


    def on_closing(self):
            if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
                self.root.destroy()  # the program will close if clicked.

        # for the whole section below
        # each individual function is called depending on what button the user has clicked on
        # each function then destroys the root window and calls the StartButtonForQuiz module while passing a specific
        # number to specifically know which function was accessed, therefore know which button to press and overall
        # know what quiz to output to the user

    def Alphabet(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(0)

    def Level1Maths(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(1)

    def Level1Colours(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(2)

    def Shapes(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(3)

    def Level2Maths(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(4)

    def Level2Colours(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(5)

    def Level3Maths(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(6)

    def LivingThingsAndTheirHabitat(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(7)

    def RhymingWords(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(8)

    def Punctuation(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(9)

    def NextPage(self):
        self.SecondPage(self.UserID)

    def Grammar(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        StartButtonForQuiz.StartButton(10)

    def PrevPage(self):
        self.FirstPage(self.UserID)

    def BookLog(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        BookLog.BookLog()

    def OwnQuestions(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        OwnQuestions.OwnQuestions()

    def Music(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        Songs.Songs()

    def PlaySound(self):
        value = random.randint(0,3)
        if value == 0:
            pygame.mixer.init()
            pygame.mixer.music.load("Music For Project/funny-and-clumsy-137251.mp3")
            pygame.mixer.music.play()
        elif value == 1:
            pygame.mixer.init()
            pygame.mixer.music.load("Music For Project/electronic-rock-king-around-here-15045.mp3")
            pygame.mixer.music.play()
        elif value == 2:
            pygame.mixer.init()
            pygame.mixer.music.load("Music For Project/happy-acoustic-guitar-background-music-122614.mp3")
            pygame.mixer.music.play()
        elif value == 3:
            pygame.mixer.init()
            pygame.mixer.music.load("Music For Project/funny-and-clumsy-137251.mp3")
            pygame.mixer.music.play()

    def Help(self):
        messagebox.showinfo(title = "What to do", message="Please click on a button on the left hand side to start "
                                                          "a quiz or click on the previous page button on the "
                                                          "right hand side to go to the next page. Additionally, you"
                                                          "can click on the pictures to hear some music")


    def HelpNext(self):
        messagebox.showinfo(title="What to do", message = "Please click on a button above to either put in "
                                                          "your own questions (Own Questions) or go into the book log"
                                                          "(Book Log) or start a quiz. You can also go back to the "
                                                          "previous page by clicking on the button on the left hand "
                                                          "side called Previous Page.Additionally, you can click "
                                                          "on the pictures to hear some music")


if __name__ == "__main__":
    Login.verification("test123", "test12345")
    LevelOptions()
