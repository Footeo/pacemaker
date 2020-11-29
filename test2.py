import serial
import struct
import time
import ctypes

ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 115200  
ser.timeout = 2
ser.write_timeout = 2
ser.dtr = 0

ser.open()
print("Serial Port Open?",ser.is_open) 

buff = ctypes.create_string_buffer(85)  

params = [['switch',1],['LRL',120],['URL',120],['MSR',0],['FAVD',0],['AtrAmp',4.5],['VentAmp',0.0],['AtrPW',0.1],['VentPW',0.0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0.0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] # list to be sent

print("all params",params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])

vals = struct.pack('<BBBHHHHddddHHHHHHdHHH',22,34,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])# < means Little Endian - uint8,uint8,uint16,uint16,double
                                                    # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
# print(buff)
print("package vals ", vals)
ser.write(vals)  #Write the bytes to the global serial port variable

time.sleep(1)

ser.flush()
arr = bytes(85)
# print(arr)
vals2 = ser.read(85)
print(type(vals2))
vals2 = struct.unpack('<BBBHHHHddddHHHHHHdHHHdd',arr) 
print(arr)
# for i in range(0,85):

#     vals = ser.readline(i)
#     print(vals)



# time.sleep(1) #1 sec delay

# count=0
# while True:  

#     vals2 = struct.pack('<BBB',22,34,1)
#     print("sending", vals2)
#     ser.write(vals2)

#     time.sleep(1)

#     vals3 = ser.read(85)
#     print(vals3)
#     #read's argument is the size of the package we are sending/recieving
#     # vals2 = struct.unpack('<BBBHHHHddddHHHHHHdHHHdd',buff) 
#     # print("reading... ", vals2)  #When you are sending bytes in '85' mode, this will not return anything. When you are sending bytes in '34' mode it will echo your parameters once unless you loop it somehow.
#     # ser.write(buff)   

    
#     # print(vals3)
#     # print(vals2)
#     # print("Serial Port Info:", ser) 


#     # print('unpack buff (in decimal): ', struct.unpack('<BBHHd',buff))
#     count += 1
#     if count==2:
#         break

# ser.close()

# print("Serial Port Open?",ser.is_open) 
