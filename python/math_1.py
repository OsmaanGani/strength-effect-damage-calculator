import math
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def resetSubmit():
    label.config(text="Input The Ammount Of \n Damage Of Your Weapons: ")
    entryBox.delete(0, END)
    submitButton.config(text="Submit", command=damageSubmit)

def strengthSubmit():
    global strength
    strength = int(entryBox.get())
    finalDamage = damage * pow(1.3, strength) + ((pow(1.3, strength) - 1) / 0.3 )
    label.config(text="\nYour Final Damage Is")
    submitButton.config(text="Reset", command = resetSubmit)
    entryBox.insert(0, f"{finalDamage: .1f}")

def damageSubmit():
    global damage
    damage = int(entryBox.get())
    label.config(text="Input The Level Of \n Strength")
    submitButton.config(command= strengthSubmit)
    entryBox.delete(0, END)

mainWindow = Tk()
mainWindow.geometry("500x270")
mainWindow.title("Minecraft Strength Counter")

mainWindow.resizable(False, False)

bg = Image.open("window_bg.png")
bg_tk = ImageTk.PhotoImage(bg)
label = ttk.Label(mainWindow,image= bg_tk)
label.place(x=0,y=0)

label = Label(mainWindow, text="Input The Ammount Of \n Base Damage Of Your Weapons: ", font=("Century Gothic", 20))
label.pack()

entryBox = Entry(mainWindow, font=("Century Gothic", 30))
entryBox.place(x=31,y=120)

submitButton = Button(mainWindow, text="Submit", command = damageSubmit, font=("Century Gothic", 20))
submitButton.place(x=31,y=190)

mainWindow.mainloop()
