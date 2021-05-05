#!/usr/bin/python
import serial
import struct

#
# Read num_floats floating point numbers over serial with a properly initialized 
# serial object (ser). 
#
def get_floats(ser, num_floats):
    f_arr = []
    for i in range (0, num_floats):
        data = ser.read(4)
        print(data)
        f_arr.append(struct.unpack('<f',data)) 
    return f_arr