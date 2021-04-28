from tkinter import *
import tkinter.font as tkFont

win = Tk()
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

PEU_on = False
def PEU():
    print("PEU button pressed")
    global PEU_on
    if PEU_on:
        PEUButton["text"] = "Start PEU"
        PEU_on = False
    else:
        PEUButton["text"] = "Stop PEU"
        PEU_on = True
        import rolling_plot.py

def exitProgram():
	print("Exit Button pressed")
	win.destroy()	

win.title("GUI")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

PEUButton = Button(win, text = "Start PEU", font = myFont, command = PEU, height = 2, width =8 )
PEUButton.pack()

mainloop()