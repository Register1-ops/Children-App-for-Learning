import tkinter as tk
from tkinter import messagebox


class AgePage():
    def __init__(self, userID):
        self.root = tk.Tk()
        self.root["bg"] = "#adaa99"
        self.menubar = tk.Menu(self.root)
        self.root.geometry("800x800")
        self.root.title("Menu Page")
        self.userID = userID

        self.filemenu = tk.Menu(self.menubar, tearoff=3)
        self.filemenu.add_command(label="Close", command = self.on_closing)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Close Without question", command = exit)

        self.menubar.add_cascade(menu=self.filemenu, label = "Close application")
        
        self.root.config(menu= self.menubar)

        self.threeToFour = tk.Button(self.root, text="Ages 3 to 4", font=("Comic Sans", 20), command=self.AgeThreeToFour)
        self.threeToFour.grid(row = 100, column = 4, padx=10,pady=10)
        self.threeToFour["bg"] = "#edab47"

        self.FiveToSix = tk.Button(self.root, text="Ages 5 to 6", font=("Comic Sans", 20), command=self.AgeFiveToSix)
        self.FiveToSix.grid(row = 100, column = 5, padx=10,pady=10)
        self.FiveToSix["bg"] = "#edab47"

        self.SevenToEight = tk.Button(self.root, text="Ages 7 to 8 ", font=("Comic Sans", 20),
                                      command=self.AgeSevenToEight)
        self.SevenToEight.grid(row=100, column = 6, padx=10, pady=10)
        self.SevenToEight["bg"] = "#edab47"
        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


    def on_closing(self):
        
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()
            print("Goodbye, see you later")

    def AgeThreeToFour(self):
        self.root.destroy()
        Ages3To4MainPage.Ages3To4(self.userID)

    def AgeFiveToSix(self):
        print("!)")
        self.root.destroy()
        Ages5To6MainPage.Ages5To6(self.userID)

    def AgeSevenToEight(self):
        self.root.destroy()
        Ages7To8MainPage.Ages7To8(self.userID)


if __name__ == "__main__":
    AgePage(None)
