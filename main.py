### kevin test code for windows for pacemaker

from tkinter import * 
from screens import *
from login import *

# define the main window 
root = Tk() 
root.title("Kevin's Test!!!!")
# sets the geometry of main root window 
root.geometry("500x400")


# create 2 frames
contentFrame = Frame(root)
contentFrame.pack()
optionsFrame = Frame(root)
optionsFrame.pack(side=BOTTOM)

copyright = Label(optionsFrame, text ="Copyright (c) KMJ 2020").pack()

# add a menu to window
menu = Menu(root)
item = Menu(menu)
item.add_command(label="Exit", command=quit)
menu.add_cascade(label="Menu", menu=item)
root.config(menu=menu) 



#create the screens class
screens = Screens(contentFrame, optionsFrame)

#### start with making them log in
loginScreen  = Login(contentFrame, screens) 
loginScreen.loginDisplay() ## call the login screen, pass in the pointer to the content frame


# mainloop, runs infinitely 
mainloop() 
