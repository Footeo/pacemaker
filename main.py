from tkinter import * 
from screens import *
from login import *
import settings # settings.init()

## Making changes to main to see what happends

settings.init() #initialize global variables

# define the main window 
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


# mainloop, runs infinitely 
mainloop() 
