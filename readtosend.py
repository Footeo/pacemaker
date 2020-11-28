from tkinter import *
import settings #user global
import serialcom #allows use of the send functions
import test3

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

                        send = [['switch',switch],['LRL',0],['URL',0],['MSR',0],['FAVD',0],['AtrAmp',0],['VentAmp',0],['AtrPW',0],['VentPW',0],['AtrSense',0],['VentSense',0],['VRP',0],['ARP',0],['PVARP',0],['RateSmooth',0],['ActivityThresh',0],['ReactTime',0],["RespFact",0],['RecoveryTime',0],['AtrSenseThresh',0],['VentSenseThresh',0],['Egram',0],['MaxActivity',0]] # list to be sent
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            if ((temp3[0] == 'AtrAmp') or (temp3[0] == 'VentAmp')):  #Typecasting 
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

















# def readAOOVOO(switch):  #if switch is 0 -> AOO if switch is 1 -> VOO
#     if (switch==0):
#         mode = "AOO"
#     else:
#         mode = "VOO"
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         i = i.strip() #removes problematic whitespace  
#         count = count+1 # count up the number of lines till we reach the user
#         if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
#             for j in lines:  
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
#                 if (j == mode):
#                     print("user global works,"+mode+" too")
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+4] 
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendAOOVOO(send,switch)
#                         break
                        
#                     else:
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break

                        

#                     ## make list variable, send that list into the serialcom -> AKA Call a function that exists within serialcom file

# def readAAIVVI(switch): # switch is 0 -> AAI 1 -> VVI
#     if (switch==0):
#         mode = "AAI"
#     else:
#         mode = "VVI"
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         count = count+1 # count up the number of lines till we reach the user
#         i = i.strip() #removes problematic whitespace  ## TEST CASE??
#         if (i==settings.user):  #user is a global variable, oh lordy hope i haven't used it yet.
#             for j in lines:
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  #counts the current line
#                 if (j == mode):
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+6]  #temp holds all the saved parameters from .txt file
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendAAIVVI(send,switch)
#                         break
                        
#                     else:
                    
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break

# def readDOO(): #no switch needed
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         i = i.strip() #removes problematic whitespace  ## TEST CASE??
#         count = count+1 # count up the number of lines till we reach the user
#         if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
#             for j in lines:  
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
#                 if (j == "DOO"):
#                     print("user global works, @DOO too")
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+7]  #temp holds all the saved parameters from .txt file
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendDOO(send)
#                         break
                        
#                     else:
                    
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break



# ##COPIES FOR MODIFICATION
# # modified

# def readAOORVOOR(switch):  #if switch is 0 -> AOO if switch is 1 -> VOO
#     if (switch==0):
#         mode = "AOOR"
#     else:
#         mode = "VOOR"
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         i = i.strip() #removes problematic whitespace  
#         count = count+1 # count up the number of lines till we reach the user
#         if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
#             for j in lines:  
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
#                 if (j == mode):
#                     print("user global works,"+mode+" too")
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+9] 
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendAOORVOOR(send,switch)
#                         break
                        
#                     else:
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break

                        

#                     ## make list variable, send that list into the serialcom -> AKA Call a function that exists within serialcom file

# def readAAIRVVIR(switch): # switch is 0 -> AAI 1 -> VVI
#     if (switch==0):
#         mode = "AAIR"
#     else:
#         mode = "VVIR"
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         count = count+1 # count up the number of lines till we reach the user
#         i = i.strip() #removes problematic whitespace  ## TEST CASE??
#         if (i==settings.user):  #user is a global variable, oh lordy hope i haven't used it yet.
#             for j in lines:
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  #counts the current line
#                 if (j == mode):
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+12]  #temp holds all the saved parameters from .txt file
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendAAIRVVIR(send,switch)
#                         break
                        
#                     else:
                    
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break

# def readDOOR(): #no switch needed
#     file = open("parameters.txt","r")
#     lines = file.readlines()
#     file.close()
#     count = 0
#     for i in lines:
#         i = i.strip() #removes problematic whitespace  ## TEST CASE??
#         count = count+1 # count up the number of lines till we reach the user
#         if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
#             for j in lines:  
#                 j = j.strip() #remove whitespace 
#                 count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
#                 if (j == "DOOR"):
#                     print("user global works, @DOOR too")
#                     yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
#                     if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
#                         temp = lines[count:count+12]  #temp holds all the saved parameters from .txt file
#                         send = []
#                         for k in temp:
#                             temp2 = k.strip("\n")
#                             temp3 = temp2.split("\t")
#                             send.append(temp3[1])
#                         serialcom.sendDOOR(send)
#                         break
                        
#                     else:
                    
#                         print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
#                         break



