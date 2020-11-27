from tkinter import *
import settings #user global
import serialcom #allows use of the send functions
import test3

def readAOOtest(switch):  #if switch is 0 -> AOO if switch is 1 -> VOO
    if (switch==0):
        mode = "AOO"
    else:
        mode = "VOO"
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
                if (j == mode):
                    print("user global works,"+mode+" too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+4] 
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(int(temp3[1]))   #If user sends floats into this it breaks :(   - Used to be int(). Maybe we should explicity typecast in the serialcom file
                        serialcom.sendAOOtest(send,switch)
                        break
                        
                    else:
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break

def readAOOVOO(switch):  #if switch is 0 -> AOO if switch is 1 -> VOO
    if (switch==0):
        mode = "AOO"
    else:
        mode = "VOO"
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
                if (j == mode):
                    print("user global works,"+mode+" too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+4] 
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendAOOVOO(send,switch)
                        break
                        
                    else:
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break

                        

                    ## make list variable, send that list into the serialcom -> AKA Call a function that exists within serialcom file

def readAAIVVI(switch): # switch is 0 -> AAI 1 -> VVI
    if (switch==0):
        mode = "AAI"
    else:
        mode = "VVI"
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        count = count+1 # count up the number of lines till we reach the user
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        if (i==settings.user):  #user is a global variable, oh lordy hope i haven't used it yet.
            for j in lines:
                j = j.strip() #remove whitespace 
                count = count + 1  #counts the current line
                if (j == mode):
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+6]  #temp holds all the saved parameters from .txt file
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendAAIVVI(send,switch)
                        break
                        
                    else:
                    
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break

def readDOO(): #no switch needed
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "DOO"):
                    print("user global works, @DOO too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+7]  #temp holds all the saved parameters from .txt file
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendDOO(send)
                        break
                        
                    else:
                    
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break



##COPIES FOR MODIFICATION
# modified

def readAOORVOOR(switch):  #if switch is 0 -> AOO if switch is 1 -> VOO
    if (switch==0):
        mode = "AOOR"
    else:
        mode = "VOOR"
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
                if (j == mode):
                    print("user global works,"+mode+" too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+9] 
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendAOORVOOR(send,switch)
                        break
                        
                    else:
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break

                        

                    ## make list variable, send that list into the serialcom -> AKA Call a function that exists within serialcom file

def readAAIRVVIR(switch): # switch is 0 -> AAI 1 -> VVI
    if (switch==0):
        mode = "AAIR"
    else:
        mode = "VVIR"
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        count = count+1 # count up the number of lines till we reach the user
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        if (i==settings.user):  #user is a global variable, oh lordy hope i haven't used it yet.
            for j in lines:
                j = j.strip() #remove whitespace 
                count = count + 1  #counts the current line
                if (j == mode):
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+12]  #temp holds all the saved parameters from .txt file
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendAAIRVVIR(send,switch)
                        break
                        
                    else:
                    
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break

def readDOOR(): #no switch needed
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "DOOR"):
                    print("user global works, @DOOR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        temp = lines[count:count+12]  #temp holds all the saved parameters from .txt file
                        send = []
                        for k in temp:
                            temp2 = k.strip("\n")
                            temp3 = temp2.split("\t")
                            send.append(temp3[1])
                        serialcom.sendDOOR(send)
                        break
                        
                    else:
                    
                        print("there is nothing available for transmission, please save parameters before sending")  ### SHOW TO USER SOMEHOW
                        break



