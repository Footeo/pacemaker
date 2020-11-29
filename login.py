from tkinter import *  
import settings # global variables
import screens # screens.func() to get anything to run

class Login:
	def __init__(self, contentFrame, screens):
		self.contentFrame = contentFrame
		self.screens = screens	
	
	def loginClear(self): # clear the input text to need to reenter
		self.inputPass.delete(0,END)

	def loginDisplay(self): #login display for entering username and password and calling the login function 
		self.labelName = Label(self.contentFrame, text ="Enter Username: ")
		self.labelName.grid(row=0,column=0,padx=350)
		self.inputName = Entry(self.contentFrame)
		self.inputName.grid(row=1,column=0)
		self.labelPass = Label (self.contentFrame, text="Exter Password: ")
		self.labelPass.grid(row=2,column=0)
		self.inputPass = Entry(self.contentFrame, show="*")
		self.inputPass.grid(row=3,column=0)
		self.message = Label(self.contentFrame, text="")
		self.message.grid(row=4,column=0)
		self.loginBtn = Button(self.contentFrame, text ="Login", command = lambda: self.loginGo(self.inputName.get(),self.inputPass.get()))
		self.loginBtn.grid(row=5,column=0)
		self.registerBtn = Button(self.contentFrame, text ="Register new user", command = self.registerScreen) 
		self.registerBtn.grid(row=6,column=0)
		self.fubar = Label(self.contentFrame, text="")
		self.fubar.grid(row=7,column=0)

	def loginGo(self,uName,Pass):
		# check with usernames/passwords stored on file
		file = open("users.txt","r")
		lines = file.readlines()
		for i in lines:
			stripped = i.strip("\n")
			FName,FPass = stripped.split("\t") # store username and password into temp variables
			if (uName == FName) and (Pass == FPass):
				settings.user = FName # !Important -> stores the logged in user to the global user variable
				self.screens.mainScreen() 
				break
			else:
				self.message.configure(text="you entered INVALID login info!") 
				self.loginClear()  #This interacts with screens.py in the main.py file @ where .mainScreen() comes from
		file.close()
			
	
	## This is the display for registering a new user

	def registerScreen(self):
		self.registerText = Label(self.contentFrame, text ="Register a new user").grid(row=8,column=0)
		self.newNameLabel = Label(self.contentFrame, text ="Enter New Username: ").grid(row=9,column=0)
		self.newNameEntry = Entry(self.contentFrame)  			##Have to save this entry into a text file somehow
		self.newNameEntry.grid(row=10,column=0)
		self.newPassLabel = Label(self.contentFrame, text="Enter Password: ").grid(row=11,column=0)
		self.newPassEntry = Entry(self.contentFrame, show="*")  #have to save this password into a text file too 
		self.newPassEntry.grid(row=12,column=0)
		self.newPassLabel2 = Label(self.contentFrame, text="Reenter Password: ")
		self.newPassLabel2.grid(row=13,column=0)
		self.newPassEntry2 = Entry(self.contentFrame, show="*")  #have to save this password into a text file too 
		self.newPassEntry2.grid(row=14,column=0)
		self.registerMessage = Label(self.contentFrame, text="")
		self.registerMessage.grid(row=15,column=0)
		self.registerMessage2 = Label(self.contentFrame, text="")
		self.registerMessage2.grid(row=16,column=0)
		self.registerBtn = Button(self.contentFrame, text ="Enter", command = lambda: self.registerUser(self.newNameEntry.get(),self.newPassEntry.get(),self.newPassEntry2.get()))
		self.registerBtn.grid(row=17,column=0) #What if i make it call a function registerUser?

	##This is the code that confirms the registration for the user.

	def registerUser(self,uName,p1,p2):
		file = open("users.txt","r")
		rows = 0
		lines = file.readlines() #make a list where each line of the file is an index in the list
		word2 = "str" ## will not be a useable username 'reserved'
		for i in lines:
			rows = rows + 1
		# if passwords match
		if (p1==p2):
			self.registerMessage.configure(text = "Passwords Match")
			for j in lines:
				for word in j.split("\t"):
					if(word == uName): # if input is same as a name on file
						print("Username already taken")
						self.registerMessage2.configure(text="Username already taken")
						word2 = word
			
				
			
			if(rows < 10 and (word2 != uName)): # append the new password and username if less than 10 users and the name is unique
				file.close() #close read mode
				file = open("users.txt",'a')
				file.write(uName + '\t') #append uName and pass to file
				file.write(p2 + "\n")
				file.close() #close this file
				file = open("parameters.txt","a")
				file.write("\n"+uName+"\nAOO\nAAI\nVOO\nVVI\nDOO\nAOOR\nVOOR\nAAIR\nVVIR\nDOOR\nLRL") # when a new user is registered they get their own set of programmable parameteres added to the parameters file
				file.close() 
				self.registerMessage2.configure(text = "New User registered")

			elif(rows < 10 and (word2 == uName)): #If username is not unique
				self.registerMessage2.configure(text = "Username already taken, try a different name")
				file.close()
			else: #if 10 or more users
				self.registerMessage.configure(text = "Max number of users has been reached")
				self.registerMessage2.configure(text = "")
				file.close()

		else: #passwords don't match
			self.registerMessage.configure(text = "Passwords do not match, try again")
			self.registerMessage2.configure(text="")
			file.close()