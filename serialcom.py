import serial
import struct
import time
import settings

#note DO NOT name the file serial.py, it will break the import feature
def sendAOOtest(params,switch): #params is a list with the parameters that need to be packed  Also if switch is 0 AOO if 1 VOO
    if (switch==0):
        mode = "AOO" #might be more benificial to use the 0 or 1 that comes with the switch variable rather than defining a string
    else:
        mode = "VOO"


    settings.ser.open()
    print("Serial Port Info:", settings.ser) 


    print(params)
    print(type(params[0]))
    print("10000")
    # LRL,URL, Atr/VentAmp, Atr/VentPW. 
    package = struct.pack('<HHHHd',22,34,params[0],params[3],params[2])  # < means Little Endian - uint16,uint16,uint16,uint16,float
                                                        #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)
    print('binary', package)
    settings.ser.write(package)  #Write the bytes to the global serial port variable

    settings.ser.read(16) #reads argument is the size of the package we are sending/recieving
    time.sleep(2)
    settings.ser.close()



def sendAOOVOO(params,switch): #params is a list with the parameters that need to be packed  Also if switch is 0 AOO if 1 VOO
    if (switch==0):
        mode = "AOO" #might be more benificial to use the 0 or 1 that comes with the switch variable rather than defining a string
    else:
        mode = "VOO"
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    # LRL,URL, Atr/VentAmp, Atr/VentPW. 
    package = struct.pack('<HHfH',params[0],params[1],params[2],params[3])  # < means Little Endian - uint32,uint32,float,uint32
                                                        #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)

    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()

def sendAAIVVI(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AOO if 1 VOO
    if (switch==0):
        mode = "AAI"
    else:
        mode = "VVI"
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    # params: LRL,URL, Atr/VentAmp, Atr/VentPW, ARP/VRP, Atr/VentSense.
    package = struct.pack('<HHfHHf',params[0],params[1],params[2],params[3],params[4],params[5])  # < means Little Endian - uint32,uint32,float,uint32,uint32,float
                                                                                                    #generally uint32s are BPM and float are Volts
                                                       
    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()

def sendDOO(params): #no switch needed here
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    #params: LRL,URL,FAVD,AtrAmp,AtrPW,VentAmp,VentPW
    package = struct.pack('<HHHfHfH',params[0],params[1],params[2],params[3],params[4],params[5],params[6])  # < means Little Endian - uint32,uint32,uint32,float,uint32,float,uint32
                                                                                                    #generally uint32s are [BPM or ms] and float are [Volts]
                                                       
    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()


def sendAOORVOOR(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AOOR if 1 VOOR
    if (switch==0):
        mode = "AOOR"
    else:
        mode = "VOOR"
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    # params: LRL,URL,MSR,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime
    package = struct.pack('<HHHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8])  # < means Little Endian - uint32,uint32,float,uint32
                                                        #https://docs.python.org/3/library/struct.html  (Scroll to charachters for reference)

    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()

def sendAAIRVVIR(params,switch): #params is a list with the parameters that need to be packed   Also if switch is 0 AAIR if 1 VVIR (use this info for Egram)
    if (switch==0):
        mode = "AAIR" 
    else:
        mode = "VVIR"
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    # params: LRL,URL,MSR,VentAmp,VentPW,VRP,VentSense,RateSmooth,ActivityThresh,ReactTime,RespFact,RecoveryTime
    package = struct.pack('<HHHfHHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11])  # < means Little Endian - uint32,uint32,float,uint32,uint32,float
                                                                                                    #generally uint32s are BPM and float are Volts
                                                       
    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()

def sendDOOR(params): #no switch needed here
    # settings.ser.open()
    print("Serial Port Info:", settings.ser) 

    print(params)
    # params: LRL,URL,MSR,FAVD,AtrAmp,AtrPW,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime
    package = struct.pack('<HHHHfHfHHHHH',params[0],params[1],params[2],params[3],params[4],params[5],params[6],params[7],params[8],params[9],params[10],params[11])  # < means Little Endian - uint32,uint32,uint32,float,uint32,float,uint32
                                                                                                    #generally uint32s are [BPM or ms] and float are [Volts]
                                                       
    settings.ser.write(package)  #Write the bytes to the global serial port variable

    # settings.ser.read(200) #reads argument is the size of the package we are sending/recieving

    # settings.ser.close()


#Egram has to be done 