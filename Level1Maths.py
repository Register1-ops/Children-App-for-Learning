import json
import tkinter as tk
from tkinter import messagebox
from functools import partial
import random
from PIL import ImageTk, Image
import pygame

import Login
import LoginPage
import StoreResults
import DisplayResults

class Maths:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/happy-acoustic-guitar-background-music-122614.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        self.countCorrect = 0  # initialises countCorrect to 0 as the amount of questions answered correctly right
        # now is 0
        self.TheirAnswer = []
        self.countWrong = 0  # initialises countWrong to 0 as the amount of questions answered correctly right now is 0
        self.QuestionUsed = []  # creates a list to store which questions have been used
        self.WrongQuestions = []  # creates a list of the questions the user got wrong
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("600x490")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Level 1 Maths")  # title refers to the name provided to the window. It appears on the top of the
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

        with open("Level1MathsQuestions.json",
                  "r") as infile:  # opens file, then closes file without needing to type code to do so
            self.questions = json.load(infile)

        self.SelectNextQuestion()  # calls the function, so it can be accessed
        self.PlaceButtons()  # then calls this function

        self.width = 500
        self.height = 200

        self.imageRaw = Image.open("Pictures for project/pexels-egor-kamelev-751687.jpg")
        # this opens the specific image in the folder named
        self.img = ImageTk.PhotoImage(self.imageRaw.resize((int(self.width), int(self.height))))
        #
        self.imgpanel = tk.Label(self.root, width=self.width, height=self.height, image=self.img)
        # anel.grid(row=9)
        self.imgpanel.place(x=50, y=300)
        # CreateImage =  panel.create_image(width,height,image = img)

        self.root.config(menu=self.menubar)  # configures the menubar so that the menubar actually shows up

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()

    def PlaceButtons(self):
        self.MyFrame = tk.Frame(self.root)  # creates a frame inside the root
        self.MyFrame.grid(row=1, column=2, padx=20, pady=20)  # places the buttons in relation to the frame created
        self.MyFrame["bg"] = "#abcd45"

        row = 1  # initialises row to 1
        self.LabelQuestion = tk.Label(self.MyFrame, text=self.CurrentQuestion["question"], font=("Arial", 20))
        # this accesses the question to ask, inside the CurrentQuestion to ask
        # the question is stored inside the label question variable
        self.LabelQuestion.grid(row=0, column=1, padx=20, pady=20)
        # places the question that is being asked in the row and column described
        for index in range(0, len(self.CurrentQuestion["answers"])):
            # for the length of 0, to the length of the options of answers that the users can be pick from i.e. 3
            answer = tk.Button(self.MyFrame, text=self.CurrentQuestion["answers"][index], font=("Arial", 15), padx=10,
                               pady=10,
                               command=partial(self.onAnswerClick, index))
            # this places the button for the answer with the text being the answer option that the user can pick
            answer.grid(row=row, column=2)
            answer["bg"] = "#da45a5"
            # places the button in adjacent rows
            row = row + 1
            # adds one to the row so the next button can be placed under
        return

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidently,
        # the page will close and be destroyed.

    def onAnswerClick(self, index):  # passes through the index of the answer options that the user clicked
        if self.CurrentQuestion["correct_answer"] == index:  # if the index of the correct answer is the same as
            # the answer that the user clicked
            self.countCorrect += 1  # then the countCorrect variables increases by one, due to the amount of correct
            # answers increases by 1


        else:
            self.countWrong += 1  # the countWrong variable is incremented by 1
            self.WrongQuestions.append(self.CurrentQuestion["id"])
            # the ID os the current question is chosen are appended to the WrongQuestions list so that it
            # can be accessed to later be outputted to the user so the user can then learn
            # off the questions they got wrong
            self.TheirAnswer.append(index)  # this appends the index of the of their answer
            # to the list called Their Array

        self.MyFrame.destroy()  # the frame is then destroyed
        if self.SelectNextQuestion():  # if it is true, if all questions have not been asked
            self.PlaceButtons()  # then it calls the function so it can ask more questions

        return

    def SelectNextQuestion(self):
        QuestionNumber = 0  # initialises the QuestionNumber variable to 0 so that it can be used later
        # and no error will occur as (it being undefined)
        status = True  # initialises status to True
        while status:  # while status is True
            QuestionNumber = random.randint(0, len(self.questions) - 1)  # chooses a random number between 0 and the
            # length of the list of questions
            if len(self.QuestionUsed) >= 2:  # if the length of the list of the question that have been used
                # are bigger then 2
                try:
                    StoreResults.storeResults(self.countWrong, self.countCorrect, "Level1Maths", self.WrongQuestions,
                                              self.TheirAnswer)
                    # calls the function storeResults and passes through the given parameters
                    pygame.mixer.music.stop()
                    self.root.destroy()  # the page is destroyed
                    Display()  # calls the functon display

                    return False
                    # returns false
                except Login.NotLoggedInError:  # if the user has not logged in, for security purposes of my program
                    # an error message box will be outputted to the user asking them to log in
                    tk.messagebox.showerror(title="Error", message="Not logged in")
                    self.root.destroy()  # the root window is destroyed
                    LoginPage.LoginPage()  # this line calls the module LoginPage, with the specific class LoginPage
                    return False


            elif QuestionNumber in self.QuestionUsed:
                #  if the question number is in the question used, then status is True
                status = True  # the another number is picked randomly
            else:
                status = False  # otherwise it comes out of the loop

        self.CurrentQuestion = self.questions[QuestionNumber]  # the CurrentQuestions stores the question of
        # the QuestionNumber index in the question json file
        # QuestionNumber is an integer which refers to a given question in the questions json file
        # the question is then stored in CurrentQuestion
        self.QuestionUsed.append(QuestionNumber)
        # ths QuestionNumber which refers to the specific question in the json file, is then appended to the list call
        # QuestionUsed which i use to verify which questions i have already outputted to the user
        return True


class Display():
    def __init__(self):
        QuizType = "Level1Maths"
        DisplayResults.Display(QuizType)


if __name__ == "__main__":
    Maths()