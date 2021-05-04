from tkinter import *
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from AniPlot import AniPlot # class for animations

window = Tk() # GUI Window
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

# initialization of flags
PEU_running = False

# when PEU button is pressed
def PEU():
    print("PEU button pressed")
    # bring flags into scope
    global PEU_running
    global PEU_plot
    if PEU_running:
        # code to stop animation
        PEUButton["text"] = "Start PEU" # change button text
        PEU_plot.ser.close() # close serial port so it can be reused
        del PEU_plot # delete AniPlot object to totally reset
        plt.close() # close figure window
        PEU_running = False
    else:
        # code to start animation
        PEUButton["text"] = "Stop PEU" # change button text
        PEU_plot = AniPlot('COM5', 921600, 150, 7, -0.5, 60.5) # call AniPlot with PEU arguments
        PEU_plot.animate() # set up the animation
        plt.show(block=False) # show the figure (block=false) is needed so code continues executing
        PEU_plot.ani.event_source.start() # start the animaton (needed because the block=false (i think))
        PEU_running = True
        
def exitProgram():
    print("Exit button pressed")
    plt.close() # close the figures
    window.destroy() # close gui and exit the program
    
window.title("GUI")
window.geometry('800x480')

exitButton  = Button(window, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

PEUButton = Button(window, text = "Start PEU", font = myFont, command = PEU, height = 2, width = 8)
PEUButton.pack()

window.mainloop()
print("Exited program")