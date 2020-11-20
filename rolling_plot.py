import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import serial
import getfloat

start_time = time.time()

port = 'COM5'
baud = 921600
timeout = 1
ylower = -0.5
yupper = 100.5
bufwidth = 300
numlines = 7

ser = serial.Serial(port, baud, timeout = 1)

fig, ax = plt.subplots()
ax.set_ylim(ylower,yupper)
line, = ax.plot([], [], lw = 2)

plotlays, plotcols = [numlines], ["black","red","blue","green","yellow","purple","orange"]
lines = []
for index in range(numlines):
    lobj = ax.plot([], [], lw = 2, color=plotcols[index])[0]
    lines.append(lobj)

def init():  # only required for blitting to give a clean slate.
    for line in lines:
        line.set_data([],[])
    return lines

x1, x2, x3, x4, x5, x6, x7 = [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth
y1, y2, y3, y4, y5, y6, y7 = [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth, [0]*bufwidth

def animate(data):
    #line.set_ydata(np.sin(i/50) )  # update the data.
    t = time.time()-start_time

    # not sure why this is here
    del x1[0]
    del x2[0]
    del x3[0]
    del x4[0]
    del x5[0]
    del x6[0]
    del x7[0]
    del y1[0]
    del y2[0]
    del y3[0]
    del y4[0]
    del y5[0]
    del y6[0]
    del y7[0]

    f_arr = getfloat.get_floats(ser,7)
    print (f_arr)

    x1.append(t)
    x2.append(t)
    x3.append(t)
    x4.append(t)
    x5.append(t)
    x6.append(t)
    x7.append(t)
    y1.append(float(*f_arr[0]))
    y2.append(float(*f_arr[1]))
    y3.append(float(*f_arr[2]))
    y4.append(float(*f_arr[3]))
    y5.append(float(*f_arr[4]))
    y6.append(float(*f_arr[5]))
    y7.append(float(*f_arr[6]))
    
    xlist = [x1, x2, x3, x4, x5, x6, x7]
    ylist = [y1, y2, y3, y4, y5, y6, y7]

    ax.relim()
    ax.autoscale_view()
    
    for lnum, line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum])

    return lines


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
    
ser.close()
