from tkinter import * 
from screens import *
from login import *
import settings # settings.init()
import serial

settings.init() #initialize global variables

##hellos 

root = Tk() 
root.title("Device Control Monitor")
# sets the geometry of main root window 
root.geometry("400x620")


# create 2 frames
contentFrame = Frame(root)
contentFrame.pack()
optionsFrame = Frame(root)
optionsFrame.pack(side=BOTTOM)

# add a menu to window
menu = Menu(root)
item = Menu(menu)
item.add_command(label="Exit", command=quit)
menu.add_cascade(label="Menu", menu=item)
root.config(menu=menu) 

#create the screens class
screens = Screens(contentFrame, optionsFrame)

#create the login class
loginScreen  = Login(contentFrame, screens) 
loginScreen.loginDisplay() ## call the login screen

# Serial Port Configuration
# This method assums no timeout is needed 
ser = serial.Serial('COM1') #Modify the serial port name here
ser.write("TestTest") # Write smtg onto the port
ser.close()

# mainloop, runs infinitely 
mainloop() 
