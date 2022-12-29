from tkinter import *
import os
import time
from piat.client.client import Client, setup
from tabulate import tabulate



ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print("Initializing...")
print("ROOT_DIR is", ROOT_DIR)
config = setup(from_path=True, cwd=f"{ROOT_DIR}/piat")
client = Client(config['serverUrl'], config['serverPort'], config['id'])
uuid = ""

def lucasArt():
    seed_var = seedEntry.get()
    print("Submitting Prompt: {}".format(seed_var))

main = Tk()

# Frames
headerFrame = Frame(main)
entryFrame = Frame(main)
previewFrame = Frame(main)
pixelFrame = Frame(main)
processFrame = Frame(main)

headerFrame.grid(row=0, columnspan=3)
entryFrame.grid(row=1, column=0)
previewFrame.grid(row=1, column=1)
pixelFrame.grid(row=1, column=2)
processFrame.grid(row=2, column=1, columnspan=2)

# Declaration
seed_var = StringVar()
seed_var.set("Happy Students")
winWidth = 40
winHeight = 20

# Header Section
guiHeader = Label(headerFrame, text="Wonders L.U.C.A.S. Art!", font=("Arial", 20))
guiHeader.grid(row=0, column=0)

# Entry Section 
seedLabel = Label(entryFrame, text= "Please enter a seed prompt to\nL.U.C.A.S. A.I. Server", font=("Arial",15))
seedEntry = Entry(entryFrame, textvariable = seed_var, font=("Arial", 15), width=30)
seedSubmit = Button(entryFrame, text="Submit", font=("Arial", 15), command = lucasArt)

seedLabel.grid(row=0, column=0)
seedEntry.grid(row=1, column=0)
seedSubmit.grid(row=2, column=0)

# Preview Section
previewWindow = Label(previewFrame, bg = 'white', width=winWidth, height=winHeight)
previewLabel = Label(previewFrame, text = "Preview Window", font = ("Arial", 15))

previewWindow.grid(row=0, column=0)
previewLabel.grid(row=1, column=0)

# Pixelized Section
pixelWindow = Label(pixelFrame, bg = 'grey', width=winWidth, height=winHeight)
pixelLabel = Label(pixelFrame, text='Pixelized Window', font=("Arial",15))

pixelWindow.grid(row=0, column=0)
pixelLabel.grid(row=1, column=0)

main.mainloop()