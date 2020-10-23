from tkinter import *

def savePassword():
    file = askopenfile(mode='a+',filetypes=[('Text Files','users.txt')])
    p1 = self.newPass.get()
    p2 = self.newPass2.get()
    uName = self.newName.get()
    if (p1==p2):
        ## read number of rows
        rows = 0
        lines = file.read()
        lineList = lines.split("\n") #makes a list

        for i in lineList:
            rows += 1

        if (rows < 10): # append the new password and username
            file.write(uName + '\t') #uName and pass split with a tab
            file.write(p2 + "\n")
            file.close()

        else: 
            file.close()
            #send error message that there is already 10 users ('max number of users has been registered')