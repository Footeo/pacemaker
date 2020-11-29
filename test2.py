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

buff = ctypes.create_string_buffer(85)  
params = [['switch',1],['LRL',60],['URL',0],['MSR',0],['FAVD',0],['AtrAmp',4.5],['VentAmp',0],['AtrPW',10],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] # list to be sent
                        
struct.pack_into('<BBBHHHHddddHHHHHHdHHH',buff,0,22,85,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])# < means Little Endian - uint8,uint8,uint16,uint16,double
                                                    # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
# print(buff)
vals1 = ser.write(buff)  #Write the bytes to the global serial port variable
print("size of the package we are sending: ", vals1)
# print("calcsize",struct.calcsize("<BBHHd"))

time.sleep(1) #1 sec delay

count=0
vals2 = [0]
while True:  ## Should turn this infinite loop into a function call that will display the Egram
    struct.pack_into('<BB',buff,0,22,34)
    ser.write(buff)
    # print("Serial Port Info:", ser) 
 
    vals3 = ser.read(85) #read's argument is the size of the package we are sending/recieving
    vals2 = struct.unpack('<BBBHHHHddddHHHHHHdHHHdd',buff) 
    # print("reading... ", vals2)  #When you are sending bytes in '85' mode, this will not return anything. When you are sending bytes in '34' mode it will echo your parameters once unless you loop it somehow.
    # ser.write(buff)   

    
    print(vals3)
    print(vals2)
    # print("Serial Port Info:", ser) 


    # print('unpack buff (in decimal): ', struct.unpack('<BBHHd',buff))
    count += 1
    if count==5:
        break

ser.close()

# print("Serial Port Info:", ser) 
