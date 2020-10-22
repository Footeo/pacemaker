###################################################
########## kmj demo for multi window and inputs
########## python code using default tkinter libraries
########## TEST ONLY!!!!!!!!!!!!!!!!!!!!!!!!!!!
###################################################
from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
master.title("Kevin's awesome sample!")

# sets the geometry of main root window 
master.geometry("500x500") 
  

# function to open a new window  
# on a button click 
def registerWindow(): 
    # Toplevel object which will  
    # be treated as a new window 
    registerWindow = Toplevel(master) 
    # sets the title of the Toplevel widget 
    registerWindow.title("Register New User") 
    # sets the geometry of toplevel 
    registerWindow.geometry("500x500") 
    # A Label widget to show in toplevel 
    Label(registerWindow, text ="\nThis is the registration window\n\nso do registration stuff here... new username and pass, save it etc.").grid() 

def viewAoo():
    ### this would be a new window for one of the four types of heart thingys.....
    # Toplevel object which will  
    # be treated as a new window 
    aooWindow = Toplevel(master) 
    # sets the title of the Toplevel widget 
    aooWindow.title("AOO Screen") 
    # sets the geometry of toplevel 
    aooWindow.geometry("500x500") 
    # A Label widget to show in toplevel 
    Label(aooWindow, text ="\nThis is the aoo window where you do all the AOO stuff").pack()
    Label(aooWindow, text="\nso put stuff here to do!").pack()

def mainWindow():
    ### this is the main window that gives you all the options you need
    ### for the project
    mainWindow = Toplevel(master) 
    # sets the title of the Toplevel widget 
    mainWindow.title("Pacemaker by Awesome Dude Kevin") 
    # sets the geometry of toplevel 
    mainWindow.geometry("500x500") 
    # A Label widget to show in toplevel 
    Label(mainWindow, text ="\nThis is the main options window\n\nChoose an option from the menu above.").grid()
    # adding menu bar in main window 
    menu = Menu(mainWindow)
    item = Menu(menu)
    item.add_command(label="View AOO screen", command=viewAoo)
    menu.add_cascade(label="Choose Function Screen", menu=item)
    mainWindow.config(menu=menu) 

def clearLogin():
    inputPass.delete(0,END)
    
def login():
    #### obviously you need to check with real usernames that
    ## you store on disk - for now user k and pass j lets you in!!!!
    if (inputName.get() != "k") or (inputPass.get()!="j"):
        message.configure(text="you entered INVALID login info!")
    else:
        message.configure(text="");
        clearLogin() # dont leave pass entered, but we leave the username
        mainWindow() # launch the main interface window which has all your options
        
     
labelName = Label(master, text ="Enter Username: ")
labelName.pack()
inputName = Entry(master)
inputName.pack()
labelPass = Label (master, text="Exter Password: ")
labelPass.pack()
inputPass = Entry(master, show="*")
inputPass.pack()
message = Label(master, text="")
message.pack()
loginBtn = Button(master, text ="Login", command = login) 
loginBtn.pack()
registerBtn = Button(master, text ="Register", command = registerWindow) 
registerBtn.pack()
fubar = Label(master, text="for testing use name 'k' and the pass 'j' - anything else will give error")
fubar.pack()


  
  
  
  
# mainloop, runs infinitely 
mainloop() 
