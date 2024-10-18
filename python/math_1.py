import math
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Strength Calculator")
        self.root.geometry("500x270")
        self.root.resizable(False, False)

        self.bg = Image.open("window_bg.png")
        self.bg_tk = ImageTk.PhotoImage(self.bg)
        self.label = ttk.Label(self.root, image=self.bg_tk)
        self.label.place(x=0, y=0)
        text = "Input The Ammount Of \n Base Damage Of Your Weapons: "
        self.label = Label(self.root, text=text, font=("Century Gothic", 20))
        self.label.pack()

        self.entryBox = Entry(self.root, font=("Century Gothic", 30))
        self.entryBox.place(x=31, y=120)

        self.submitButton = Button(self.root, text="Submit", command=self.damageSubmit, font=("Century Gothic", 20))
        self.submitButton.place(x=31, y=190)

    def damageSubmit(self):
        global damage
        try:
            damage = int(self.entryBox.get())
        except ValueError:
            text = "Input The Ammount Of \n Base Damage Of Your Weapons:\nPlease input a valid number"
            self.label.config(text=text)
            return
        text = "Input Your Strength Level: "
        self.label.config(text=text)
        self.submitButton.config(command=self.strengthSubmit)
        self.entryBox.delete(0, END)

    def strengthSubmit(self):
        global strength
        try:
            strength = int(self.entryBox.get())
        except ValueError:
            text = "Input Your Strength Level:\nPlease input a valid number"
            self.label.config(text=text)
            return
        finalDamage = damage * pow(1.3, strength) + ((pow(1.3, strength) - 1) / 0.3)
        self.label.config(text="\nYour destinated damage")
        self.submitButton.config(text="Reset", command=self.resetSubmit)
        self.entryBox.insert(0, f"{finalDamage: .1f}")
        self.entryBox.config(state=DISABLED, disabledbackground="white", disabledforeground="black")

    def resetSubmit(self):
        self.entryBox.config(state=NORMAL)
        text = "Input The Ammount Of \n Base Damage Of Your Weapons: "
        self.label.config(text=text)
        self.entryBox.delete(0, END)
        self.submitButton.config(text="Submit", command=self.damageSubmit)

if __name__ == "__main__":
    mainWindow = Tk()
    app = App(mainWindow)
    mainWindow.mainloop()