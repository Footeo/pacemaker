from tkinter import *

def registerUser(uName,p1,p2):
    file = open("users.txt","r")
    rows = 0
    lines = file.readlines() #make a list where each line of the file is an index in the list

    for i in lines:
        rows = rows + 1

    if (p1==p2):
        print("passwords match")
        
        if(rows < 4): # append the new password and username
            file.close()
            file = open("users.txt",'a')
            file.write(uName + '\t') #append uName and pass to file
            file.write(p2 + "\n")
            file.close()
        else: 
            print("Max number of users has been registered")
            file.close()
            
    else:
        print("passwords don't match")
        file.close()