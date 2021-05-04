import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

class AniPlot():
    def __init__(self,port, baud, bufwidth, numlines, ylower, yupper):
        self.port = port
        self.baud = baud
        self.bufwidth = bufwidth
        self.numlines = numlines
        self.ylower = ylower
        self.yupper = yupper
        # set start time
        self.start_time = time.time()

        # set up serial port
        self.ser = serial.Serial(self.port, self.baud, timeout = 1)

        #set up figue
        self.fig, self.ax = plt.subplots()
        self.ax.set_ylim(self.ylower,self.yupper)
        self.line, = self.ax.plot([], [], lw = 2) # lw is line width

        self.plotlays, self.plotcols = [self.numlines], ["black","red","blue","green","yellow","purple","orange"] # if you want more then 7 lines add another color
        self.lines = [] # lines holds line objects for ploting
        self.data = [] # data holds data points to plot

        # only need one list t (time) for all lines
        self.t = [0]*self.bufwidth

        for index in range(self.numlines):
            # create line object
            lineobj = self.ax.plot([], [], lw = 2, color=self.plotcols[index])[0]
            self.lines.append(lineobj)
            # create data object
            dataobj = [0]*self.bufwidth
            self.data.append(dataobj)

    def ani_init(self):  # only required for blitting to give a clean slate.
        for line in self.lines:
            line.set_data([],[])
        return self.lines

    def ani_update(self,i):
        # delete first entry in each list
        del self.t[0]
        for index in range(self.numlines):
            del (self.data[index])[0]

        # get data
        f_arr = getfloat.get_floats(self.ser,7)
        #print (f_arr)

        # append new data to lists
        self.t.append(time.time()-self.start_time)
        for index in range(self.numlines):
            self.data[index].append(float(*f_arr[index]))    

        #rescale plot
        self.ax.relim()
        self.ax.autoscale_view()
        
        # set line data
        for lnum, line in enumerate(self.lines):
            line.set_data(self.t, self.data[lnum])

        return self.lines

    def animate(self):
        self.ani = animation.FuncAnimation(self.fig, self.ani_update, init_func=self.ani_init, interval=20, blit=True, save_count=50)