from tkinter import *
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from AniPlot import AniPlot # class for animations

PEU_port = 'COM5'
calibration_port = 'COM5'


window = Tk() # GUI Window
myFont = tkFont.Font(family = 'Helvetica', size = 36, weight = 'bold')

# initialization of flags
PEU_running = False
calibration_running = False

# when PEU button is pressed
def PEU():
    print("PEU button pressed")
    # bring flags into scope
    global calibration_running
    if calibration_running:
        calibration()
    global PEU_running
    global PEU_plot
    global PEU_port
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
        PEU_plot = AniPlot(PEU_port, 921600, 150, 7, -0.5, 60.5) # call AniPlot with PEU arguments
        PEU_plot.animate() # set up the animation
        plt.show(block=False) # show the figure (block=false) is needed so code continues executing
        PEU_plot.ani.event_source.start() # start the animaton (needed because the block=false (i think))
        PEU_running = True

# when calibration button is pressed
def calibration():
    print("Calibration button pressed")
    # bring flags into scope
    global PEU_running
    if PEU_running:
        PEU()
    global calibration_running
    global calibration_plot
    global calibration_port
    if calibration_running:
        # code to stop animation
        calibrationButton["text"] = "Start Calibration" # change button text
        calibration_plot.ser.close() # close serial port so it can be reused
        del calibration_plot # delete AniPlot object to totally reset
        plt.close() # close figure window
        calibration_running = False
    else:
        # code to start animation
        calibrationButton["text"] = "Stop Calibration" # change button text
        calibration_plot = AniPlot(calibration_port, 115200, 100, 4, -0.15, 0.15) # call AniPlot with PEU arguments
        calibration_plot.animate() # set up the animation
        plt.show(block=False) # show the figure (block=false) is needed so code continues executing
        calibration_plot.ani.event_source.start() # start the animaton (needed because the block=false (i think))
        calibration_running = True
        
def exitProgram():
    print("Exit button pressed")
    plt.close() # close the figures
    window.destroy() # close gui and exit the program
    
window.title("GUI")
window.geometry('800x480')

exitButton  = Button(window, text = "Exit", font = myFont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

PEUButton = Button(window, text = "Start PEU", font = myFont, command = PEU, height = 2, width = 8)
PEUButton.pack(side = LEFT, expand=YES)

calibrationButton = Button(window, text = "Start Calibration", font = myFont, command = calibration, height = 2, width = 16)
calibrationButton.pack(side = LEFT, expand=YES)

window.mainloop()
print("Exiting program")