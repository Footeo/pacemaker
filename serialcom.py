import serial
import struct
import time
import settings
import ctypes

#note DO NOT name the file serial.py, it will break the import feature
def sendparameters(params,switch): #params is a list with the parameters that need to be packed  Also if switch is 0 AOO if 1 VOO
##set up this dictionary to have whatever values are needed for transmission i.e. bytes,  etc.
    mode = {
        1: ['AOO',4],
        2: ['VOO',4],
        3: ['AAI',7],
        4: ['VVI',6],
        5: ['DOO',7],
        6: ['AOOR',9],
        7: ['VOOR',9],
        8: ['AAIR',13],
        9: ['VVIR',12],
        10: ['DOOR',12]
    }
    # mode_sel = mode.get(switch)
    # cur_mode = mode_sel[0] #use current mode later when transmitting

    print("Typecasted parameters",params)

    settings.ser.open()
    time.sleep(1)
    print("Serial Port Open?", settings.ser.is_open) 

    buff = ctypes.create_string_buffer(100)  

    ## AOO VOO

    # params = [['switch',switch],['LRL',0],['URL',0],['MSR',0],['FAVD',0],['AtrAmp',0],['VentAmp',0],['AtrPW',0],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] 

    struct.pack_into('<BBBHHHHddddHHHHHHdHHH',buff,0,22,85,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])# < means Little Endian - B = uint8. H = uint16. d = double (64)
                                                    # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
    print(buff)
    vals1 = settings.ser.write(buff)  #Write the bytes to the global serial port variable
    print("size of the package we are sending: ", vals1)
    print("calcsize",struct.calcsize("<BBBHHHHddddHHHHHHdHHH"))

    time.sleep(1) #1 sec delay

    count=0

    # buff = ctypes.create_string_buffer(87)  #new buffer  

    while True:  ## Should turn this infinite loop into a function call that will display the Egram
        
        struct.pack_into('<BB',buff,0,22,34)
        settings.ser.write(buff)
        #When reading here we have to read the entire serial packet and read off the last 2 doubles which are atr and vent pacing signals.

        vals2 = settings.ser.read(87) #read's argument is the size of the package we are sending/recieving
        print("reading... ", vals2)  

        #How are we going to unpack the two pacing pins? I think we have to unpack everything and then only use the last 2 values for the egram?

        print('unpack buff (in decimal): ', struct.unpack('<BBBHHHHddddHHHHHHHdHHHdd',buff))
        
        count += 1
        if count==3:
            break

    settings.ser.close()

    print("Serial Port Open?", settings.ser.is_open) 




# #Egram has to be done 