import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

def rolling_plot(port, baud, bufwidth, numlines, ylower, yupper, timeout):
    # port = 'COM5'
    # baud = 921600
    # timeout = 1
    # ylower = -0.5
    # yupper = 100.5
    # bufwidth = 150
    # numlines = 7
    
    # set start time
    start_time = time.time()

    # set up serial port
    ser = serial.Serial(port, baud, timeout = 1)

    #set up figue
    fig, ax = plt.subplots()
    ax.set_ylim(ylower,yupper)
    line, = ax.plot([], [], lw = 2) # lw is line width
    
    plotlays, plotcols = [numlines], ["black","red","blue","green","yellow","purple","orange"] # if you want more then 7 lines add another color
    lines = [] # lines holds line objects for ploting
    data = [] # data holds data points to plot

    # only need one list t (time) for all lines
    t = [0]*bufwidth

    for index in range(numlines):
        # create line object
        lineobj = ax.plot([], [], lw = 2, color=plotcols[index])[0]
        lines.append(lineobj)
        # create data object
        dataobj = [0]*bufwidth
        data.append(dataobj)

    def init():  # only required for blitting to give a clean slate.
        for line in lines:
            line.set_data([],[])
        return lines

    def animate(i):
        # delete first entry in each list
        del t[0]
        for index in range(numlines):
            del (data[index])[0]

        # get data
        f_arr = getfloat.get_floats(ser,7)
        #print (f_arr)

        # append new data to lists
        t.append(time.time()-start_time)
        for index in range(numlines):
            data[index].append(float(*f_arr[index]))    

        #rescale plot
        ax.relim()
        ax.autoscale_view()
        
        # set line data
        for lnum, line in enumerate(lines):
            line.set_data(t, data[lnum])

        return lines

    ani = animation.FuncAnimation(fig, animate, init_func=init, interval=20, blit=True, save_count=50)

    plt.show()
        
    ser.close()

rolling_plot('COM5', 921600, 150, 7, -0.5, 60.5, 1)








