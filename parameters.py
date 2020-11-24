from tkinter import *
import settings

# This could probably be cleaned up by making a class, the functions all take different inputs so it would be
# difficult to make them universal members of a class in that case. 

def writeAOO(LRL,URL,AtrAmp,AtrPW):
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
                if (j == "AOO"):
                    print("user global works, @AOO too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 4 values
                        del lines[count:count+4] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeAAI(LRL,URL,AtrAmp,AtrPW,ARP,AtrSense): ## Same variables a write AAI just different naming convention
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
                if (j == "AAI"):
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete values
                        del lines[count:count+6] 
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+4, "\n"+"ARP"+"\t"+ARP)
                        lines.insert(count+5, "\n"+"AtrSense"+"\t"+AtrSense+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+4, "\n"+"ARP"+"\t"+ARP)
                        lines.insert(count+5, "\n"+"AtrSense"+"\t"+AtrSense+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeVOO(LRL,URL,VentAmp,VentPW):
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
                if (j == "VOO"):
                    print("user global works, @VOO too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 4 values
                        del lines[count:count+4] 
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeVVI(LRL,URL,VentAmp,VentPW,VRP,VentSense):  ## This is an edge test case wrt this being at the end of the file, it doesn't work the same. Ghetto solution is to Write LRL during registration, works now
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
                if (j == "VVI"):
                    print("user global works, @VVI too")
                    print(count)
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    print(yesLRL)
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete values
                        del lines[count:count+6] 
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP)
                        lines.insert(count+5, "\n"+"VentSense"+"\t"+VentSense+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        del lines[count]
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP)
                        lines.insert(count+5, "\n"+"VentSense"+"\t"+VentSense+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

## NEW!!
## EDIT FUNCTION PARAMETERS AND INTERNALS

def writeDOO(LRL,URL,FAVD,AtrAmp,AtrPW,VentAmp,VentPW):
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
                        #delete next 7 values
                        del lines[count:count+7] #delete items from count to count+7
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"FAVD"+"\t"+FAVD)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)                        
                        lines.insert(count+5, "\n"+"VentAmp"+"\t"+VentAmp)                        
                        lines.insert(count+6, "\n"+"VentPW"+"\t"+VentPW)

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"FAVD"+"\t"+FAVD)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)                        
                        lines.insert(count+5, "\n"+"VentAmp"+"\t"+VentAmp)                        
                        lines.insert(count+6, "\n"+"VentPW"+"\t"+VentPW)                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

# writeAOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())
def writeAOOR(LRL,URL,MSR,AtrAmp,AtrPW,ActivityThresh,ReactTime,RespFact,RecoveryTime):
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  # This will bug if there is more than one user in the parameters file
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "AOOR"):
                    print("user global works, @AOOR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 9 values
                        del lines[count:count+9] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+5, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+6, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+7, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+8, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+5, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+6, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+7, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+8, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break


def writeAAIR(LRL,URL,MSR,AtrAmp,AtrPW,ARP,AtrSense,RateSmooth,ActivityThresh,ReactTime,RespFact,RecoveryTime):
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  # This will bug if there is more than one user in the parameters file
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "AAIR"):
                    print("user global works, @AAIR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 12 values
                        del lines[count:count+12] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+5, "\n"+"ARP"+"\t"+ARP)
                        lines.insert(count+6, "\n"+"AtrSense"+"\t"+AtrSense)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+RateSmooth)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+4, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+5, "\n"+"ARP"+"\t"+ARP)
                        lines.insert(count+6, "\n"+"AtrSense"+"\t"+AtrSense)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+RateSmooth)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

# writeVOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.VentAmplitudeInput.get(),self.VentPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())
def writeVOOR(LRL,URL,MSR,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime):
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  # This will bug if there is more than one user in the parameters file
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "VOOR"):
                    print("user global works, @VOOR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 9 values
                        del lines[count:count+9] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+5, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+6, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+7, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+8, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+5, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+6, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+7, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+8, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeVVIR(LRL,URL,MSR,VentAmp,VentPW,VRP,VentSense,RateSmooth,ActivityThresh,ReactTime,RespFact,RecoveryTime):
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  # This will bug if there is more than one user in the parameters file
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "VVIR"):
                    print("user global works, @VVIR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 12 values
                        del lines[count:count+12] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+5, "\n"+"VRP"+"\t"+VRP)
                        lines.insert(count+6, "\n"+"VentSense"+"\t"+VentSense)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+RateSmooth)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+5, "\n"+"VRP"+"\t"+VRP)
                        lines.insert(count+6, "\n"+"VentSense"+"\t"+VentSense)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+RateSmooth)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

# writeDOOR(self.LRLInput.get(),self.URLInput.get(),self.MaxSensorRateInput.get(),self.FixedAVDelayInput.get(),self.AtrApmlitudeInput.get(),self.AtrPulseWidthInput.get(),self.VentApmlitudeInput.get(),self.VentPulseWidthInput.get(),self.ActivityThresholdInput.get(),self.ReactionTimeInput.get(),self.ResponseFactorInput.get(),self.RecoveryTimeInput.get())

def writeDOOR(LRL,URL,MSR,FAVD,AtrAmp,AtrPW,VentAmp,VentPW,ActivityThresh,ReactTime,RespFact,RecoveryTime):
    file = open("parameters.txt","r")
    lines = file.readlines()
    file.close()
    count = 0
    for i in lines:
        i = i.strip() #removes problematic whitespace  ## TEST CASE??
        count = count+1 # count up the number of lines till we reach the user
        if (i==settings.user):  #user is a global variable, this checks to see if the user exists in the parameters file.
            for j in lines:  # This will bug if there is more than one user in the parameters file
                j = j.strip() #remove whitespace 
                count = count + 1  # count the number of lines until AOO is reached + lines to the current user (from previous loop)
                if (j == "DOOR"):
                    print("user global works, @DOOR too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 12 values
                        del lines[count:count+12] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"FAVD"+"\t"+FAVD)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+AtrAmp)
                        lines.insert(count+5, "\n"+"VRP"+"\t"+AtrPW)
                        lines.insert(count+6, "\n"+"Hysteresis"+"\t"+VentAmp)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+VentPW)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break
                        
                    else:
                        # write only
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"MSR"+"\t"+MSR)
                        lines.insert(count+3, "\n"+"FAVD"+"\t"+FAVD)
                        lines.insert(count+4, "\n"+"VentPW"+"\t"+AtrAmp)
                        lines.insert(count+5, "\n"+"VRP"+"\t"+AtrPW)
                        lines.insert(count+6, "\n"+"Hysteresis"+"\t"+VentAmp)
                        lines.insert(count+7, "\n"+"RateSmooth"+"\t"+VentPW)
                        lines.insert(count+8, "\n"+"ActivityThresh"+"\t"+ActivityThresh)
                        lines.insert(count+9, "\n"+"ReactTime"+"\t"+ReactTime)
                        lines.insert(count+10, "\n"+"RespFact"+"\t"+RespFact)
                        lines.insert(count+11, "\n"+"RecoveryTime"+"\t"+RecoveryTime)
                        

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

# def readAOO