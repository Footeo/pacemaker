import serial
import struct
import time
import ctypes

ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 115200  
ser.timeout = .5
ser.dtr = 0

ser.open()
time.sleep(1)
print("Serial Port Info:", ser) 

buff = ctypes.create_string_buffer(14)  

struct.pack_into('<BBHHd',buff,0,22,85,120,10,4)# < means Little Endian - uint8,uint8,uint16,uint16,double
                                                # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
print(buff)
vals1 = ser.write(buff)  #Write the bytes to the global serial port variable
print("size of the package we are sending: ", vals1)
print("calcsize",struct.calcsize("<BBHHd"))

time.sleep(1) #1 sec delay

count=0

while True:  ## Should turn this infinite loop into a function call that will display the Egram
    struct.pack_into('<BB',buff,0,22,34)
    ser.write(buff)
    vals2 = ser.read(14) #read's argument is the size of the package we are sending/recieving
    print("reading... ", vals2)  #When you are sending bytes in '85' mode, this will not return anything. When you are sending bytes in '34' mode it will echo your parameters once unless you loop it somehow.
    


    print('unpack buff (in decimal): ', struct.unpack('<BBHHd',buff))
    count += 1
    if count==5:
        break

ser.close()

print("Serial Port Info:", ser) 
