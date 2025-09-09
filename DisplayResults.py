import random

import pygame

import Login
import MainPage
import StoreResults
import tkinter as tk # importing tkinter as tk so can use tk as abbreviation
from tkinter import messagebox # from the module tkinter, i import messagebox
import json
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Display():

    def __init__(self, QuizType):  # passes the variable QuizType which holds the type of quiz that the user entered
        pygame.mixer.init()
        pygame.mixer.music.load("Music For Project/happy-acoustic-guitar-background-music-122614.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.05)
        self.resultsWrongQID, self.resultsTheirAnswers, self.PercentageCorrect = StoreResults.getResults(QuizType)
        # calls the module Store results to get the results of the quiz that the user has just completed and
        # stores it in 3 separate variables since 3 values are being returned in the getResults function
        # they are all stored as arrays
        self.QuizType = QuizType # stores QuizType as a member variable to the class
        self.root = tk.Tk()  # creates a root window and displays it on the screen
        self.root["bg"] = "#ffbd99"  # creates a background colour fpr the root window
        self.menubar = tk.Menu(self.root)  # itself have dropdown menus, and that combination is what makes a menubar.
        # In order to make this work you must first create the menu, and then associate that menu with the window.
        self.root.geometry("1200x600")  # This method is used to set the dimensions of the Tkinter window and is used to
        # set the position of the main window on the user’s desktop.
        self.root.title("Results")  # title refers to the name provided to the window. It appears on the top of the
        # window & mostly found on the top left or center of the screen.

        self.backbutton = tk.Button(self.root, text = "Previous Page", font = ("Arial",20), command = self.PrevPage)
        self.backbutton.place(x = 500, y =530)
        self.backbutton["bg"] = "#aaddcc"

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

        self.Frames(QuizType) # passes the quiz type to a called function, Frames
        self.PlotGraphOfResults() # calls the function
        self.root.config(menu=self.menubar)  # configures the menubar so that the menubar actually shows up

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # this protocol to prompt the user to confirm
        # they want to exit
        self.root.mainloop()


    def Frames(self, QuizType):
        self.Frame = tk.Frame(self.root) # this creates a frame inside the root so that i can individually add
        # items to the frame without disrupting the root as a well
        self.Frame.pack()  # pack() organizes widgets in horizontal and vertical boxes that are limited to left,
        # right, top, bottom positions offset and relative to each other within a frame.
        self.FrameTop = tk.Frame(self.Frame) # a frame is instantiated inside the Frame that was declared above
        self.FrameTop["bg"] = "#ffbd00" # the frame is given a background colour
        self.FrameBottom = tk.Frame(self.Frame) # another frame is declared from the frame above
        # two frames are declared since I would like to have two parts to my root window and two frames
        # allow the root window to be divided into 2
        self.FrameTop.pack(side="top", fill="x", expand = True )
        self.FrameBottom.pack(side="bottom", fill="x", expand=True)
        # both lines above pack both FrameTop and FrameBottom to ensure that both
        # frames have separate sides that they fill


        self.FrameGraph = tk.Frame(self.FrameTop) # This further creates a division inside
        # the FrameTop so that i can include a graph
        self.FrameGraph.pack() # # pack() organizes widgets in horizontal and vertical boxes that are limited to left,
        # right, top, bottom positions offset and relative to each other within a frame.
        self.FrameCurrent = tk.Frame(self.FrameBottom) # A frame can be used as a foundation class to implement
        # complex widgets. It is used to organize a group of widgets. This organises the FrameBottom to contain an
        # inside frame called FrameCurrent which wil hold the questions they got wrong in the current quiz
        self.FrameCurrent.grid(row = 3 , column = 3) # this part places where the Frame will be placed in
        # the root window
        self.FramePrevious = tk.Frame(self.FrameBottom) # # A frame can be used as a foundation class
        # to implement complex widgets. It is used to organize a group of widgets. This organizes the FrameBottom
        # to contain an inside frame called FramePrevious which will hold previous questions they got wrong
        self.FramePrevious.grid(row = 3, column = 8) # this places the Frame inside the root window

        self.FramePrevious["bg"] = "#aafbaa"
        self.FrameCurrent["bg"] = "#ffbbaa"
        self.FrameGraph["bg"] = "#ffbbaa"
        self.FrameBottom["bg"] = "#aafbaa"
        self.FrameTop["bg"] = "#ffbbaa"

        results = [] # results is instantiated as an empty list
        numberOfSamples = 2  # the number of samples that are taken to output to the user is defined here
        for i, value in enumerate(self.resultsWrongQID):  # value: enumerate gives index and value,
            # but we do not need value.
            # if we didn't do (i, value), i would have been a tuple instead which is not want i need in the code
            # Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
            # This enumerated object can then be used directly for loops or converted into a list of tuples using
            # the list() function.
            qAndACombo = [] # this sets the variable qAndACombo as an empty list
            for j, value in enumerate(self.resultsWrongQID[i]):
                # value: enumerate gives index and value,
                # but we do not need value.
                # if we didn't do (j, value), j would have been a tuple instead which is not want i need in the code
                # Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.
                # This enumerated object can then be used directly for loops or converted into a list of tuples using
                # the list() function. since resultsWrongQID is stored as an array within an array,
                # this loop is needed to loop through the inside array which actually hold the values
                qAndACombo.append((self.resultsWrongQID[i][j], self.resultsTheirAnswers[i][j]))
                # this appends both the specific question ID with their corresponding answer as an array,
                # within qAnACombo which is an array as well
            results.extend(qAndACombo)  # this extends, which is another way of appending, but with lists
            # instead of singular values, qAndACombo to the results lists
        results = set(results) # It changes results from a list data type into a set data type.
        # The reason we do that is because a list can contain duplicates but a set can't
        PastQuestionsDisplay = random.sample(results, min(numberOfSamples, len(results)))
        # this gets a sample with a minimum sample of 2 till how many results the user has got, if they have less 2,
        # then that means that, that number of samples is used
        # this gets 2 samples from results which holds
        # the question ID and corresponding answer to output to the user


        with open(f"{QuizType}Questions.json", "r") as infile:  # opens file, then closes file without needing to type code to do so
            self.questions = json.load(infile)  # stores what is stored in the json file inside the questions
            # variable, this stores the questions, answer options and the correct-answer


        row = 2 # initiates row to 2

        # Label is a Label widget with an Arial font and a size of 20
        # Statement is a Label
        self.Statement = tk.Label(self.FramePrevious, text="Previous Questions you got wrong",
                                  font=("Arial", 15))
        self.Statement.grid(row=0, column=0, columnspan=3)
        self.Statement["bg"] = "#aafbaa"
        # the label, statement is then placed in a specific row and column with a column span of 3
        # so that it spans across 3 columns

        # Label is a Label widget with an Arial font and a size of 20
        # Questions Label is a Label
        self.QuestionsLabel = tk.Label(self.FramePrevious, text="Questions", font=("Arial",13))
        self.QuestionsLabel.grid(row=1, column=0)
        self.QuestionsLabel["bg"] = "#aafbaa"
        # Then the label is placed in specific row and column

        ## Label is a Label widget with an Arial font and a size of 20
        # TheirAnswerLabel Label is a Label
        # Then the label is placed in specific row and column
        self.TheirAnswerLabel = tk.Label(self.FramePrevious, text="Your Answers", font=("Arial", 13))
        self.TheirAnswerLabel.grid(row=1, column=2)
        self.TheirAnswerLabel["bg"] = "#aafbaa"
        ## Label is a Label widget with an Arial font and a size of 20
        # CorrectAnswerLabel is a Label
        # Then the label is placed in specific row and column
        self.CorrectAnswerLabel = tk.Label(self.FramePrevious, text="Correct Answer", font=("Arial", 13))
        self.CorrectAnswerLabel.grid(row=1, column=4)
        self.CorrectAnswerLabel["bg"] = "#aafbaa"

        for questionIndex, answerIndex in PastQuestionsDisplay:  # for the indexes of both the question
            # and the answers in the PastQuestionsDisplay array stored as [questionIndex, answerIndex]
            question = self.questions[questionIndex]["question"]
            # this accesses the specific question
            theirAnswer = self.questions[questionIndex]["answers"][answerIndex]
            correctAnswerIndex = self.questions[questionIndex]["correct_answer"]
            correctAnswer = self.questions[questionIndex]["answers"][correctAnswerIndex]


            # Label is a Label widget with an Arial font and a size of 20
            # Questions Label is a Label
            self.QuestionsLabel = tk.Label(self.FramePrevious, text= question, font=("Arial", 10))
            self.QuestionsLabel.grid(row=row, column=0)
            self.QuestionsLabel["bg"] = "#aafbaa"
            # Then the label is placed in specific row and column

            ## Label is a Label widget with an Arial font and a size of 20
            # TheirAnswerLabel Label is a Label
            # Then the label is placed in specific row and column
            self.TheirAnswerLabel = tk.Label(self.FramePrevious, text= theirAnswer, font=("Arial", 10))
            self.TheirAnswerLabel.grid(row=row, column=2)
            self.TheirAnswerLabel["bg"] = "#aafbaa"

            ## Label is a Label widget with an Arial font and a size of 20
            # CorrectAnswerLabel is a Label
            # Then the label is placed in specific row and column
            self.CorrectAnswerLabel = tk.Label(self.FramePrevious, text=correctAnswer, font=("Arial", 10))
            self.CorrectAnswerLabel.grid(row=row, column=4)
            self.CorrectAnswerLabel["bg"] = "#aafbaa"


            row += 1


        # Label is a Label widget with an Arial font and a size of 20
        # Statement is a Label
        self.Statement = tk.Label(self.FrameCurrent, text = "On this quiz you got these questions wrong", font=("Arial",15))
        self.Statement.grid(row = 0, column =0, columnspan=3)
        self.Statement["bg"] = "#ffbbaa"
        # the label, statement is then placed in a specific row and column with a column span of 3
        # so that it spans across 3 columns

        # Label is a Label widget with an Arial font and a size of 20
        # Questions Label is a Label
        self.QuestionsLabel = tk.Label(self.FrameCurrent, text = "Questions", font=("Arial",13))
        self.QuestionsLabel.grid(row = 1, column = 0, padx=15, pady=15)
        self.QuestionsLabel["bg"] = "#ffbbaa"
        # Then the label is placed in specific row and column

        ## Label is a Label widget with an Arial font and a size of 20
        # TheirAnswerLabel Label is a Label
        # Then the label is placed in specific row and column
        self.TheirAnswerLabel = tk.Label(self.FrameCurrent, text="Your Answer", font=("Arial", 13))
        self.TheirAnswerLabel.grid(row=1, column=2,padx=15, pady=15)
        self.TheirAnswerLabel["bg"] = "#ffbbaa"

        ## Label is a Label widget with an Arial font and a size of 20
        # CorrectAnswerLabel is a Label
        # Then the label is placed in specific row and column
        self.CorrectAnswerLabel = tk.Label(self.FrameCurrent, text="Correct Answer", font=("Arial", 13))
        self.CorrectAnswerLabel.grid(row=1, column=4)
        self.CorrectAnswerLabel["bg"] = "#ffbbaa"

        with open(f"{QuizType}Questions.json","r") as infile:
            # opens file, then closes file without needing to type code to do so
            self.questions = json.load(infile)
        # this opens the file with the QuizType as a json file
        # the quiz type is the same as the module names therefore an if statement is not needed as it has been done a
        # more concise way rather than  a bunch of if statements

        rowNum = 2 # sets the rowNum to 2, not a member variable as it doesn't need to be a global variable



        for i, index in enumerate(self.resultsWrongQID[-1]):
            # The enumerate() function is a built-in function that returns an enumerate object.
            # This lets you get the index of an element while iterating over a list.
            # This accesses the index of the last item (ID in this case) in the resultsWrongID list
            # this loops through the list of wrong answers that they got in the current test that they did
            rowNum += 1  # add 1 to the row number so that the results are displayed under each other
            accessQuestion = self.questions[index] # accesses the actual question inside the json
            # list question with a given index
            self.questionLabel = tk.Label(self.FrameCurrent, text = accessQuestion["question"], font = ("Arial", 10))
            # creates a Label inside the FrameCurrent with the text being the question that they got wrong
            self.questionLabel.grid(row = rowNum, column = 0)
            self.questionLabel["bg"] = "#ffbbaa"
            # this places where the question should go, with a given row

            self.theiranswerLabel = tk.Label(self.FrameCurrent,
                                      text=accessQuestion["answers"][self.resultsTheirAnswers[-1][i]],
                                      font=("Arial", 10))
            self.theiranswerLabel.grid(row=rowNum, column=2)
            self.theiranswerLabel["bg"] = "#ffbbaa"
            # this label shows the answer that they entered for the question using the answer part of
            # the certain question that they answered in the json file.

            self.actualAnswerLabel = tk.Label(self.FrameCurrent, text= accessQuestion["answers"][accessQuestion["correct_answer"]], font=("Arial", 10))
            self.actualAnswerLabel.grid(row=rowNum, column=4)
            self.actualAnswerLabel["bg"] = "#ffbbaa"
            # this label shows the actual answer for the question, by accessing the json file for the quiz type
            # then the label is placed by a row number and column

    def PlotGraphOfResults(self):
        fig = matplotlib.figure.Figure(figsize=(20,7), dpi = 50)
        # Matplotlib Fig size is a method from the pyplot class which allows you to change the dimensions of the graph.
        # As every dimension in generated graphs is adjusted by the library,
        # it can be quite difficult to visualize data in a proper format. As a result,
        # the fig-size method is very useful to customize the dimensions as well as layouts of the graphs.

        ax = fig.add_subplot() # The add_subplot() method figure module of matplotlib library is
        # used to add an Axes to the figure as part of a subplot arrangement.

        canvas = FigureCanvasTkAgg(fig, master= self.FrameGraph)
        # Matplotlib has a special module called backends which contains various submodules for
        # integration with other popular libraries such as Tkinter. The backend library for Tkinter is
        # called backend_tkagg, which holds various Classes which can be used for Matplotlib and Tkinter integration.
        # This is where we will import FigureCanvasTkAgg from.

        canvas.get_tk_widget().pack()
        # pack() organizes widgets in horizontal and vertical boxes that are limited to left,
        # right, top, bottom positions offset and relative to each other within a frame.

        toolbar = NavigationToolbar2Tk(canvas, self.FrameGraph, pack_toolbar=False)
        # If you are familiar with Matplotlib, you will notice that we are currently missing the Navigation Toolbar
        # which provides us with helpful features to interact with the graph,
        # such as Zoom in, Zoom out, Save Graph, etc.
        # To enable these features, we must add NavigationToolbar2Tk to our Tkinter GUI.
        # From the same place where we imported FigureCanvasTkAgg, we will also import NavigationToolbar2Tk.
        toolbar.update()
        # update works by performing the following steps in a loop until no events are serviced in one iteration:
        # Service the first event whose scheduled time has come. If no such events are found, service all
        # events currently in the idle queue, but not those added once this step starts.
        toolbar.pack(anchor="w", fill = tk.X)
        # this packs the toolbar to anchor it to the right of the frame and fills it in the x axis

        lengthAttempts = len(self.PercentageCorrect)
        # this obtains the length of the correct answers that user has been successfully able to answer correctly
        x = list(range(1,lengthAttempts+1))
        # stores the range of the attempts as a list from 1 to the length of the attempts it took
        y = self.PercentageCorrect
        # y stores the percentage of the specific correct answer
        ax.set_xlabel("Number of tries", fontsize = 25)
        ax.set_ylabel("Percentage", fontsize = 20)
        ax.set_title("Result History", fontsize = 20)


        ax.plot(x, y)  # plots the x and y-axis on the graph
        canvas.draw() # this draws the graph
        return

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):  # if the messagebox was clicked
            self.root.destroy()  # the program will close if clicked.
        # if the user wants to exit the application the program will ask the user as a form of a messagebox,
        # if they want to quit
        # if the user clicks yes, as the messagebox will ask the user to choose between yes
        # and no since the user may have clicked on the exit button accidentally,
        # the page will close and be destroyed.

    def PrevPage(self):
        self.root.destroy()
        pygame.mixer.music.stop()
        MainPage.LevelOptions()
