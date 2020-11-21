#!/usr/bin/python
import serial
import struct
import getfloat

ser = serial.Serial('COM4', 921600, timeout = 1)
print(ser.name)

count = 0
while (count < 500):
    f_arr = getfloat.get_floats(ser,2);
    print(f_arr)
    count = count + 1
    
ser.close()

print ("fuck off")