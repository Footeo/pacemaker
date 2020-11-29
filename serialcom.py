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
    print("Serial Port Info:", settings.ser) 

    buff = ctypes.create_string_buffer(100)  

    ## AOO VOO

    #send = [['switch',switch],['LRL',0],['URL',0],['MSR',0],['FAVD',0],['AtrAmp',0],['VentAmp',0],['AtrPW',0],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] 

    struct.pack_into('<BBBHHHHddddHHHHHHdHHH',buff,0,22,85,params[0][1],params[1][1],params[2][1],params[3][1],params[4][1],params[5][1],params[6][1],params[7][1],params[8][1],params[9][1],params[10][1],params[11][1],params[12][1],params[13][1],params[14][1],params[15][1],params[16][1],params[17][1],params[18][1])# < means Little Endian - uint8,uint8,uint16,uint16,double
                                                    # parameter 3. can be either 34 -> echo, or 85 -> set. Which is 0x22 and 0x55 in hex respectively.
    print(buff)
    vals1 = settings.ser.write(buff)  #Write the bytes to the global serial port variable
    print("size of the package we are sending: ", vals1)
    print("calcsize",struct.calcsize("<BBBHHHHddddHHHHHHdHHH"))

    time.sleep(1) #1 sec delay

    count=0

    buff = ctypes.create_string_buffer(87)  #new buffer  

    while True:  ## Should turn this infinite loop into a function call that will display the Egram
        
        # struct.pack_into('<BB',buff,0,22,34)
        # settings.ser.write(buff)
        #When reading here we have to read the entire serial packet and read off the last 2 doubles which are atr and vent pacing signals.

        #Vent signal is first 

        vals2 = settings.ser.read(87) #read's argument is the size of the package we are sending/recieving
        print("reading... ", vals2)  
        
        print(vals2[0])

        #How are we going to unpack the two pacing pins? I think we have to unpack everything and then only use the last 2 values for the egram?
        # print('unpack buff (in decimal): ', struct.unpack('<BBBHHHHddddHHHHHHHdHHHdd',buff))
        count += 1
        if count==3:
            break

    settings.ser.close()

    print("Serial Port Info:", settings.ser) 




# def sendAOOVOO(params,switch): #params is a list with the parameters that need to be packed  Also if switch is 0 AOO if 1 VOO
#     if (switch==0):
#         mode = "AOO" #might be more benificial to use the 0 or 1 that comes with the switch variable rather than defining a string
#     else:
#         mode = "VOO"
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     # LRL,URL, Atr/VentAmp, Atr/VentPW. 
#     package = struct.pack('<HHfH',params[0],params[1],params[2],params[3])  # < means Little Endian - uint32,uint32,float,uint32
#                                                         #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)

#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()

# def sendAAIVVI(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AOO if 1 VOO
#     if (switch==0):
#         mode = "AAI"
#     else:
#         mode = "VVI"
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     # params: LRL,URL, Atr/VentAmp, Atr/VentPW, ARP/VRP, Atr/VentSense.
#     package = struct.pack('<HHfHHf',params[0],params[1],params[2],params[3],params[4],params[5])  # < means Little Endian - uint32,uint32,float,uint32,uint32,float
#                                                                                                     #generally uint32s are BPM and float are Volts
                                                       
#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()

# def sendDOO(params): #no switch needed here
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     #params: LRL,URL,FAVD,AtrAmp,AtrPW,VentAmp,VentPW
#     package = struct.pack('<HHHfHfH',params[0],params[1],params[2],params[3],params[4],params[5],params[6])  # < means Little Endian - uint32,uint32,uint32,float,uint32,float,uint32
#                                                                                                     #generally uint32s are [BPM or ms] and float are [Volts]
                                                       
#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()


# def sendAOORVOOR(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AOOR if 1 VOOR
#     if (switch==0):
#         mode = "AOOR"
#     else:
#         mode = "VOOR"
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     # params: LRL,URL,MSR,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime
#     package = struct.pack('<HHHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8])  # < means Little Endian - uint32,uint32,float,uint32
#                                                         #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)

#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()

# def sendAAIRVVIR(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AAIR if 1 VVIR (use this info for Egram)
#     if (switch==0):
#         mode = "AAIR" 
#     else:
#         mode = "VVIR"
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     # params: LRL,URL,MSR,VentAmp,VentPW,VRP,VentSense,RateSmooth,ActivityThresh,ReactTime,RespFact,RecoveryTime
#     package = struct.pack('<HHHfHHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11])  # < means Little Endian - uint32,uint32,float,uint32,uint32,float
#                                                                                                     #generally uint32s are BPM and float are Volts
                                                       
#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()

# def sendDOOR(params): #no switch needed here
#     # settings.ser.open()
#     print("Serial Port Info:", settings.ser) 

#     print(params)
#     # params: LRL,URL,MSR,FAVD,AtrAmp,AtrPW,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime
#     package = struct.pack('<HHHHfHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11])  # < means Little Endian - uint32,uint32,uint32,float,uint32,float,uint32
#                                                                                                     #generally uint32s are [BPM or ms] and float are [Volts]
                                                       
#     settings.ser.write(package)  #Write the bytes to the global serial port variable

#     # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

#     # settings.ser.close()


# #Egram has to be done 