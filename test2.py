import serial
import threading
import struct
import time
import ctypes

ser = serial.Serial()
ser.port = 'COM4'
ser.baudrate = 115200  
ser.timeout = .5
ser.dtr = 0


def infiniteTransmit(count,buff):  ## Should turn this infinite loop into a function call that will display the Egram
        
    while True:
        #When reading here we have to read the entire serial packet and read off the last 2 doubles which are atr and vent pacing signals.

        buff = bytearray(100)
        struct.pack_into('<BBBHHHHddddHHHHHHdHHHdd',buff,0,22,34,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1],0.0,0.0)   
        #going to test sending in a full length string, (none of these should be written, just dummy variables)
        ser.write(buff)

        time.sleep(1)

        buff = ser.read(100) #read's argument is the size of the package we are sending/recieving

        print(buff)  
        print(type(buff))
        #How are we going to unpack the two pacing pins? I think we have to unpack everything and then only use the last 2 values for the egram?

        vals2 = struct.unpack_from('<BHHHHddddHHHHHHdHHHdd', buff, offset=0)


        print(vals2)


        time.sleep(.5)
        count += 1
        if count==3:
            break

count=0
ser.open()
thread = threading.Thread(target=ser.read(100), args=(ser.port))
thread.start()
time.sleep(1)
print("Serial Port Info:", ser) 

buff = ctypes.create_string_buffer(69)  
params = [['switch',1],['LRL',120],['URL',240],['MSR',0],['FAVD',0],['AtrAmp',4.5],['VentAmp',0],['AtrPW',10],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] # list to be sent
                        
struct.pack_into('<BBBHHHHddddHHHHHHdHHH',buff,0,22,85,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])# < means Little Endian - uint8,uint8,uint16,uint16,double
                                                    # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
# print(buff)
vals1 = ser.write(buff)  #Write the bytes to the global serial port variable

# time.sleep(1) #1 sec delay

# write the echo byte

buff2 = ctypes.create_string_buffer(100)

infiniteTransmit(count,buff2)



##THIS WORKS!! (sometimes)
# struct.pack_into('<BB',buff,0,22,34)
# ser.write(buff)


# buff = ser.read(83)  # 67 + 16 for the atr/vent

# print(buff)
# print(type(buff))

# #NOTE If this throws errors, unplug the FRDM board, it's a finniky mofo

# vals2 = struct.unpack_from('<BHHHHddddHHHHHHdHHHdd', buff, offset=0)   #FUCK THIS FORMAT STRING UGH (so if you add the d's at the end one at a time all of a sudden it works) 

# print(vals2) 

ser.close()
