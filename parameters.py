from tkinter import *
import settings
import screens

# This could probably be cleaned up by making a class, the functions all take different inputs so it would be
# difficult to make them universal members of a class in that case. 

def writeAOO(LRL,URL,AtrAmp,AtrPW,APR):
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
                if (j == "AOO"):
                    print("user global works, @AOO too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 4 values
                        del lines[count:count+5] #delete items from count to count+4
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

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
                        lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeAAI(LRL,URL,AtrAmp,AtrPW,APR): ## Same variables a write AAI just different naming convention
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
                        #delete next 4 values
                        del lines[count:count+5] #delete items from count-1 to count+3
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"AtrAmp"+"\t"+AtrAmp)
                        lines.insert(count+3, "\n"+"AtrPW"+"\t"+AtrPW)
                        lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

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
                        lines.insert(count+4, "\n"+"APR"+"\t"+APR+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeVOO(LRL,URL,VentAmp,VentPW,VRP):
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
                if (j == "VOO"):
                    print("user global works, @VOO too")
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 4 values
                        del lines[count:count+5] #delete items from count-1 to count+3
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

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
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

def writeVVI(LRL,URL,VentAmp,VentPW,VRP):  ## This is an edge test case wrt this being at the end of the file, it doesn't work the same. Ghetto solution is to Write LRL during registration, works now
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
                if (j == "VVI"):
                    print("user global works, @VVI too")
                    print(count)
                    yesLRL = lines[count].split("\t") # splits potential LRL into a list of 2 things
                    print(yesLRL)
                    if yesLRL[0] == "LRL":	 #index the list at 0 check if its a match
                        #delete next 4 values
                        del lines[count:count+5] #delete items from count-1 to count+3
                        
                        lines.insert(count, "LRL"+"\t"+LRL) # insert all the passed parameters into the lines variable (index,data)
                        lines.insert(count+1, "\n"+"URL"+"\t"+URL)
                        lines.insert(count+2, "\n"+"VentAmp"+"\t"+VentAmp)
                        lines.insert(count+3, "\n"+"VentPW"+"\t"+VentPW)
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

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
                        lines.insert(count+4, "\n"+"VRP"+"\t"+VRP+"\n")

                        file = open("parameters.txt","w")
                        lines = "".join(lines) # join the new lines variable

                        file.write(lines) #write to the file
                        file.close()
                        break

# def readAOO()