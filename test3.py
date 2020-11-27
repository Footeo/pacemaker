import serial
import struct
import time
import settings
from ctypes import *

#note DO NOT name the file serial.py, it will break the import feature
def sendAOOtest(params,switch): #params is a list with the parameters that need to be packed  Also if switch is 0 AOO if 1 VOO
    if (switch==0):
        mode = "AOO" #might be more benificial to use the 0 or 1 that comes with the switch variable rather than defining a string
    else:
        mode = "VOO"

    settings.ser.open()
    # print("Serial Port Info:", settings.ser) 


    # print(params)
    # print(type(params[0]))
    # print("10000")
    buff = create_string_buffer(14)

    # LRL,URL, Atr/VentAmp, Atr/VentPW. 
    # package = struct.pack_into('<BBHHd',buff,0,22,34,params[0],params[3],params[2])  # < means Little Endian - uint16,uint16,uint16,uint16,float
                                                        #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)
    # print('binary', package)
    struct.pack_into('<BBHHd',buff,0,22,34,params[0],params[3],params[2])
    vals1 = settings.ser.write(buff)  #Write the bytes to the global serial port variable



    vals2 = settings.ser.read(14) #reads argument is the size of the package we are sending/recieving
    print(buff)
    print(vals1)
    print(vals2) 
    time.sleep(2) #2 sec delay



    # settings.ser.close()