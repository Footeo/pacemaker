from tkinter import *
import settings #user global
import serialcom #allows use of the send functions

def readparameters(switch):  # 1-10
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

    mode_sel = mode.get(switch)
    cur_mode = mode_sel[0]
    print("Current mode",cur_mode)
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == cur_mode):
                    print("user global works,"+cur_mode+" too")
                    yesLRL = lines[count].split("\t") # checks if LRL exists 

                    # Correct typecasting/range

                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+mode_sel[1]] 

                        print(temp)

                        send = [['switch',switch],['LRL',0],['URL',0],['MSR',0],['FAVD',0],['AtrAmp',0],['VentAmp',0],['AtrPW',0],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0]] # list to be sent
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            if ((temp3[0] == 'AtrAmp') or (temp3[0] == 'VentAmp') or (temp3[0] == 'AtrPW') or (temp3[0] == 'VentPW') or (temp3[0] == 'ActivityThresh')):  #Typecasting 
                                print("float value",temp3[1])
                                temp3[1] = float(temp3[1])
                            else:
                                print("int value",temp3[1])
                                temp3[1] = int(temp3[1])
                            for l in send:
                                if(l[0]==temp3[0]): # checks to see if parameter in temp3 is in send
                                    l[1] = temp3[1] # assign parameter to send

                        serialcom.sendparameters(send,switch)
                        print(send)
                        
                    else:
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break
