### kevin test code for windows for pacemaker

from tkinter import * 
from screens import *
from login import *
from register import * #added

# define the main window 
root = Tk() 
root.title("Device Control Monitor")
# sets the geometry of main root window 
root.geometry("500x400")


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

#### start with making them log in
#create the login class
loginScreen  = Login(contentFrame, screens) 
loginScreen.loginDisplay() ## call the login screen, pass in the pointer to the content frame


# mainloop, runs infinitely 
mainloop() 
