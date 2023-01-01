from tkinter import *

def start_Callback():
    global count

    print("Count Value is", count)
    var = count


main = Tk()

textVar = StringVar()
textVar.set("This is a Callback Demo")
count = 0

callLabel = Label(main, textvariable=textVar, font=("Arial",20), width= 30, height=15)
callLabel.grid(row=0, column=0)

callButton = Button(main, text="Start", font=("Arial",20), command=start_Callback)
callButton.grid(row=1, column=0)


main.mainloop()